---
name: game-ai-news-digest
description: "Research and compile the latest video games + AI news into a verified, Simplified-Chinese digest — Section 1 in-depth (at least 5 items: facts, why, results) and Section 2 a brief roundup (at least 20 items, 3 sentences each), both strictly verified and covering only the last 7 days — PLUS Section 3, a relaxed-rules 24-hour flash roundup of general gaming and gaming-investment news (AI angle not required, lighter sourcing, aim for 10+ items, no repeats from earlier sections or the previous run). Use whenever the user asks for a gaming/AI news briefing, digest, or roundup, or when running a scheduled gaming-AI news task. Never fabricates or pads to reach counts."
---

# Video Games + AI News Digest

> This skill is **self-contained**: the helper script is embedded at the end of this file, so nothing needs to be uploaded as a separate file.

## Goal
Produce a Simplified-Chinese news digest in three sections:
- **Section 1 — in-depth, at least 5 items (strict, last 7 days):** video games + AI intersection; facts + why it's happening + what resulted.
- **Section 2 — brief roundup, at least 20 items (strict, last 7 days):** video games + AI intersection; no more than 3 sentences each.
- **Section 3 — 24-hour flash roundup, aim for at least 10 items (relaxed rules):** general gaming industry news AND gaming-related investment from the past 24 hours only. The AI angle is NOT required here, and sourcing rules are deliberately lighter (see "Section 3 rules" below) so this section reliably delivers fresh news even when the strict sections yield little that is new.

Sections 1 and 2 keep their original strict standards unchanged: **factual accuracy** (every item verified in both content and source) and **comprehensive coverage**. Section 3 exists to guarantee a steady flow of fresh, non-repeated news under relaxed—but still honest—rules. Never fabricate, duplicate, or pad any section to reach the counts.

## Tools
- **Web search** — gather candidate items with many varied queries.
- **Web fetch** — open each candidate's URL to verify it. This is the key accuracy step.
- **Code execution** — write and run the embedded `dedup_and_filter.py` (see the end of this file) to deduplicate, enforce the recency windows (7 days for Sections 1–2; 1 day for Section 3), count items deterministically, and — via `--previous` — flag items already covered in the previous run so they are not repeated.
- **(Optional) date-filtered search connector** (Firecrawl / Exa / Tavily / Perplexity Sonar via MCP) — if available, enforce the 7-day window at the source instead of inferring dates from snippets.

## Procedure — run as an explicit loop, NOT one shot
1. **Plan.** Compute two cutoffs: the 7-day cutoff (today − 7 days) for Sections 1–2, and the 24-hour cutoff (now − 24 hours) for Section 3. Note the search angles (below). If a date-filtered search connector is available, use the matching window per section.
2. **Gather wide.** Run multiple searches per angle — the strict games+AI angles for Sections 1–2 AND the broader Section 3 angles (general gaming + gaming investment, last 24 hours). Collect far more candidates than the floors so verification and de-duplication still leave enough. For each candidate, record: `title`, source `url`, publication `date` (normalize to ISO `YYYY-MM-DD`), a one-line `summary`, and a draft `section` (1, 2, or 3).
3. **Verify.** For **Sections 1–2 candidates (strict, unchanged):** web-fetch the source URL and confirm all three: (a) it resolves to a reputable source — official post, primary document, or established outlet, not a content farm, scraper, or AI-generated page; (b) the original publication date is genuinely within the last 7 days, not an SEO-refreshed or re-timestamped older page; (c) the content actually matches the claim. Drop anything that fails. A single credible source is sufficient to keep a real item. For **Section 3 candidates (relaxed):** apply the lighter checks in "Section 3 rules" below — snippet-level confirmation from a recognizable outlet is enough; web-fetch only when in doubt.
4. **Deduplicate + filter (use the embedded helper script).** On the first run in a session, copy the Python from the "Helper script" section at the end of this file into a file named `dedup_and_filter.py` in your working directory. Run it **twice**: (a) write the Section 1–2 candidates to `candidates.json` and run `python dedup_and_filter.py candidates.json` (default 7-day window); (b) write the Section 3 candidates to `candidates_24h.json` and run `python dedup_and_filter.py candidates_24h.json --days 1 --out filtered_24h.json`. The script returns deduplicated items inside each window, groups likely same-event duplicates for you to merge (keep the most authoritative source), and reports per-section counts against the floors. Ensure no item appears in more than one section; Section 1 items are excluded from Section 2, and anything already in Section 1 or 2 is excluded from Section 3.
5. **Exclude repeats from the previous run.** If a previous digest exists — from the conversation history, from a prior scheduled run's output, or from a saved `previous_items.json` — extract its items (`title`, `url`, `date`) into `previous_items.json` and add `--previous previous_items.json` to both helper runs. The report marks each unique item with `previously_covered`. **Drop every `previously_covered` item from Section 3** — that section must contain only fresh news. For Sections 1–2, prefer new items when ranking, but keep the weekly rules otherwise unchanged (a major story may legitimately stay in the weekly digest with updated results). If no previous digest is available, skip this step.
6. **Classify & rank.** Finalize each item's section (Section 1 = most significant / technically advanced game tech, AI-priority; Section 2 = any other genuine gaming + AI item; Section 3 = past-24-hour general gaming or gaming-investment item that is not already in Section 1 or 2). Within Sections 1–2, order by: AI relevance → significance to the video game industry → recency. Within Section 3, order by: significance → recency, with investment news interleaved rather than buried.
7. **Enforce coverage.** Confirm Section 1 has at least 5, Section 2 at least 20, and Section 3 aims for at least 10 distinct items (the script reports this). If short, return to step 2 and search more angles before finalizing — for Section 3 especially, broaden queries (regional outlets, investment/finance press, platform announcements) before giving up. Only if genuinely exhausted, include every qualifying item you found and add ONE brief line per short section stating how many were available — never invent or pad. Section 3's target is a goal, not a hard floor.
8. **Format & deliver.** Emit the output format below, fully in Simplified Chinese.

## Search angles (cover broadly to hit coverage)
**For Sections 1–2 (games + AI, last 7 days — unchanged):** major publishers and studios; game engines (Unreal, Unity, Godot); GPU/hardware makers (NVIDIA, AMD, Intel); AI model/tool companies; storefronts and platforms (Steam, Epic Games Store, PlayStation, Xbox, Nintendo); the gaming trade press. Topics: in-game AI / NPC behavior, generative asset / voice / animation tools, rendering and graphics, procedural generation, anti-cheat / security, networking, cloud / streaming, accessibility, developer tooling — plus AI-related business, funding, partnerships, acquisitions, regulation, and labor news in games.

**For Section 3 (general gaming + gaming investment, last 24 hours):** everything above WITHOUT the AI requirement, plus: game announcements, releases, delays, and major updates; sales/player-count milestones; platform and storefront news; studio openings, closures, layoffs, and leadership changes; esports business news; regulation and policy affecting games; and gaming-related investment — funding rounds, venture deals, M&A, IPOs, strategic stakes, divestitures, and earnings/major capital news from gaming companies. Also query investment/finance press and regional gaming outlets, which the strict sweep tends to miss.

## Section 3 rules — 24-hour flash roundup (relaxed)
Purpose: Sections 1–2 are strict and often overlap with prior runs, so they can come back thin or repetitive. Section 3 keeps those strict weekly rules untouched while guaranteeing a fresh batch of gaming and gaming-investment news every run. Its rules are deliberately lighter:
- **Window:** past 24 hours only. Run the helper with `--days 1` on the Section 3 candidates. Prefer sources that clearly show a publication time; drop anything that is plainly older being re-surfaced.
- **Scope:** ANY genuine video game industry news (AI angle NOT required) plus ANY gaming-related investment news. Small and mid-size studios, indie news of note, and regional stories all qualify — this section is meant to be broad.
- **Relaxed verification:** a search-result snippet from a recognizable outlet (established gaming trade press, mainstream tech/business press, official company channels) is sufficient — a full web-fetch of every URL is NOT required. Web-fetch only when the claim is surprising, the outlet is unfamiliar, or the date is unclear. Honesty rules still hold: never fabricate, never guess numbers or dates, keep real URLs, and prefix single-source unconfirmed reports with 「据报道」 or name the reporting outlet.
- **No repeats:** exclude anything already in Section 1 or 2 of this digest, and drop every item marked `previously_covered` against the previous run.
- **Volume target:** aim for **at least 10 items**; more is welcome. This is a goal, not a hard floor — if fewer qualify after honest searching, report what exists with one brief note, and never pad.
- **Brevity:** each item is 1–2 sentences of plain fact.

## Rules
- Report only verifiable facts — no opinions, speculation, hype, or predictions. Attribute anything alleged or unconfirmed to its source, or exclude it.
- Verification exists to remove items that are false or fabricated, not to discard items that are real and properly sourced; one credible source suffices to include an item. Full fetch-and-confirm verification applies to Sections 1–2; Section 3 uses the relaxed checks defined above — but the no-fabrication rules below apply to every section equally.
- Never fabricate facts, figures, quotes, dates, or sources. If a specific detail cannot be verified, omit that detail rather than guess.
- Preserve official proper nouns, company names, game titles, model names, engine names, and product names in their original form. Preserve every URL exactly.
- Output only the digest (plus the single shortfall line if it applies) — no introductions, conclusions, or filler.

## Output format (Simplified Chinese)

### 第一部分：游戏前沿技术与 AI（深度报道，至少 5 条）
为每条新闻重复以下结构：

## [新闻标题（中文）]
* **日期：** [已验证的原始发布日期]
* **来源链接：** [精确的规范 URL；如另有用于背景或结果的来源，一并列出]
* **核心事实（发生了什么）：**
  * [事实 1：密集、客观、细致]
  * [事实 2：密集、客观、细致]
  * [事实 N：任何其他必要的已验证具体事实、数字、技术细节、相关实体、发布时间、基准或规格]
* **背景与起因（为什么会发生）：**
  * [基于可靠来源的背景事实：前因、技术/竞争/市场驱动因素、相关方公开陈述的动机、所要解决的问题、先前的相关公告，或导致此事的监管/商业情况]
* **结果与进展（已经产生了什么结果）：**
  * [已经发生或正在发生的具体结果：可衡量的成果、官方后续行动、相关方的已记录反应、采用或推出进展等——仅限事实，不作预测]

### 第二部分：游戏与 AI 综合简讯（至少 20 条）
为每条新闻重复以下结构：

## [新闻标题（中文）]
* **日期：** [已验证的原始发布日期]
* **来源链接：** [精确的规范 URL]
* **概要（三句话以内，仅客观事实）：** [用不超过三句话，客观、准确地概述该消息的整体事实]

### 第三部分：24 小时游戏与投资快讯（目标至少 10 条；不限 AI 主题）
本部分覆盖过去 24 小时内的游戏行业动态与游戏相关投资（融资、并购、IPO、战略入股、重大财报等），不与第一、二部分及上次简报重复。为每条新闻重复以下结构：

* **[新闻标题（中文）]**（[日期或发布时间]）— [一到两句客观事实概述；如为单一来源的未经证实消息，以「据报道」或注明报道媒体开头] [来源 URL]

## Optional — delivery when run as a scheduled/triggered task (e.g., in Cowork)
If the task specifies destinations, produce two renderings of the digest:
- **Detailed → Discord:** the full three-section digest. Discord caps messages at 2,000 characters, so split into sequential messages of ~1,900 characters each (in order), or attach the full text as a .md file.
- **Condensed → email:** Section 1 as headline + one line each; Sections 2 and 3 as short bulleted lists; with source links.
Use whatever Discord/email connectors are configured. If nothing qualifies in a window, say so briefly rather than inventing items.

For recurring runs, after delivering the digest, save the final published items from ALL three sections (`title`, `url`, `date`) as `previous_items.json` (or append them to the run's output/notes) so the next run can exclude repeats in step 5 — this is what keeps Section 3 fresh from run to run.

## Helper script — write this verbatim to `dedup_and_filter.py`, then run it (used in step 4)
Stdlib-only (no internet or extra packages). On first use in a session, save it exactly as `dedup_and_filter.py` in your working directory.

```python
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
```
