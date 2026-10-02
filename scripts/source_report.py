"""Monthly source report for the news digest.

Usage: python scripts/source_report.py YYYY-MM [--out reports/sources-YYYY-MM.md]

Scans digests/YYYY-MM-*/news.md and the dedup reports' denied drops (if present in digests/*/filtered*.json)
and writes a Markdown report: links per outlet by section, tier of each outlet (Tier 1 / Tier 2 / unlisted /
denied) per news-sources.md, outlets that appear in the digest despite being on the deny list, aggregator links,
and concentration (share of the top 3 outlets). The routine posts a summary and the recommendations it derives
from this report on the last day of the month; the maintainer then updates news-sources.md.
"""
import collections, glob, json, os, re, sys
from urllib.parse import urlsplit

month = sys.argv[1]
out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else os.path.join("reports", f"sources-{month}.md")
SRC = os.path.join(".claude", "skills", "game-ai-news-digest", "references", "news-sources.md")

def host(u):
    h = (urlsplit(u).netloc or "").lower()
    return h[4:] if h.startswith("www.") else h

# --- tiers from news-sources.md ---
tier_of = {}
if os.path.exists(SRC):
    cur = None
    for line in open(SRC, encoding="utf-8"):
        s = line.strip()
        if s.startswith("## "):
            cur = "T1" if "Tier 1" in s else "T2" if "Tier 2" in s else "deny" if s.lower().startswith("## deny") else None
            continue
        if not cur or not s or s.startswith("#"):
            continue
        for h in re.findall(r"\b[a-z0-9][a-z0-9.-]+\.[a-z]{2,}\b", s.lower()):
            tier_of.setdefault(h, cur)

def tier(h):
    for k, v in tier_of.items():
        if h == k or h.endswith("." + k):
            return v
    return "unlisted"

# --- scan digests ---
per_outlet = collections.defaultdict(lambda: collections.Counter())
days = 0
for f in sorted(glob.glob(os.path.join("digests", f"{month}-*", "news.md"))):
    days += 1
    t = open(f, encoding="utf-8").read().replace("\r\n", "\n")
    secs = re.split(r"^\s*#*\s*(第[一二三]部分)[^\n]*$", t, flags=re.M)
    for i in range(1, len(secs), 2):
        sec = {"第一部分": "S1", "第二部分": "S2", "第三部分": "S3"}[secs[i]]
        for u in re.findall(r"https?://[^\s<>（）【】，。；、\"')]+", secs[i + 1]):
            per_outlet[host(u)][sec] += 1

denied_drops = collections.Counter()
for f in glob.glob(os.path.join("digests", f"{month}-*", "filtered*.json")):
    try:
        for d in json.load(open(f, encoding="utf-8")).get("dropped_denied_source", []):
            denied_drops[d.get("_denied_host", "?")] += 1
    except Exception:
        pass

total = sum(sum(c.values()) for c in per_outlet.values())
rows = sorted(per_outlet.items(), key=lambda kv: -sum(kv[1].values()))
top3 = sum(sum(c.values()) for _, c in rows[:3])

lines = [f"# News source report — {month}", "",
         f"Days: {days} · links posted: {total} · distinct outlets: {len(rows)} · top-3 outlet share: {100 * top3 // max(total, 1)}%", "",
         "| Outlet | Tier | S1 | S2 | S3 | Total |", "|---|---|---|---|---|---|"]
for h, c in rows:
    lines.append(f"| {h} | {tier(h)} | {c['S1']} | {c['S2']} | {c['S3']} | {sum(c.values())} |")

flagged = [h for h, _ in rows if tier(h) == "deny"]
aggr = [h for h, _ in rows if h in ("news.google.com", "msn.com", "newswav.com", "flipboard.com", "news.yahoo.com")]
unlisted = [(h, sum(c.values())) for h, c in rows if tier(h) == "unlisted"]
lines += ["", "## Checks",
          f"- Denied outlets that still appeared in posted digests: {', '.join(flagged) if flagged else 'none'}",
          f"- Aggregator/redirect links posted: {', '.join(aggr) if aggr else 'none'}",
          f"- Candidates dropped by the deny list this month: {sum(denied_drops.values())}"
          + (" (" + ", ".join(f'{h} {n}' for h, n in denied_drops.most_common(10)) + ")" if denied_drops else ""),
          f"- Unlisted outlets used 3+ times (candidates for Tier 2 or Deny): "
          + (", ".join(f"{h} ({n})" for h, n in unlisted if n >= 3) or "none"),
          f"- Tier 1 share of posted links: {100 * sum(sum(c.values()) for h, c in rows if tier(h) == 'T1') // max(total, 1)}%",
          "", "## Recommendations", "(filled in by the routine on the last day of the month: outlets to add to Tier 1/2, outlets to drop, "
          "outlets to un-deny, with one-line reasons based on the numbers above and on verification failures seen during the month.)"]
os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"wrote {out}: {days} days, {total} links, {len(rows)} outlets, denied-still-posted={len(flagged)}")
