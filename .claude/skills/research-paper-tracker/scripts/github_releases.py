#!/usr/bin/env python3
"""
github_releases.py — GitHub Releases candidate fetcher for Part B (Research -> Product)
of the research-paper-tracker skill.

What it does
------------
1. Reads `references/product-sources.md` and collects every `github: <org>/<repo>` or
   `github: <org>/*` line (comma-separated lists on one line are fine).
2. For `<org>/*`, lists the org's public repos (most recently pushed first, capped by
   --max-repos-per-org) so the call budget stays inside GitHub's unauthenticated limit
   (60 requests/hour; set GITHUB_TOKEN for 5000/hour).
3. Pulls recent releases per repo and keeps those whose `published_at` falls inside the
   window (default last 90 days). Pre-releases are kept and flagged.
4. Applies a light topic-keyword filter (3D / world model / animation / engine terms) to the
   repo name + description + release name/body and records which keywords matched. Items
   with no keyword match are still written, under `off_topic_candidates`, so nothing is
   silently dropped.
5. Writes JSON to --out. Every item is a LEAD only: the skill must still verify the release
   against the primary source and apply the company/topic/tier gates from
   references/product-criteria.md.

Network: reaches api.github.com. If blocked, exits non-zero with a clear message so the skill
falls back to manual web search/fetch of the sources in references/product-sources.md.

USAGE
-----
  python scripts/github_releases.py                          # 90 days, all orgs in the sources file
  python scripts/github_releases.py --as-of 2026-09-12 --days 90 --out github_release_candidates.json
  python scripts/github_releases.py --orgs NVIDIA,Tencent-Hunyuan --max-repos-per-org 20
"""

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"
DEFAULT_SOURCES = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                               "references", "product-sources.md")

TOPIC_KEYWORDS = {
    "3d": ["3d", "mesh", "gaussian", "splat", "nerf", "texture", "pbr", "render", "reconstruction",
           "point cloud", "sdf", "trellis", "hunyuan3d", "shape", "geometry", "usd", "omniverse"],
    "world_models": ["world model", "worldmodel", "world-model", "interactive video", "game world",
                     "cosmos", "genie", "simulat", "action-conditioned", "playable", "gamecraft"],
    "character_animation": ["motion", "animation", "retarget", "rig", "skeleton", "avatar", "humanoid",
                            "character", "pose", "mocap", "gesture", "facial", "lip"],
    "game_engine": ["unity", "unreal", "engine", "dlss", "ray tracing", "rtx", "shader", "gpu",
                    "real-time", "realtime", "sdk", "plugin", "isaac", "physx"],
}


def log(msg):
    print(msg, file=sys.stderr)


def gh_get(url, token=None, retries=2):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "research-paper-tracker-skill",
        **({"Authorization": "Bearer " + token} if token else {}),
    })
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                remaining = r.headers.get("X-RateLimit-Remaining")
                return json.loads(r.read().decode("utf-8")), remaining
        except urllib.error.HTTPError as e:
            if e.code == 403 and "rate limit" in (e.read().decode("utf-8", "ignore").lower()):
                return None, "0"
            if e.code == 404:
                return None, None
            if attempt < retries:
                time.sleep(1.5)
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt < retries:
                time.sleep(1.5)
                continue
            raise


def parse_sources(path):
    """Return ({org: set(repos) | {'*'}}, company_by_org)."""
    targets, company = {}, {}
    if not os.path.exists(path):
        log("WARN: sources file not found: %s" % path)
        return targets, company
    current_company = None
    for line in open(path, encoding="utf-8"):
        h = re.match(r"^##\s+(.+)", line)
        if h:
            current_company = h.group(1).strip()
            continue
        m = re.match(r"^\s*-?\s*github:\s*(.+)", line, re.I)
        if not m:
            continue
        for spec in m.group(1).split(","):
            spec = spec.strip().split(" ")[0].strip("`")
            if "/" not in spec:
                continue
            org, repo = spec.split("/", 1)
            targets.setdefault(org, set()).add(repo)
            company.setdefault(org, current_company or org)
    return targets, company


def list_org_repos(org, token, max_repos):
    repos = []
    page = 1
    while len(repos) < max_repos:
        url = "%s/orgs/%s/repos?type=public&sort=pushed&direction=desc&per_page=100&page=%d" % (API, org, page)
        data, remaining = gh_get(url, token)
        if data is None:
            # maybe a user account rather than an org
            url = "%s/users/%s/repos?type=owner&sort=pushed&direction=desc&per_page=100&page=%d" % (API, org, page)
            data, remaining = gh_get(url, token)
        if not data:
            break
        repos.extend(data)
        if len(data) < 100:
            break
        page += 1
    return repos[:max_repos], remaining


def topic_matches(text):
    t = text.lower()
    hits = {}
    for group, kws in TOPIC_KEYWORDS.items():
        found = [k for k in kws if k in t]
        if found:
            hits[group] = found
    return hits


def main():
    ap = argparse.ArgumentParser(description="Fetch recent GitHub releases from tracked orgs for the research-paper-tracker skill.")
    ap.add_argument("--as-of", default=None, help="Reference date YYYY-MM-DD (default: today UTC)")
    ap.add_argument("--days", type=int, default=90)
    ap.add_argument("--sources", default=DEFAULT_SOURCES, help="Path to references/product-sources.md")
    ap.add_argument("--orgs", default=None, help="Comma-separated org subset (overrides sources file orgs)")
    ap.add_argument("--max-repos-per-org", type=int, default=15)
    ap.add_argument("--releases-per-repo", type=int, default=10)
    ap.add_argument("--out", default="github_release_candidates.json")
    ap.add_argument("--dry-run", action="store_true", help="Only parse the sources file and print the targets; no network calls")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    today = dt.date.fromisoformat(args.as_of) if args.as_of else dt.datetime.now(dt.timezone.utc).date()
    cutoff = today - dt.timedelta(days=args.days)
    log("Window: %s .. %s (%d days)" % (cutoff, today, args.days))

    targets, company_by_org = parse_sources(args.sources)
    if args.orgs:
        wanted = [o.strip() for o in args.orgs.split(",") if o.strip()]
        targets = {o: targets.get(o, {"*"}) for o in wanted}
    if not targets:
        log("ERROR: no github targets found. Add `github: org/repo` lines to the sources file or pass --orgs.")
        sys.exit(2)

    if args.dry_run:
        for org, repos in sorted(targets.items()):
            log("  %s (%s): %s" % (org, company_by_org.get(org, org), ", ".join(sorted(repos))))
        return

    # connectivity check
    try:
        _, remaining = gh_get(API + "/rate_limit", token)
    except Exception as e:
        log("ERROR: cannot reach api.github.com (%s). Fall back to manual web search/fetch per references/product-sources.md." % e)
        sys.exit(3)
    log("GitHub API reachable; requests remaining this hour: %s" % remaining)
    if remaining == "0":
        log("ERROR: GitHub API rate limit is exhausted for this IP (unauthenticated limit is 60/hour, shared egress IPs exhaust it fast). "
            "Set GITHUB_TOKEN, wait for the reset, or fall back to manual web search/fetch per references/product-sources.md.")
        sys.exit(3)

    candidates, off_topic, errors = [], [], []
    queries_ok = 0
    for org, repos in targets.items():
        try:
            if "*" in repos:
                repo_objs, remaining = list_org_repos(org, token, args.max_repos_per_org)
                if repo_objs is None:
                    repo_objs = []
                repo_names = [r["name"] for r in repo_objs]
                desc_by_name = {r["name"]: (r.get("description") or "") for r in repo_objs}
                repo_names += [r for r in repos if r != "*"]
            else:
                repo_names = sorted(repos)
                desc_by_name = {}
        except Exception as e:
            errors.append({"org": org, "error": str(e)})
            continue

        for repo in repo_names:
            url = "%s/repos/%s/%s/releases?per_page=%d" % (API, org, repo, args.releases_per_repo)
            try:
                rels, remaining = gh_get(url, token)
            except Exception as e:
                errors.append({"repo": "%s/%s" % (org, repo), "error": str(e)})
                continue
            if remaining == "0":
                log("WARN: GitHub rate limit exhausted at %s/%s; stopping early. Set GITHUB_TOKEN to raise the limit." % (org, repo))
                errors.append({"repo": "%s/%s" % (org, repo), "error": "rate limit exhausted"})
                break
            queries_ok += 1
            if not rels:
                continue
            for rel in rels:
                pub = rel.get("published_at") or rel.get("created_at")
                if not pub:
                    continue
                pub_date = dt.date.fromisoformat(pub[:10])
                if pub_date < cutoff or pub_date > today:
                    continue
                text = " ".join([repo, desc_by_name.get(repo, ""), rel.get("name") or "", (rel.get("body") or "")[:2000]])
                hits = topic_matches(text)
                item = {
                    "company": company_by_org.get(org, org),
                    "org": org,
                    "repo": repo,
                    "repo_url": "https://github.com/%s/%s" % (org, repo),
                    "repo_description": desc_by_name.get(repo, ""),
                    "release_name": rel.get("name") or rel.get("tag_name"),
                    "tag": rel.get("tag_name"),
                    "published_at": pub[:10],
                    "prerelease": bool(rel.get("prerelease")),
                    "release_url": rel.get("html_url"),
                    "body_excerpt": (rel.get("body") or "")[:600],
                    "topic_hits": hits,
                }
                (candidates if hits else off_topic).append(item)

    candidates.sort(key=lambda x: x["published_at"], reverse=True)
    off_topic.sort(key=lambda x: x["published_at"], reverse=True)
    out = {
        "as_of": today.isoformat(),
        "cutoff": cutoff.isoformat(),
        "days": args.days,
        "orgs_queried": sorted(targets.keys()),
        "queries_ok": queries_ok,
        "errors": errors,
        "note": "Every item is a lead. Verify against the primary source and apply the company/topic/tier gates before use.",
        "candidates": candidates,
        "off_topic_candidates": off_topic,
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    log("Wrote %d on-topic and %d off-topic release leads to %s (%d repo queries ok, %d errors)"
        % (len(candidates), len(off_topic), args.out, queries_ok, len(errors)))
    if queries_ok == 0:
        sys.exit(4)


if __name__ == "__main__":
    main()
