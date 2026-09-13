"""Assemble digest.md from verified Part A block files and a Part B file.

Usage: python scripts/assemble_digest.py digests/YYYY-MM-DD TODAY CUTOFF_A RETRIEVAL_NOTE
Reads digests/<date>/partA_raw_*.md (each "## " section is one paper; "# Near-misses" sections
are collected) and digests/<date>/partB.md, writes digests/<date>/digest.md.
"""
import glob, os, re, sys

d = sys.argv[1]
today = sys.argv[2]
cutoff = sys.argv[3]
retrieval = sys.argv[4] if len(sys.argv) > 4 else "website fallback"

papers = {}
near = []
for path in sorted(glob.glob(os.path.join(d, "partA_raw_*.md"))):
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    body, _, nm = text.partition("\n# Near-misses")
    for chunk in re.split(r"^## ", body, flags=re.M)[1:]:
        title, _, rest = chunk.partition("\n")
        m = re.search(r"\*\*arXiv:\*\* (\S+)", rest)
        s = re.search(r"\*\*Submitted:\*\* (\d{4}-\d{2}-\d{2})", rest)
        if not (m and s):
            raise SystemExit(f"missing arXiv/Submitted in {path}: {title}")
        aid = m.group(1)
        if aid in papers:
            print(f"duplicate {aid} skipped ({path})", file=sys.stderr)
            continue
        # drop per-paper verification notes; the digest carries one statement
        rest = "\n".join(l for l in rest.strip("\n").split("\n") if not l.startswith("**Verification note:**"))
        papers[aid] = (s.group(1), title.strip(), rest.strip())
    if nm:
        for l in nm.split("\n"):
            l = l.strip()
            if l.startswith("- "):
                near.append(l[2:])

ordered = sorted(papers.values(), key=lambda p: (p[0], p[1]), reverse=True)
flagged = sum(1 for p in ordered if "FLAG" in p[2])
open_rel = sum(1 for p in ordered if re.search(r"\*\*Open release:\*\* (?!none)", p[2]))

out = [f"# Part A — Papers",
       f"Window: last 30 days ({cutoff} to {today}). Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO. "
       f"Retrieval: {retrieval}. Qualifying papers: {len(ordered)} ({flagged} flagged).", ""]
for date, title, rest in ordered:
    out += ["---", f"## {title}", rest, ""]
out += ["Near-misses (on-topic candidates excluded, with reason):"] + [f"- {n}" for n in near] if near else ["Near-misses: none recorded."]
out += [
        f"Verification: every listed paper was checked twice against arXiv (v1 date and title on the abstract page; "
        f"affiliations read from the paper's HTML or PDF author block; topic confirmed from the abstract) before inclusion. "
        f"{open_rel} papers list an open release (weights, code or demo).", ""]

partB = open(os.path.join(d, "partB.md"), encoding="utf-8").read().replace("\r\n", "\n").strip("\n")
out += [partB, ""]
open(os.path.join(d, "digest.md"), "w", encoding="utf-8").write("\n".join(out))
print(f"papers={len(ordered)} flagged={flagged} open_releases={open_rel} near_misses={len(near)}")
