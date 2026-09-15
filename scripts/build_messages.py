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
import json, os, re, sys, shutil

LIMIT = 1960  # headroom below Discord's 2000-char cap to absorb <url> wrapping below
EMBED_FIELDS = 25       # Discord: max fields per embed
EMBED_CHARS = 5500      # keep under Discord's 6000-char total per message

URL_RE = re.compile(r"<?(https?://[^\s<>]+)>?")

def wrap_urls(text):
    """Wrap bare URLs in <...> so Discord doesn't auto-unfurl a link preview for them.
    Applied only to final .md message text, never to .json embed payloads or to text used
    for URL-keyed lookups (e.g. product_state[url]) earlier in the pipeline."""
    return URL_RE.sub(lambda m: f"<{m.group(1)}>", text)


def companies_of(affil):
    """'NVIDIA — A, B; Microsoft — C; FLAG: borderline' -> 'NVIDIA; Microsoft (flag)'."""
    names, flag = [], False
    for part in re.split(r";\s*", affil or ""):
        part = part.strip()
        if not part:
            continue
        if part.upper().startswith("FLAG"):
            flag = True
            continue
        name = re.split(r"\s+—\s+|\s+-\s+", part, 1)[0].strip()
        name = re.sub(r"\s*\(.*?\)\s*$", "", name)
        if name and name not in names:
            names.append(name)
    return "; ".join(names) + (" (flag)" if flag else "")


def embed_files(prefix, title, rows):
    """rows = [(name, value)] -> {filename: json payload} split by field count and char budget. No links."""
    out, batch, used, j = {}, [], len(title), 0
    def flush():
        nonlocal batch, used, j
        if batch:
            out[f"{prefix}{chr(97 + j)}-previously-reported.json"] = json.dumps(
                {"embeds": [{"title": title, "fields": [{"name": n, "value": v, "inline": False} for n, v in batch]}]},
                ensure_ascii=False)
            j += 1
        batch, used = [], len(title)
    for name, value in rows:
        name = (name or "untitled")[:250]
        value = (value or "—")[:1000]
        if len(batch) >= EMBED_FIELDS or used + len(name) + len(value) > EMBED_CHARS:
            flush()
        batch.append((name, value)); used += len(name) + len(value)
    flush()
    return out
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
for old in os.listdir(OUT):  # clear stale research messages only (news files are managed by build_news_messages.py)
    if old.lower().endswith((".md", ".json")) and not old.startswith(("10-news", "20-news", "30-news", "35-news")) and old != "00-header.md":
        os.remove(os.path.join(OUT, old))

product_state = {}
try:
    product_state = json.load(open(os.path.join("state", "product_seen.json"), encoding="utf-8"))
except Exception:
    pass

files = {}
winA, itemsA, trailA = parse_section(sections["A"][1]) if "A" in sections else ("", [], "")
winB, itemsB, trailB = parse_section(sections["B"][1]) if "B" in sections else ("", [], "")

# split Part B items into new vs previously reported
newB = [(t, b) for t, b in itemsB if "Previously reported" not in b]
prevB = [(t, b) for t, b in itemsB if "Previously reported" in b]

date = re.search(r"to (\d{4}-\d{2}-\d{2})\)", winA or winB)
date = date.group(1) if date else "today"

def short_window(w):
    # keep "last N days (from to). ... Qualifying ...: counts" but drop the long retrieval sentence
    w = w.replace("Window: ", "")
    w = re.sub(r"\s*Retrieval:.*?(?=Qualifying|$)", " ", w).strip()
    return re.sub(r"\s{2,}", " ", w)

header = [f"**Research & Product Tracker — {date}**", ""]
# a combined daily banner is written only when the news builder has not already written one
if not os.path.exists(os.path.join(OUT, "00-header.md")):
    files["00-header.md"] = f"**每日简报 — {date}**\n今日无新闻部分；以下为研究与产品追踪（Research & Product Tracker）。"
if winA:
    header += ["**Part A — Papers.** " + short_window(winA), ""]
else:
    header += ["**Part A — Papers.** No Part A in this digest.", ""]
if winB:
    header += ["**Part B — Research → Product.** " + short_window(winB), ""]
header += [f"One message per new item: {len(itemsA)} new papers (A01–A{len(itemsA):02d}), "
           f"{len(newB)} new products (B01–B{len(newB):02d}). Previously reported items follow as compact cards "
           "(title · companies · one line); near-miss details are kept in the repository digest."]
files["50-research-header.md"] = "\n".join(header)

for i, (t, b) in enumerate(itemsA, 1):
    files[f"60-A{i:02d}-{slug(t)}.md"] = condense(t, b, f"[A{i:02d}]")
for i, (t, b) in enumerate(newB, 1):
    files[f"70-B{i:02d}-{slug(t)}.md"] = condense(t, b, f"[B{i:02d}]")
if prevB:
    rows = []
    for t, b in prevB:
        src = re.search(r"\*\*Primary source:\*\* (\S+)", b)
        comp = re.search(r"\*\*Company:\*\* ([^\n]+)", b)
        comp = re.sub(r"\s*—\s*FLAG.*$", " (flag)", comp.group(1).strip()) if comp else ""
        summ = ""
        if src and src.group(1) in product_state:
            summ = product_state[src.group(1)].get("summary", "")
        if not summ:
            ws = re.search(r"\*\*What shipped[^*]*\*\*\s*([^\n]+)", b)
            summ = ws.group(1).strip() if ws else ""
        rows.append((t, f"{comp} — {summ}".strip(" —")))
    files.update(embed_files("75", "Previously reported products (still in the 90-day window)", rows))

# Part B may also list previously reported products as a "### Previously reported" block of
# "- name · company · tier · Released date · url" lines (the routine's compact form)
mprevB = re.search(r"^### Previously reported[^\n]*\n((?:- .*\n?)+)", trailB, flags=re.M)
if mprevB:
    rows = []
    for l in mprevB.group(1).split("\n"):
        if not l.strip():
            continue
        parts = [p.strip() for p in l[2:].split(" · ")]
        name = parts[0]
        comp = parts[1] if len(parts) > 1 else ""
        url = next((p for p in parts if p.startswith("http")), "")
        summ = product_state.get(url, {}).get("summary", "") if url else ""
        rows.append((name, f"{comp} — {summ}".strip(" —")))
    files.update(embed_files("75", "Previously reported products (still in the 90-day window)", rows))
    trailB = trailB[:mprevB.start()] + trailB[mprevB.end():]

# Part A previously reported papers → compact embed cards (title · companies · one line), no links
mprev = re.search(r"^### Previously reported papers[^\n]*\n((?:- .*\n?)+)", trailA, flags=re.M)
if mprev:
    rows = []
    for l in mprev.group(1).split("\n"):
        if not l.strip():
            continue
        parts = l[2:].split(" · ")
        # digest line: title · affiliation · date · summary · url  (summary may itself contain " · ")
        if len(parts) >= 5:
            title, affil, summary = parts[0], parts[1], " · ".join(parts[3:-1])
        elif len(parts) == 4:
            title, affil, summary = parts[0], parts[1], ""
        else:
            title, affil, summary = parts[0], "", ""
        rows.append((title, f"{companies_of(affil)} — {summary}".strip(" —")))
    files.update(embed_files("65", "Previously reported papers (still in the 30-day window)", rows))
    trailA = trailA[:mprev.start()] + trailA[mprev.end():]

# Footer: announced-only items only, plus a one-line count of near-misses (details stay in the repo digest)
footer_lines = []
near_counts = []
for label, tr in (("papers", trailA), ("products", trailB)):
    lines = [l for l in tr.strip("\n").split("\n") if l.strip()]
    ann = False
    for l in lines:
        if l.startswith("### Announced only"):
            ann = True
            footer_lines.append("**Announced only (not yet usable)**")
            continue
        if l.startswith(("Near-misses", "Verification:")) or l.startswith("### "):
            ann = False
        if ann and l.startswith("- "):
            footer_lines.append(l)
    if label == "papers":
        n_near = len([l for l in lines if l.startswith("- ") and not any(l == f for f in footer_lines)])
        if n_near:
            near_counts.append(f"{n_near} paper near-misses")
    elif any(l.startswith("Near-misses") for l in lines):
        near_counts.append("product near-misses")
if near_counts:
    footer_lines.append("Excluded on review: " + " and ".join(near_counts) + " — details in the repository digest, not posted here.")
if footer_lines:
    for j, ch in enumerate(chunk_lines(footer_lines)):
        files[f"90{chr(97+j)}-footer.md"] = ch

for name, content in files.items():
    content = content.rstrip()
    if name.lower().endswith(".md"):
        content = wrap_urls(content)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(content + "\n")
    print(f"{name}: {len(content)} chars")
print(f"wrote {len(files)} messages to {OUT}")
