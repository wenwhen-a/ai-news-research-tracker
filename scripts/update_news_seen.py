"""Record today's published news items in state/news_previous_items.json (deterministic; run right after news.md is written).

Usage: python scripts/update_news_seen.py digests/YYYY-MM-DD/news.md TODAY [--keep-days 14]

Parses the three sections of news.md (第一部分 / 第二部分 / 第三部分). For Sections 1 and 2 an item is a
title line (plain or bold, optionally "## ") followed by "* 日期：" / "* 来源链接：" bullets; for Section 3 an
item is one "* [标题]（日期）— 概述 URL" line. Appends {title, url, date, section, posted} for each item,
de-duplicates by URL, and drops entries posted more than --keep-days ago.
"""
import json, os, re, sys
from datetime import date, timedelta

src, today = sys.argv[1], sys.argv[2]
keep = int(sys.argv[sys.argv.index("--keep-days") + 1]) if "--keep-days" in sys.argv else 14
state_path = os.path.join("state", "news_previous_items.json")
prev = json.load(open(state_path, encoding="utf-8")) if os.path.exists(state_path) else []

text = open(src, encoding="utf-8").read().replace("\r\n", "\n")
secs = re.split(r"^\s*#*\s*(第[一二三]部分)[^\n]*$", text, flags=re.M)
found = []
URL = re.compile(r"https?://[^\s<>）)]+")

def clean_title(s):
    s = re.sub(r"^\s*#+\s*", "", s).replace("**", "").strip()
    return s.strip("[]【】").strip()

for i in range(1, len(secs), 2):
    sec, body = secs[i], secs[i + 1]
    lines = [l.rstrip() for l in body.split("\n") if l.strip()]
    if sec == "第三部分":
        for l in lines:
            if not re.match(r"^\s*[*-]\s", l):
                continue
            m = URL.search(l)
            t = re.sub(r"^\s*[*-]\s*", "", l).replace("**", "")
            t = re.split(r"[（(]\s*\d{4}-\d{2}-\d{2}", t)[0].strip().strip("[]【】")
            d = re.search(r"(\d{4}-\d{2}-\d{2})", l)
            if m and t:
                found.append({"title": t, "url": m.group(0), "date": d.group(1) if d else today, "section": 3, "posted": today})
        continue
    n = len(lines)
    for j, l in enumerate(lines):
        is_bullet = re.match(r"^\s*[*-]\s", l) and not l.lstrip().startswith("**")
        if is_bullet or l.lstrip().startswith("#") and not l.lstrip().startswith("## "):
            continue
        nxt = " ".join(lines[j + 1:j + 4])
        if "日期" in nxt and "来源链接" in nxt:
            d = re.search(r"日期[^\d]*(\d{4}-\d{2}-\d{2})", nxt)
            u = re.search(r"来源链接[^h]*(https?://[^\s<>）)]+)", nxt)
            if u:
                found.append({"title": clean_title(l), "url": u.group(1), "date": d.group(1) if d else today,
                              "section": 1 if sec == "第一部分" else 2, "posted": today})

cutoff = (date.fromisoformat(today) - timedelta(days=keep)).isoformat()
merged = {}
for p in prev:
    if p.get("posted", p.get("date", today)) >= cutoff:
        merged[p["url"].rstrip("/").lower()] = p
for f in found:
    merged.setdefault(f["url"].rstrip("/").lower(), f)
json.dump(list(merged.values()), open(state_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"news_previous_items.json: +{len(found)} parsed today, {len(merged)} kept (last {keep} days)")
