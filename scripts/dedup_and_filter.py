#!/usr/bin/env python3
"""
dedup_and_filter.py — deterministic helper for the game-ai-news-digest skill.

Takes a JSON list of candidate news items and:
  1. Filters to items whose publication date is within the last N days (default 7).
  2. De-duplicates: merges items that share a normalized URL or a near-identical
     title into groups (so the model can keep the single most authoritative source).
  3. Reports per-section counts and whether the floors are met (Section 1 >= 5,
     Section 2 >= 20, Section 3 >= 10 by default; run separately with --days 1
     for Section 3 candidates, whose target is a soft goal rather than a floor).
  4. Optionally compares against the previous run (--previous previous_items.json,
     a JSON array with at least "title" and "url" per item): marks each unique item
     with "previously_covered" and reports "new_vs_previous". Previously covered
     items must be dropped from Section 3 (that section is fresh-news only) and
     deprioritized in Sections 1-2.

Stdlib only — no internet access or extra packages required, so it runs the same
in Cowork, claude.ai code execution, and the Claude API container.

INPUT (candidates.json): a JSON array of objects, e.g.
  [
    {"title": "...", "url": "https://...", "date": "2026-06-15",
     "summary": "...", "section": 1},
    ...
  ]
  - date must be ISO (YYYY-MM-DD or a full ISO datetime); items without a
    parseable date are reported separately and never silently kept.
  - section is 1 or 2 (optional; missing -> counted as "unclassified").

USAGE:
  python dedup_and_filter.py candidates.json
  python dedup_and_filter.py candidates.json --days 7 --as-of 2026-06-17 \
      --title-threshold 0.82 --s1-floor 5 --s2-floor 20 --out filtered.json
  # Sections 1-2 with repeat-check against the previous digest:
  python dedup_and_filter.py candidates.json --previous previous_items.json
  # Section 3 (24-hour flash) candidates:
  python dedup_and_filter.py candidates_24h.json --days 1 \
      --previous previous_items.json --out filtered_24h.json

OUTPUT:
  - Prints a JSON report to stdout (also written to --out, default filtered.json).
  - Prints a short human-readable summary to stderr.
"""

import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta
from difflib import SequenceMatcher
from urllib.parse import urlsplit, urlunsplit

TRACKING_PREFIXES = ("utm_", "fbclid", "gclid", "mc_", "ref", "ref_src", "igshid")


def parse_iso_date(value):
    """Return a date from an ISO date/datetime string, or None if unparseable."""
    if not value or not isinstance(value, str):
        return None
    v = value.strip()
    # Try full ISO datetime first (tolerate trailing Z).
    try:
        return datetime.fromisoformat(v.replace("Z", "+00:00")).date()
    except ValueError:
        pass
    # Try plain date.
    try:
        return datetime.strptime(v[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def normalize_url(url):
    """Lowercase host, drop scheme differences, strip www, query, fragment, and
    trailing slash, so the same article at slightly different URLs collapses."""
    if not url or not isinstance(url, str):
        return ""
    try:
        parts = urlsplit(url.strip())
    except ValueError:
        return url.strip().lower()
    host = (parts.netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]
    path = (parts.path or "").rstrip("/")
    # Drop scheme and query/fragment entirely for comparison purposes.
    return urlunsplit(("", host, path, "", "")).lower()


def normalize_title(title):
    """Lowercase, strip punctuation, collapse whitespace for fuzzy comparison."""
    if not title or not isinstance(title, str):
        return ""
    t = title.lower()
    t = re.sub(r"[^\w\s]", " ", t, flags=re.UNICODE)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def title_similarity(a, b):
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def bigram_overlap(a, b):
    """Share of character bigrams of the shorter title that also occur in the other title.
    Catches the same event reported under differently worded headlines (e.g. two outlets covering one
    lawsuit), which plain sequence similarity misses. Works for Chinese and English alike."""
    def grams(t):
        t = re.sub(r"[\W_]+", "", (t or "").lower())
        return {t[i:i + 2] for i in range(len(t) - 1)}
    ga, gb = grams(a), grams(b)
    if len(ga) < 4 or len(gb) < 4:
        return 0.0
    return len(ga & gb) / min(len(ga), len(gb))


def cluster_items(items, title_threshold):
    """Greedy clustering: an item joins an existing cluster if it shares a
    normalized URL with any member, or its title is similar enough to the
    cluster's representative. Otherwise it starts a new cluster."""
    clusters = []
    for item in items:
        nurl = item["_nurl"]
        ntitle = item["_ntitle"]
        placed = False
        for cluster in clusters:
            rep = cluster[0]
            same_url = bool(nurl) and nurl == rep["_nurl"]
            similar_title = title_similarity(ntitle, rep["_ntitle"]) >= title_threshold
            # Also check URL match against any member, not just the rep.
            if not same_url:
                same_url = any(bool(nurl) and nurl == m["_nurl"] for m in cluster)
            if same_url or similar_title:
                cluster.append(item)
                placed = True
                break
        if not placed:
            clusters.append([item])
    return clusters


def strip_internal(item):
    return {k: v for k, v in item.items() if not k.startswith("_")}


def main():
    ap = argparse.ArgumentParser(description="Dedup + 7-day filter + count for the news digest skill.")
    ap.add_argument("input", help="Path to candidates.json (a JSON array of items).")
    ap.add_argument("--days", type=int, default=7, help="Recency window in days (default 7).")
    ap.add_argument("--as-of", default=None, help="Reference date YYYY-MM-DD (default: today).")
    ap.add_argument("--title-threshold", type=float, default=0.82,
                    help="Title-similarity ratio to treat two items as the same event (default 0.82).")
    ap.add_argument("--s1-floor", type=int, default=5, help="Minimum Section 1 items (default 5).")
    ap.add_argument("--s2-floor", type=int, default=20, help="Minimum Section 2 items (default 20).")
    ap.add_argument("--s3-floor", type=int, default=10,
                    help="Soft target for Section 3 (24-hour flash) items (default 10).")
    ap.add_argument("--event-threshold", type=float, default=0.45,
                    help="Shared-bigram overlap with a previous title above which an item counts as the same event (default 0.45).")
    ap.add_argument("--previous", default=None,
                    help="Path to previous_items.json (items from the previous digest run); marks repeats via 'previously_covered'.")
    ap.add_argument("--out", default="filtered.json", help="Where to write the JSON report (default filtered.json).")
    args = ap.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as fh:
            raw = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        print("ERROR reading input: %s" % exc, file=sys.stderr)
        sys.exit(1)

    if not isinstance(raw, list):
        print("ERROR: input must be a JSON array of item objects.", file=sys.stderr)
        sys.exit(1)

    as_of = parse_iso_date(args.as_of) if args.as_of else date.today()
    if as_of is None:
        print("ERROR: --as-of must be YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)
    cutoff = as_of - timedelta(days=args.days)

    in_window, out_of_window, invalid_date = [], [], []
    for it in raw:
        if not isinstance(it, dict):
            invalid_date.append({"raw": it, "reason": "not an object"})
            continue
        d = parse_iso_date(it.get("date"))
        item = dict(it)
        item["_nurl"] = normalize_url(it.get("url", ""))
        item["_ntitle"] = normalize_title(it.get("title", ""))
        if d is None:
            invalid_date.append(strip_internal(item))
        elif d < cutoff or d > as_of:
            rec = strip_internal(item)
            rec["_date_parsed"] = d.isoformat()
            out_of_window.append(rec)
        else:
            item["_date_parsed"] = d.isoformat()
            in_window.append(item)

    clusters = cluster_items(in_window, args.title_threshold)

    unique_items, duplicate_groups = [], []
    for cluster in clusters:
        # Representative = earliest-listed; the model decides authority when merging.
        rep = strip_internal(cluster[0])
        members = [strip_internal(m) for m in cluster]
        entry = {"representative": rep, "members": members, "duplicate_count": len(members)}
        unique_items.append(entry)
        if len(members) > 1:
            duplicate_groups.append(members)

    def section_of(entry):
        return entry["representative"].get("section")

    s1 = sum(1 for e in unique_items if section_of(e) == 1)
    s2 = sum(1 for e in unique_items if section_of(e) == 2)
    s3 = sum(1 for e in unique_items if section_of(e) == 3)
    unclassified = sum(1 for e in unique_items if section_of(e) not in (1, 2, 3))

    # --- Compare against the previous run (repeat check) ---
    new_vs_previous = None
    if args.previous:
        try:
            with open(args.previous, "r", encoding="utf-8") as fh:
                prev_raw = json.load(fh)
        except (OSError, json.JSONDecodeError) as exc:
            print("ERROR reading --previous: %s" % exc, file=sys.stderr)
            sys.exit(1)
        if not isinstance(prev_raw, list):
            print("ERROR: --previous must be a JSON array of item objects.", file=sys.stderr)
            sys.exit(1)
        prev_urls = set()
        prev_titles = []
        for p in prev_raw:
            if not isinstance(p, dict):
                continue
            nu = normalize_url(p.get("url", ""))
            if nu:
                prev_urls.add(nu)
            nt = normalize_title(p.get("title", ""))
            if nt:
                prev_titles.append(nt)

        def previously_covered(entry):
            for m in entry["members"]:
                nu = normalize_url(m.get("url", ""))
                if nu and nu in prev_urls:
                    return True
                nt = normalize_title(m.get("title", ""))
                if nt and any(title_similarity(nt, pt) >= args.title_threshold
                              for pt in prev_titles):
                    return True
                # same event, different headline/outlet: high shared-bigram overlap with a previous title
                if nt and any(bigram_overlap(nt, pt) >= args.event_threshold for pt in prev_titles):
                    return True
            return False

        new_vs_previous = 0
        for entry in unique_items:
            covered = previously_covered(entry)
            entry["previously_covered"] = covered
            if not covered:
                new_vs_previous += 1

    report = {
        "as_of": as_of.isoformat(),
        "cutoff": cutoff.isoformat(),
        "window_days": args.days,
        "summary": {
            "input_items": len(raw),
            "in_window": len(in_window),
            "out_of_window": len(out_of_window),
            "invalid_date": len(invalid_date),
            "unique_after_dedup": len(unique_items),
            "duplicate_clusters": len(duplicate_groups),
            "section1_count": s1,
            "section2_count": s2,
            "section3_count": s3,
            "unclassified_count": unclassified,
            "section1_floor": args.s1_floor,
            "section2_floor": args.s2_floor,
            "section3_target": args.s3_floor,
            "section1_floor_met": s1 >= args.s1_floor,
            "section2_floor_met": s2 >= args.s2_floor,
            "section3_target_met": s3 >= args.s3_floor,
            "new_vs_previous": new_vs_previous,
            "previously_covered_count": (len(unique_items) - new_vs_previous)
                                        if new_vs_previous is not None else None,
        },
        "unique_items": unique_items,
        "duplicate_groups": duplicate_groups,
        "dropped_out_of_window": out_of_window,
        "dropped_invalid_date": invalid_date,
    }

    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=2)

    s = report["summary"]
    print("Dedup/filter report (as of %s, window %d days, cutoff %s):"
          % (report["as_of"], report["window_days"], report["cutoff"]), file=sys.stderr)
    print("  input=%d  in_window=%d  out_of_window=%d  invalid_date=%d"
          % (s["input_items"], s["in_window"], s["out_of_window"], s["invalid_date"]), file=sys.stderr)
    print("  unique_after_dedup=%d  duplicate_clusters=%d"
          % (s["unique_after_dedup"], s["duplicate_clusters"]), file=sys.stderr)
    s3_only = s["section3_count"] > 0 and s["section1_count"] == 0 and s["section2_count"] == 0
    if not s3_only:
        print("  Section 1: %d / %d  -> %s" % (s["section1_count"], s["section1_floor"],
              "OK" if s["section1_floor_met"] else "BELOW FLOOR — search more"), file=sys.stderr)
        print("  Section 2: %d / %d  -> %s" % (s["section2_count"], s["section2_floor"],
              "OK" if s["section2_floor_met"] else "BELOW FLOOR — search more"), file=sys.stderr)
    if s["section3_count"]:
        print("  Section 3 (24h flash): %d / %d target -> %s"
              % (s["section3_count"], s["section3_target"],
                 "OK" if s["section3_target_met"]
                 else "below soft target — broaden 24h queries before finalizing"), file=sys.stderr)
    if s["unclassified_count"]:
        print("  unclassified (no section): %d" % s["unclassified_count"], file=sys.stderr)
    if s["new_vs_previous"] is not None:
        print("  vs previous run: %d new, %d previously covered "
              "(drop repeats from Section 3; deprioritize in Sections 1-2)"
              % (s["new_vs_previous"], s["previously_covered_count"]), file=sys.stderr)
    print("  full report written to: %s" % args.out, file=sys.stderr)

    # Machine-readable report to stdout.
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
