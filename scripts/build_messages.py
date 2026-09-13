"""Split a digest.md into per-item Discord message files (<=2000 chars each).

Usage: python scripts/build_messages.py digests/YYYY-MM-DD/digest.md digests/YYYY-MM-DD/messages

Input format is the tracker digest: "# Part A — Papers" / "# Part B — Research → Product" headers,
each item starting with "## <title>", a bullet list of fields, then bold-labelled blocks
("**Summary (≤3 sentences):** ..."). Trailing "### Announced only" and "Near-misses:"/"Verification:"
lines are collected into the footer.

Output files (sorted order = posting order):
  00-header.md, 10-A01-<slug>.md ..., 20-B01-<slug>.md ..., 30-B-previously-reported.md (if any),
  90-footer.md (split 90a/90b/... if needed).

Condensing rule per item: try full text; if over the limit, cut every block to 2 sentences, then 1;
then shorten the author list to "First Author et al."; never cut mid-sentence. Never drops the title,
arXiv/primary URL, date or affiliation lines.
"""
import os, re, sys, shutil

LIMIT = 2000
SRC = sys.argv[1]
OUT = sys.argv[2]

text = open(SRC, encoding="utf-8").read().replace("\r\n", "\n")

def slug(s, n=40):
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return s[:n].rstrip("-") or "item"

def split_sentences(s):
    # split on sentence enders followed by space+capital/quote/digit; keep abbreviations mostly intact
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"“(0-9])", s.strip())
    return [p for p in parts if p]

def md_to_discord(s):
    # Discord has no tables/headings; convert "## " headings inside items to bold lines
    return s

# ---- parse parts ----
parts = re.split(r"^# (Part [AB][^\n]*)$", text, flags=re.M)
# parts: ['', 'Part A — Papers', body, 'Part B — ...', body]
sections = {}
for i in range(1, len(parts), 2):
    key = "A" if parts[i].startswith("Part A") else "B"
    sections[key] = (parts[i].strip(), parts[i + 1])

def parse_section(body):
    """Return (window_line, items[(title, body)], trailing_text)."""
    lines = body.strip("\n").split("\n")
    window = lines[0].strip() if lines and lines[0].startswith("Window:") else ""
    chunks = re.split(r"^## ", body, flags=re.M)
    head = chunks[0]
    items = []
    trailing = ""
    for ch in chunks[1:]:
        title, _, rest = ch.partition("\n")
        # trailing footer material lives after the last item: "### Announced only", "Near-misses:", "Verification:"
        m = re.search(r"^(### Previously reported.*|### Announced only.*|Near-misses\b.*|Verification:.*)$", rest, flags=re.M | re.S)
        if m:
            trailing += m.group(0) + "\n"
            rest = rest[: m.start()]
        items.append((title.strip(), rest.strip()))
    # footer lines may also sit in the head (empty section)
    m = re.search(r"^(### Previously reported.*|### Announced only.*|Near-misses\b.*|Verification:.*)$", head, flags=re.M | re.S)
    if m and not items:
        trailing += m.group(0) + "\n"
    return window, items, trailing

def condense(title, body, prefix):
    header_line = f"**{prefix} {title}**"
    field_lines = [l for l in body.split("\n") if l.startswith("- **")]
    block_lines = [l for l in body.split("\n") if l.startswith("**")]
    def render(max_sent, short_authors):
        fl = []
        for l in field_lines:
            if short_authors and l.startswith("- **Authors:**"):
                names = l.split("**Authors:**", 1)[1].strip().split(",")
                l = "- **Authors:** " + names[0].strip() + (" et al." if len(names) > 1 else "")
            fl.append(l)
        bl = []
        for l in block_lines:
            label, _, content = l.partition(":** ")
            label = label + ":**"
            label = re.sub(r" \(≤3 sentences\)", "", label)
            sents = split_sentences(content)
            if max_sent:
                sents = sents[:max_sent]
            bl.append(f"{label} {' '.join(sents)}")
        return "\n".join([header_line] + fl + [""] + bl).strip()
    for max_sent, short in [(None, False), (2, False), (1, False), (1, True)]:
        out = render(max_sent, short)
        if len(out) <= LIMIT:
            return out
    # last resort: drop Tools/Limitation blocks (still never mid-sentence)
    out = render(1, True)
    lines = out.split("\n")
    while len("\n".join(lines)) > LIMIT and len(lines) > 8:
        lines.pop()
    return "\n".join(lines)

def chunk_lines(lines, first_line=None):
    """Pack lines into <=LIMIT chunks without splitting a line."""
    chunks, cur = [], (first_line + "\n") if first_line else ""
    # a single line longer than the limit is split at " · " separators, never mid-sentence
    expanded = []
    for l in lines:
        while len(l) > LIMIT - 20:
            cut = l.rfind(" · ", 0, LIMIT - 20)
            if cut <= 0:
                break
            expanded.append(l[:cut])
            l = "… " + l[cut + 3:]
        expanded.append(l)
    lines = expanded
    for l in lines:
        if len(cur) + len(l) + 1 > LIMIT and cur.strip():
            chunks.append(cur.rstrip())
            cur = ""
        cur += l + "\n"
    if cur.strip():
        chunks.append(cur.rstrip())
    return chunks

os.makedirs(OUT, exist_ok=True)
for old in os.listdir(OUT):  # clear stale messages (rmtree can fail on synced folders)
    if old.lower().endswith(".md"):
        os.remove(os.path.join(OUT, old))

files = {}
winA, itemsA, trailA = parse_section(sections["A"][1]) if "A" in sections else ("", [], "")
winB, itemsB, trailB = parse_section(sections["B"][1]) if "B" in sections else ("", [], "")

# split Part B items into new vs previously reported
newB = [(t, b) for t, b in itemsB if "Previously reported" not in b]
prevB = [(t, b) for t, b in itemsB if "Previously reported" in b]

date = re.search(r"to (\d{4}-\d{2}-\d{2})\)", winA or winB)
date = date.group(1) if date else "today"

header = [f"**Research & Product Tracker — {date}**", ""]
if winA:
    header += ["**Part A — Papers.** " + winA.replace("Window: ", ""), ""]
else:
    header += ["**Part A — Papers.** No Part A in this digest.", ""]
if winB:
    header += ["**Part B — Research → Product.** " + winB.replace("Window: ", ""), ""]
header += [f"Items follow as one message each: {len(itemsA)} new papers (A01–A{len(itemsA):02d}), "
           f"{len(newB)} new products (B01–B{len(newB):02d}); previously reported papers and products are collapsed into list messages, "
           "then a footer with announced-only items and near-misses."]
files["00-header.md"] = "\n".join(header)

for i, (t, b) in enumerate(itemsA, 1):
    files[f"10-A{i:02d}-{slug(t)}.md"] = condense(t, b, f"[A{i:02d}]")
for i, (t, b) in enumerate(newB, 1):
    files[f"20-B{i:02d}-{slug(t)}.md"] = condense(t, b, f"[B{i:02d}]")
if prevB:
    lines = ["**Previously reported products (unchanged since an earlier digest)**"]
    for t, b in prevB:
        src = re.search(r"\*\*Primary source:\*\* (\S+)", b)
        comp = re.search(r"\*\*Company:\*\* ([^\n]+)", b)
        rel = re.search(r"\*\*Released:\*\* (\d{4}-\d{2}-\d{2})", b)
        lines.append(f"- {t} · {comp.group(1) if comp else ''} · {rel.group(1) if rel else ''} · {src.group(1) if src else ''}")
    for j, ch in enumerate(chunk_lines(lines)):
        files[f"30{chr(97+j)}-B-previously-reported.md"] = ch

# Part A previously reported papers → their own collapsed message(s), removed from the footer
mprev = re.search(r"^### Previously reported papers[^\n]*\n((?:- .*\n?)+)", trailA, flags=re.M)
if mprev:
    lines = ["**Previously reported papers (still in the 30-day window)**"] + [l for l in mprev.group(1).split("\n") if l.strip()]
    for j, ch in enumerate(chunk_lines(lines)):
        files[f"15{chr(97+j)}-A-previously-reported.md"] = ch
    trailA = trailA[:mprev.start()] + trailA[mprev.end():]

footer_lines = ["**Announced only, near-misses and verification**"]
for tr in (trailA, trailB):
    for l in tr.strip("\n").split("\n"):
        if l.strip():
            footer_lines.append(l.replace("### ", "**").replace("Announced only (not yet usable)", "Announced only (not yet usable)**") if l.startswith("### ") else l)
for j, ch in enumerate(chunk_lines(footer_lines)):
    files[f"90{chr(97+j)}-footer.md"] = ch

for name, content in files.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(content.rstrip() + "\n")
    print(f"{name}: {len(content.rstrip())} chars")
print(f"wrote {len(files)} messages to {OUT}")
