"""Usage: python scripts/arxiv_site_scan.py OUT.json TODAY CUTOFF
Website-fallback discovery + affiliation pre-screen for Part A (stdlib only).

1. Query arxiv.org/search for topic phrases, newest first, until dates < cutoff.
2. For each unique id, fetch arxiv.org/html/<id> (fallback: abs page only) and
   keyword-scan the first part of the document for tracked company names.
Writes site_candidates.json with all candidates and 'hits' = those with a company match.
"""
import html, json, re, sys, time, urllib.request, urllib.parse, urllib.error

OUT = sys.argv[1] if len(sys.argv) > 1 else "site_candidates.json"
TODAY = sys.argv[2] if len(sys.argv) > 2 else "2026-09-13"
CUTOFF = sys.argv[3] if len(sys.argv) > 3 else "2026-08-14"
UA = {"User-Agent": "Mozilla/5.0 (research-tracker site fallback; contact ruoyuandy@gmail.com)"}

PHRASES = [
    "world model", "world models", "world simulator", "interactive video generation",
    "action-conditioned video", "playable", "neural game engine", "game generation",
    "3D generation", "text-to-3D", "image-to-3D", "3D Gaussian splatting", "Gaussian splatting",
    "novel view synthesis", "neural rendering", "mesh generation", "3D reconstruction",
    "scene generation", "4D generation", "texture generation", "PBR material", "3D asset",
    "relighting", "feed-forward 3D",
    "character animation", "motion generation", "human motion", "motion capture", "motion retargeting",
    "physics-based character", "humanoid animation", "facial animation", "talking head", "avatar",
    "digital human", "gesture generation", "animation",
    "game engine", "Unreal Engine", "Unity", "real-time rendering", "procedural content generation",
    "video game", "game agent",
]

COMPANIES = {
    "Google": r"\bGoogle\b|DeepMind", "Microsoft": r"\bMicrosoft\b", "Meta": r"\bMeta\b(?! ?-?learn)|\bFAIR\b|Reality Labs",
    "Amazon": r"\bAmazon\b|\bAWS\b", "Apple": r"\bApple\b", "NVIDIA": r"NVIDIA|Nvidia", "Adobe": r"\bAdobe\b",
    "Intel": r"\bIntel\b(?!ligen)", "Qualcomm": r"Qualcomm", "Tencent": r"Tencent|Hunyuan", "ByteDance": r"ByteDance|Bytedance|TikTok|\bSeed\b(?! ?-?ing)",
    "miHoYo": r"miHoYo|HoYoverse|Mihoyo", "NetEase": r"NetEase|Netease|Fuxi", "Alibaba": r"Alibaba|Tongyi|DAMO|Taobao|Ant Group|AntGroup",
    "Baidu": r"\bBaidu\b", "Kuaishou": r"Kuaishou|Kling", "Sony": r"\bSony\b", "Ubisoft": r"Ubisoft", "EA": r"Electronic Arts|\bEA SEED\b|\bSEED\b.*Electronic",
    "Roblox": r"Roblox", "Unity": r"Unity Technologies", "Epic": r"Epic Games",
    "borderline": r"JD\.com|JD Explore|StepFun|MiniMax|Huawei|Samsung|Xiaomi|SenseTime|Zhipu|Moonshot|Skywork|Kunlun|\bVAST\b|Tripo|Meshy|Krafton|Nexon|Square Enix|Autodesk|\bAMD\b|Snap Inc|Snap Research|Horizon Robotics|Bosch|Toyota Research|Wayve|Waymo|OpenAI|Anthropic|Stability AI|Runway|Luma|World Labs|Decart|Odyssey|Pika|Midjourney|Shanghai AI Lab",
}

def get(url, tries=3):
    for t in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return 404, ""
            if e.code == 429:
                time.sleep(20 * (t + 1)); continue
            time.sleep(5);
        except Exception:
            time.sleep(5)
    return 0, ""

ID_RE = re.compile(r'<p class="list-title is-inline-block"><a href="https://arxiv.org/abs/([^"]+)">')
TITLE_RE = re.compile(r'<p class="title is-5 mathjax">\s*(.*?)\s*</p>', re.S)
SUB_RE = re.compile(r'<span class="has-text-black-bis has-text-weight-semibold">Submitted</span>\s*([0-9]+ [A-Za-z]+, [0-9]{4})')
MONTHS = {m: i for i, m in enumerate(["January","February","March","April","May","June","July","August","September","October","November","December"], 1)}

def iso(d):
    day, mon, yr = d.replace(",", "").split()
    return f"{yr}-{MONTHS[mon]:02d}-{int(day):02d}"

cands = {}
for ph in PHRASES:
    for start in range(0, 1000, 200):
        q = urllib.parse.quote(f'"{ph}"')  # exact phrase
        url = f"https://arxiv.org/search/?query={q}&searchtype=all&abstracts=hide&order=-announced_date_first&size=200&start={start}"
        st, body = get(url)
        time.sleep(3.5)
        if st != 200:
            print(f"WARN {ph!r} start={start} http={st}", file=sys.stderr); break
        items = body.split('<li class="arxiv-result">')[1:]
        if not items: break
        oldest = None
        for it in items:
            m = ID_RE.search(it); t = TITLE_RE.search(it); s = SUB_RE.search(it)
            if not (m and t and s): continue
            aid = m.group(1).split("v")[0]
            d = iso(s.group(1)); oldest = d
            if CUTOFF <= d <= TODAY:
                title = html.unescape(re.sub(r"<[^>]+>", "", t.group(1))).strip()
                cands.setdefault(aid, {"id": aid, "title": title, "submitted": d, "phrases": []})
                cands[aid]["phrases"].append(ph)
        print(f"{ph!r} start={start}: {len(items)} results, oldest {oldest}, total cands {len(cands)}", file=sys.stderr)
        if oldest and oldest < CUTOFF: break

print(f"== discovery done: {len(cands)} unique candidates in window ==", file=sys.stderr)
json.dump({"candidates": list(cands.values())}, open(OUT, "w"), indent=1)

# affiliation pre-screen
hits = []
for i, (aid, c) in enumerate(sorted(cands.items(), key=lambda kv: kv[1]["submitted"], reverse=True), 1):
    st, body = get(f"https://arxiv.org/html/{aid}")
    time.sleep(3.0)
    src = "html"
    if st != 200 or "ltx_authors" not in body:
        st, body = get(f"https://arxiv.org/abs/{aid}")
        time.sleep(3.0)
        src = "abs"
    text = html.unescape(re.sub(r"<[^>]+>", " ", body))
    text = re.sub(r"\s+", " ", text)
    head = text[:6000] if src == "html" else text[:4000]
    matched = {}
    for name, pat in COMPANIES.items():
        m = re.search(pat, head)
        if m:
            matched[name] = head[max(0, m.start()-60): m.end()+60]
    c["screen_source"] = src
    c["company_matches"] = matched
    if matched:
        hits.append(c)
    print(f"[{i}/{len(cands)}] {aid} {src} {'HIT '+','.join(matched) if matched else ''}", file=sys.stderr)
    if i % 10 == 0:
        json.dump({"candidates": list(cands.values()), "hits": hits}, open(OUT, "w"), indent=1)

json.dump({"candidates": list(cands.values()), "hits": hits}, open(OUT, "w"), indent=1)
print(f"== screen done: {len(hits)} hits of {len(cands)} ==", file=sys.stderr)
