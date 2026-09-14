"""Merge today's Part A results into state/papers_seen.json so later runs skip already-checked ids.

Usage: python scripts/update_papers_seen.py digests/YYYY-MM-DD TODAY [site_candidates.json] [screened.json]

papers_seen.json schema: { "<arxiv id>": {"status": "qualified" | "near-miss" | "screened-out",
                                          "first_seen": "YYYY-MM-DD", "submitted": "YYYY-MM-DD",
                                          "title": "...", "affiliation": "...", "url": "..."} }
- qualified: has a full block in a partA_raw_*.md of that day (title/affiliation/url kept so later
  digests can list it as "previously reported" while it is still inside the 30-day window)
- near-miss: listed under "# Near-misses" in a partA_raw_*.md
- screened-out: was a discovery candidate that never reached verification (no company lead or off-topic title)
Existing entries are never downgraded; a near-miss can become qualified if re-verified later.
"""
import glob, json, os, re, sys

d = sys.argv[1]
today = sys.argv[2]
cand_file = sys.argv[3] if len(sys.argv) > 3 else "site_candidates.json"
screen_file = sys.argv[4] if len(sys.argv) > 4 else "screened.json"
state_path = os.path.join("state", "papers_seen.json")
seen = json.load(open(state_path, encoding="utf-8")) if os.path.exists(state_path) else {}
RANK = {"screened-out": 0, "near-miss": 1, "qualified": 2}

def put(aid, status, **kw):
    cur = seen.get(aid)
    if cur and RANK[cur["status"]] > RANK[status]:
        return
    entry = {"status": status, "first_seen": cur["first_seen"] if cur else today}
    if cur:
        entry.update({k: v for k, v in cur.items() if k not in ("status", "first_seen")})
    entry.update({k: v for k, v in kw.items() if v})
    seen[aid] = entry

for src in (cand_file, screen_file):
    if os.path.exists(src):
        data = json.load(open(src, encoding="utf-8"))
        for c in data.get("candidates", []):
            put(c["id"], "screened-out", submitted=c.get("submitted"), title=c.get("title"))

for path in sorted(glob.glob(os.path.join(d, "partA_raw_*.md"))):
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    body, _, nm = text.partition("\n# Near-misses")
    for chunk in re.split(r"^## ", body, flags=re.M)[1:]:
        title, _, rest = chunk.partition("\n")
        m = re.search(r"\*\*arXiv:\*\* (\S+) · (\S+)", rest)
        s = re.search(r"\*\*Submitted:\*\* (\d{4}-\d{2}-\d{2})", rest)
        a = re.search(r"\*\*Qualifying affiliation\(s\):\*\* ([^\n]+)", rest)
        sm = re.search(r"\*\*Summary[^*]*\*\*\s*([^\n]+)", rest)
        summary = None
        if sm:
            # first sentence only (one-line description for the compact "previously reported" list)
            summary = re.split(r"(?<=[.!?])\s+(?=[A-Z\"“(0-9])", sm.group(1).strip())[0][:300]
        if m:
            put(m.group(1), "qualified", submitted=s.group(1) if s else None, title=title.strip(),
                affiliation=a.group(1).strip() if a else None, url=m.group(2), summary=summary)
    for l in nm.split("\n"):
        m = re.match(r"- (\d{4}\.\d{4,5})(?:v\d+)? · ([^·]+?) ·", l.strip())
        if m:
            put(m.group(1), "near-miss", title=m.group(2).strip())

os.makedirs("state", exist_ok=True)
json.dump(seen, open(state_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
counts = {}
for v in seen.values():
    counts[v["status"]] = counts.get(v["status"], 0) + 1
print(f"papers_seen.json: {len(seen)} ids {counts}")
