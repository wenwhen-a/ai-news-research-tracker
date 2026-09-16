"""Split the Simplified-Chinese news digest (news.md) into Discord message files (<=2000 chars).

Usage: python scripts/build_news_messages.py digests/YYYY-MM-DD/news.md digests/YYYY-MM-DD/messages [TODAY]

Input: the game-ai-news-digest output format:
  第一部分 ... (in-depth items: title line, then "* 日期：", "* 来源链接：", "* 核心事实", "* 背景与起因", "* 结果与进展" bullets)
  第二部分 ... (brief items: title line, then "* 日期：", "* 来源链接：", "* 概要：")
  第三部分 ... (flash items: one "* [title]（date）— summary URL" line each)

Output (posting order; research messages use 50+ prefixes so news comes first):
  00-header.md            overall banner for the day (written only if absent)
  10-news-S1-NN-<slug>.md one message per in-depth item (bullets trimmed from the end if over the limit)
  20-news-S2-a.md ...     several brief items per message, each with its link
  30-news-S3-a.md ...     several flash items per message, each with its link
  35-news-note.md         shortfall / notes lines from the digest, if any
Never splits mid-sentence; a section whose items cannot be parsed is chunked line by line instead, so no content is lost.
"""
import os, re, sys

LIMIT = 1960  # headroom below Discord's 2000-char cap to absorb <url> wrapping below
SRC, OUT = sys.argv[1], sys.argv[2]
TODAY = sys.argv[3] if len(sys.argv) > 3 else ""
os.makedirs(OUT, exist_ok=True)

URL_RE = re.compile(r"<?(https?://[^\s<>]+)>?")

def wrap_urls(text):
    """Wrap bare URLs in <...> so Discord doesn't auto-unfurl a link preview for them."""
    return URL_RE.sub(lambda m: f"<{m.group(1)}>", text)
for old in os.listdir(OUT):
    if old.startswith(("10-news", "20-news", "30-news", "35-news")):
        os.remove(os.path.join(OUT, old))

text = open(SRC, encoding="utf-8").read().replace("\r\n", "\n")

def slug(s, n=30):
    s = re.sub(r"[^A-Za-z0-9一-鿿]+", "-", s).strip("-")
    return s[:n].strip("-") or "item"

def bullet(l):
    return l.lstrip().startswith(("* ", "- ", "• "))

# ---- split sections on 第一/二/三部分 headings ----
sec_re = re.compile(r"^\s*#*\s*(第[一二三]部分)[^\n]*$", re.M)
marks = list(sec_re.finditer(text))
sections = {}
for i, m in enumerate(marks):
    end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
    sections[m.group(1)] = (m.group(0).strip().lstrip("#").strip(), text[m.end():end])

def parse_items(body):
    """Items = a non-bullet, non-empty line followed by bullet lines. Returns [(title, [lines])]."""
    items, cur = [], None
    for l in body.split("\n"):
        s = l.rstrip()
        if not s.strip():
            continue
        if s.lstrip().startswith("#"):
            # "## Title" / "### Title" lines are item titles (the section heading itself was split off earlier)
            if re.match(r"^\s*#{1,4}\s+\S", s):
                if cur:
                    items.append(cur)
                cur = [re.sub(r"^\s*#+\s*", "", s).replace("**", "").strip().strip("[]【】"), []]
            continue
        if not bullet(s) and not s.startswith(" "):
            if cur:
                items.append(cur)
            cur = [s.strip().replace("**", "").strip("[]【】"), []]
        elif cur:
            indent = len(s) - len(s.lstrip())
            body_line = re.sub(r"^\s*[*•-]\s+", "", s)
            cur[1].append(("  - " if indent >= 2 else "- ") + body_line if bullet(s) else s.strip())
    if cur:
        items.append(cur)
    # drop "items" that never got bullets (stray prose) but keep their text as notes
    notes = [t for t, ls in items if not ls and not t.startswith(("本部分覆盖", "为每条新闻重复"))]
    return [(t, ls) for t, ls in items if ls], notes

def chunk(lines, first=None):
    chunks, cur = [], (first + "\n") if first else ""
    for l in lines:
        if len(cur) + len(l) + 1 > LIMIT and cur.strip():
            chunks.append(cur.rstrip()); cur = ""
        cur += l + "\n"
    if cur.strip():
        chunks.append(cur.rstrip())
    return chunks

def trim_to_limit(head, lines):
    """Drop trailing sub-bullets (from the longest group first) until the message fits."""
    out = head + "\n" + "\n".join(lines)
    while len(out) > LIMIT:
        # candidate: last sub-bullet ("   * ...") that is not the only one under its parent
        idx = None
        for i in range(len(lines) - 1, 0, -1):
            # drop a nested fact bullet only if its parent keeps at least one other nested bullet
            if lines[i].startswith("  - ") and i > 0 and lines[i - 1].startswith("  - "):
                idx = i; break
        if idx is None:
            break
        lines.pop(idx)
        out = head + "\n" + "\n".join(lines)
    if len(out) > LIMIT:
        out = out[:LIMIT - 2].rsplit("\n", 1)[0] + "\n…"
    return out

files = {}
counts = {}

# Section 1: one message per item
if "第一部分" in sections:
    title, body = sections["第一部分"]
    items, notes = parse_items(body)
    counts["S1"] = len(items)
    for n, (t, ls) in enumerate(items, 1):
        head = f"**[新闻 {n}] {t.replace('**', '').strip()}**"
        files[f"10-news-S1-{n:02d}-{slug(t)}.md"] = trim_to_limit(head, list(ls))
    if not items and body.strip():
        for j, ch in enumerate(chunk([l for l in body.split("\n") if l.strip()], f"**{title}**")):
            files[f"10-news-S1-raw-{chr(97+j)}.md"] = ch
    notes_all = notes
else:
    notes_all = []

# Section 2: grouped brief items with links
if "第二部分" in sections:
    title, body = sections["第二部分"]
    items, notes = parse_items(body)
    counts["S2"] = len(items)
    blocks = []
    def field(ls, label):
        for l in ls:
            clean = re.sub(r"^\s*[-*•]\s*", "", l).replace("**", "").strip()
            m = re.match(rf"{label}[^：:]*[：:]\s*(.*)$", clean)
            if m:
                return m.group(1).strip()
        return ""
    for n, (t, ls) in enumerate(items, 1):
        date, link, summ = field(ls, "日期"), field(ls, "来源链接"), field(ls, "概要")
        t = t.replace("**", "").strip()
        blocks.append(f"**{n}. {t}**（{date}）\n{summ}\n{link}".strip())
    if blocks:
        for j, ch in enumerate(chunk(blocks, f"**{title}**")):
            files[f"20-news-S2-{chr(97+j)}.md"] = ch.replace("\n**", "\n\n**")
    elif body.strip():
        for j, ch in enumerate(chunk([l for l in body.split("\n") if l.strip()], f"**{title}**")):
            files[f"20-news-S2-raw-{chr(97+j)}.md"] = ch
    notes_all += notes

# Section 3: flash lines, grouped
if "第三部分" in sections:
    title, body = sections["第三部分"]
    lines = [re.sub(r"^\s*[*-]\s+", "- ", l.rstrip()) for l in body.split("\n") if l.strip() and not l.lstrip().startswith("#")]
    flash = [l for l in lines if l.startswith("- ")]
    counts["S3"] = len(flash)
    prose = [l for l in lines if not l.startswith("- ") and not l.startswith("本部分覆盖")]
    for j, ch in enumerate(chunk(flash if flash else prose, f"**{title}**")):
        files[f"30-news-S3-{chr(97+j)}.md"] = ch
    if flash:
        notes_all += prose

if notes_all:
    for j, ch in enumerate(chunk([f"- {n}" for n in notes_all], "**新闻备注**")):
        files[f"35-news-note-{chr(97+j)}.md"] = ch

# overall banner (only if the research builder has not written one)
banner = os.path.join(OUT, "00-header.md")
if not os.path.exists(banner):
    files["00-header.md"] = (f"**每日简报 — {TODAY or 'today'}**\n"
                             f"新闻：深度 {counts.get('S1', 0)} 条 · 综合简讯 {counts.get('S2', 0)} 条 · 24 小时快讯 {counts.get('S3', 0)} 条。"
                             f"随后为研究与产品追踪（Research & Product Tracker）。")

for name, content in files.items():
    content = wrap_urls(content.rstrip())
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(content + "\n")
    print(f"{name}: {len(content)} chars")
print(f"news messages: {len(files)}  counts={counts}")
