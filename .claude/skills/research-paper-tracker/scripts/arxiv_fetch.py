#!/usr/bin/env python3
"""
arxiv_fetch.py — deterministic arXiv candidate fetcher for the
research-paper-tracker skill.

What it does
------------
1. Queries the official arXiv API (http://export.arxiv.org/api/query) across a
   set of categories and topic keyword groups, sorted by most-recent submission.
2. Parses the Atom 1.0 response (stdlib only — no third-party packages).
3. Filters to papers whose ORIGINAL submission date falls within the recency
   window (default: last 30 days), computed deterministically here rather than
   eyeballed from snippets.
4. De-duplicates by arXiv ID (a paper that matches several queries appears once).
5. Emits a clean JSON list of candidates for the model to affiliation-verify.

What it deliberately does NOT do
--------------------------------
It does NOT decide whether a paper is from a "qualified" team. arXiv's API only
sometimes includes <arxiv:affiliation>, and that field is usually empty, so it
cannot be trusted as the affiliation gate. This script surfaces any inline
affiliation strings it finds as a *hint* only (`affiliation_hints`). The skill's
verification step (fetch the abstract page / PDF first page and read the real
author affiliations) is what actually decides qualification.

Network note
------------
This reaches export.arxiv.org. In sandboxes where that host is blocked, run this
in the environment where the skill is actually used (e.g. Claude chat code
execution or an agent runtime with outbound access). If the API is unreachable,
the script exits non-zero with a clear message so the skill can fall back to
web_search / web_fetch against arxiv.org listing pages instead.

USAGE
-----
  python arxiv_fetch.py                      # defaults: 30-day window, all topic groups
  python arxiv_fetch.py --days 30 --out candidates.json
  python arxiv_fetch.py --as-of 2026-06-18 --per-query 80 --max-pages 3
  python arxiv_fetch.py --topics "3d,world_models"   # subset of topic groups

OUTPUT
------
  - Writes a JSON object to --out (default arxiv_candidates.json) containing the
    run parameters and a `candidates` array.
  - Prints a short human-readable summary to stderr.
  - Prints the same JSON object to stdout (for piping).
"""

import argparse
import json
import sys
import time
from datetime import date, datetime, timedelta, timezone
from urllib.parse import urlencode
from urllib.error import HTTPError, URLError
import urllib.request
import xml.etree.ElementTree as ET

API_URL = "http://export.arxiv.org/api/query"

ATOM = "http://www.w3.org/2005/Atom"
ARXIV = "http://arxiv.org/schemas/atom"
NS = {"atom": ATOM, "arxiv": ARXIV}

# arXiv categories most relevant to the four topic areas.
#   cs.GR = Graphics (rendering, animation, game engines)
#   cs.CV = Computer Vision (3D reconstruction/generation, video/world models, animation)
#   cs.LG = Machine Learning (world models, generative models)
#   cs.AI = Artificial Intelligence (agents, world models)
#   cs.RO = Robotics (world models for embodied agents, physics)
DEFAULT_CATEGORIES = ["cs.GR", "cs.CV", "cs.LG", "cs.AI", "cs.RO"]

# Topic keyword groups. Each group is OR-ed internally; the script runs one query
# per (category x group) combination so recall stays high. Keep phrases specific
# enough to be on-topic but broad enough not to miss relevant work.
TOPIC_GROUPS = {
    "3d": [
        "3D generation", "3D reconstruction", "Gaussian splatting", "neural rendering",
        "mesh generation", "novel view synthesis", "text-to-3D", "3D scene",
    ],
    "world_models": [
        "world model", "world models", "video generation", "interactive environment",
        "neural simulation", "playable world", "video world model",
    ],
    "character_animation": [
        "character animation", "motion synthesis", "motion generation",
        "human motion", "physics-based animation", "motion capture", "avatar animation",
        "skeletal animation",
    ],
    "game_engine": [
        "game engine", "neural game engine", "game generation", "real-time rendering",
        "procedural generation", "playable game", "game simulation",
    ],
}


def build_query(category, keywords):
    """Build an arXiv search_query string: category AND (kw1 OR kw2 OR ...).

    Keywords are matched against the abstract (abs:) so we catch papers that use
    the term in substance, not only in the title.
    """
    ors = " OR ".join('abs:"%s"' % kw for kw in keywords)
    return "cat:%s AND (%s)" % (category, ors)


def fetch_page(search_query, start, per_query, user_agent, timeout=30):
    """Fetch one page of results from the arXiv API. Returns the raw XML string."""
    params = {
        "search_query": search_query,
        "start": start,
        "max_results": per_query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = API_URL + "?" + urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": user_agent})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "replace")


def parse_iso_dt(value):
    """Parse an arXiv Atom timestamp (e.g. 2026-06-01T17:59:59Z) to a date."""
    if not value:
        return None
    v = value.strip()
    try:
        return datetime.fromisoformat(v.replace("Z", "+00:00")).date()
    except ValueError:
        try:
            return datetime.strptime(v[:10], "%Y-%m-%d").date()
        except ValueError:
            return None


def text_or_empty(node):
    return node.text.strip() if node is not None and node.text else ""


def parse_entries(xml_text):
    """Parse an Atom feed into a list of paper dicts. Tolerates malformed XML by
    returning whatever parsed successfully (and signals a parse error upstream)."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return None  # signal parse failure to caller

    papers = []
    for entry in root.findall("atom:entry", NS):
        id_url = text_or_empty(entry.find("atom:id", NS))
        # id_url looks like http://arxiv.org/abs/2506.01234v1
        arxiv_id = id_url.rsplit("/abs/", 1)[-1] if "/abs/" in id_url else id_url
        base_id = arxiv_id.split("v")[0] if arxiv_id else arxiv_id

        title = " ".join(text_or_empty(entry.find("atom:title", NS)).split())
        summary = " ".join(text_or_empty(entry.find("atom:summary", NS)).split())
        published = text_or_empty(entry.find("atom:published", NS))
        updated = text_or_empty(entry.find("atom:updated", NS))

        authors = []
        affiliation_hints = []
        for a in entry.findall("atom:author", NS):
            name = text_or_empty(a.find("atom:name", NS))
            if name:
                authors.append(name)
            aff = a.find("arxiv:affiliation", NS)
            aff_text = text_or_empty(aff)
            if aff_text:
                affiliation_hints.append(aff_text)

        categories = [c.get("term") for c in entry.findall("atom:category", NS) if c.get("term")]
        primary = entry.find("arxiv:primary_category", NS)
        primary_cat = primary.get("term") if primary is not None else (categories[0] if categories else "")

        # Prefer the abstract (/abs/) and PDF links for the verification step.
        abs_url = "https://arxiv.org/abs/%s" % base_id if base_id else id_url
        pdf_url = "https://arxiv.org/pdf/%s" % base_id if base_id else ""

        papers.append({
            "arxiv_id": base_id,
            "version_id": arxiv_id,
            "title": title,
            "abstract": summary,
            "authors": authors,
            "affiliation_hints": affiliation_hints,  # usually empty; never authoritative
            "categories": categories,
            "primary_category": primary_cat,
            "published": published,
            "updated": updated,
            "abs_url": abs_url,
            "pdf_url": pdf_url,
        })
    return papers


def main():
    ap = argparse.ArgumentParser(description="Fetch recent arXiv candidates for the research-paper-tracker skill.")
    ap.add_argument("--days", type=int, default=30, help="Recency window in days, based on original submission date (default 30).")
    ap.add_argument("--as-of", default=None, help="Reference date YYYY-MM-DD (default: today, UTC).")
    ap.add_argument("--categories", default=",".join(DEFAULT_CATEGORIES),
                    help="Comma-separated arXiv categories to search.")
    ap.add_argument("--topics", default=",".join(TOPIC_GROUPS.keys()),
                    help="Comma-separated topic groups: %s" % ", ".join(TOPIC_GROUPS.keys()))
    ap.add_argument("--per-query", type=int, default=100, help="Results per API page (default 100, arXiv max 2000 but be polite).")
    ap.add_argument("--max-pages", type=int, default=1, help="Pages to page through per query if results keep falling in-window (default 1).")
    ap.add_argument("--sleep", type=float, default=3.0, help="Seconds to wait between API calls (arXiv asks for ~3s; default 3).")
    ap.add_argument("--user-agent", default="research-paper-tracker/1.0 (mailto:example@example.com)",
                    help="User-Agent to send (arXiv requests a descriptive UA).")
    ap.add_argument("--out", default="arxiv_candidates.json", help="Where to write the JSON output.")
    args = ap.parse_args()

    as_of = parse_iso_dt(args.as_of) if args.as_of else datetime.now(timezone.utc).date()
    if as_of is None:
        print("ERROR: --as-of must be YYYY-MM-DD.", file=sys.stderr)
        sys.exit(2)
    cutoff = as_of - timedelta(days=args.days)

    categories = [c.strip() for c in args.categories.split(",") if c.strip()]
    topic_keys = [t.strip() for t in args.topics.split(",") if t.strip()]
    unknown = [t for t in topic_keys if t not in TOPIC_GROUPS]
    if unknown:
        print("ERROR: unknown topic group(s): %s. Valid: %s"
              % (", ".join(unknown), ", ".join(TOPIC_GROUPS.keys())), file=sys.stderr)
        sys.exit(2)

    by_id = {}
    matched_queries = {}  # arxiv_id -> set of "cat/topic" labels that surfaced it
    queries_run = 0
    network_errors = 0
    parse_errors = 0

    for cat in categories:
        for topic in topic_keys:
            sq = build_query(cat, TOPIC_GROUPS[topic])
            label = "%s/%s" % (cat, topic)
            for page in range(args.max_pages):
                start = page * args.per_query
                try:
                    xml_text = fetch_page(sq, start, args.per_query, args.user_agent)
                except HTTPError as exc:
                    print("WARN: HTTP %s for query [%s] start=%d" % (exc.code, label, start), file=sys.stderr)
                    network_errors += 1
                    break
                except (URLError, TimeoutError) as exc:
                    print("WARN: network error for query [%s] start=%d: %s" % (label, start, exc), file=sys.stderr)
                    network_errors += 1
                    break
                queries_run += 1

                entries = parse_entries(xml_text)
                if entries is None:
                    print("WARN: could not parse XML for query [%s] start=%d" % (label, start), file=sys.stderr)
                    parse_errors += 1
                    break
                if not entries:
                    break  # no more results for this query

                page_had_in_window = False
                for p in entries:
                    d = parse_iso_dt(p.get("published"))
                    if d is None:
                        continue
                    if d < cutoff or d > as_of:
                        continue
                    page_had_in_window = True
                    aid = p["arxiv_id"]
                    if aid not in by_id:
                        by_id[aid] = p
                        matched_queries[aid] = set()
                    matched_queries[aid].add(label)

                # Because results are sorted newest-first, once a full page has no
                # in-window items we've paged past the window for this query.
                if not page_had_in_window:
                    break
                if page < args.max_pages - 1:
                    time.sleep(args.sleep)
            time.sleep(args.sleep)

    candidates = []
    for aid, p in by_id.items():
        p = dict(p)
        p["matched_queries"] = sorted(matched_queries.get(aid, []))
        candidates.append(p)
    # Newest first for convenience.
    candidates.sort(key=lambda x: x.get("published", ""), reverse=True)

    result = {
        "as_of": as_of.isoformat(),
        "cutoff": cutoff.isoformat(),
        "window_days": args.days,
        "categories": categories,
        "topics": topic_keys,
        "queries_run": queries_run,
        "network_errors": network_errors,
        "parse_errors": parse_errors,
        "candidate_count": len(candidates),
        "candidates": candidates,
    }

    # If we ran zero successful queries, that's a hard failure — tell the skill to fall back.
    if queries_run == 0:
        print("ERROR: no arXiv API queries succeeded (host may be blocked). "
              "Fall back to web_search / web_fetch against arxiv.org listings.", file=sys.stderr)
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(result, fh, ensure_ascii=False, indent=2)
        sys.exit(1)

    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=2)

    print("arXiv fetch (as of %s, window %d days, cutoff %s):"
          % (result["as_of"], result["window_days"], result["cutoff"]), file=sys.stderr)
    print("  categories=%s" % ",".join(categories), file=sys.stderr)
    print("  topics=%s" % ",".join(topic_keys), file=sys.stderr)
    print("  queries_run=%d  network_errors=%d  parse_errors=%d"
          % (queries_run, network_errors, parse_errors), file=sys.stderr)
    print("  unique in-window candidates=%d" % len(candidates), file=sys.stderr)
    print("  -> written to %s" % args.out, file=sys.stderr)
    if candidates:
        print("  newest: [%s] %s (%s)"
              % (candidates[0]["arxiv_id"], candidates[0]["title"][:70], candidates[0]["published"][:10]),
              file=sys.stderr)

    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
