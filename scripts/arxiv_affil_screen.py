"""Affiliation pre-screen for arXiv candidates (stdlib only, 2 workers).

Usage: python scripts/arxiv_affil_screen.py site_candidates.json screened.json
Reads {"candidates":[{"id","title","submitted",...}]} and, for each id, fetches
https://arxiv.org/html/<id> (fallback: abs page) and regex-scans the author block
for tracked company names. Writes the same list with "screen_source" and
"company_matches" filled in, plus "hits" = candidates with any match.
This is a LEAD FILTER only; every hit must still be verified by reading the paper.
"""
import html, json, re, sys, threading, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

SRC = sys.argv[1] if len(sys.argv) > 1 else "site_candidates.json"
OUT = sys.argv[2] if len(sys.argv) > 2 else "screened.json"
WORKERS = 3
SLEEP = 1.5
UA = {"User-Agent": "Mozilla/5.0 (research-tracker affiliation screen; contact ruoyuandy@gmail.com)"}

COMPANIES = {
    "Google": r"\bGoogle\b|DeepMind", "Microsoft": r"\bMicrosoft\b", "Meta": r"\bMeta\b(?! ?-?learn)|\bFAIR\b|Reality Labs",
    "Amazon": r"\bAmazon\b|\bAWS\b", "Apple": r"\bApple\b", "NVIDIA": r"NVIDIA|Nvidia", "Adobe": r"\bAdobe\b",
    "Intel": r"\bIntel\b(?!ligen)", "Qualcomm": r"Qualcomm", "Tencent": r"Tencent|Hunyuan", "ByteDance": r"ByteDance|Bytedance|TikTok|\bSeed\b(?! ?-?ing)",
    "miHoYo": r"miHoYo|HoYoverse|Mihoyo", "NetEase": r"NetEase|Netease|Fuxi", "Alibaba": r"Alibaba|Tongyi|DAMO|Taobao|Ant Group|AntGroup",
    "Baidu": r"\bBaidu\b", "Kuaishou": r"Kuaishou|Kling", "Sony": r"\bSony\b", "Ubisoft": r"Ubisoft", "EA": r"Electronic Arts|\bEA SEED\b",
    "Roblox": r"Roblox", "Unity": r"Unity Technologies", "Epic": r"Epic Games",
    "borderline": r"JD\.com|JD Explore|StepFun|MiniMax|Huawei|Samsung|Xiaomi|SenseTime|Zhipu|Moonshot|Skywork|Kunlun|\bVAST\b|Tripo|Meshy|Krafton|Nexon|Square Enix|Autodesk|\bAMD\b|Snap Inc|Snap Research|Horizon Robotics|Bosch|Toyota Research|Wayve|Waymo|OpenAI|Anthropic|Stability AI|Runway|Luma|World Labs|Decart|Odyssey|Pika|Shanghai AI Lab|Tesla|Nokia|Disney|Pixar|Weta|Wayfair|Naver|LINE|Kakao|Baidu",
}

def get(url, tries=3):
    for t in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return 404, ""
            time.sleep(15 * (t + 1) if e.code == 429 else 5)
        except Exception:
            time.sleep(5)
    return 0, ""

lock = threading.Lock()
done = [0]

def screen(c):
    aid = c["id"]
    st, body = get(f"https://arxiv.org/html/{aid}")
    src = "html"
    if st != 200 or "ltx_authors" not in body:
        st, body = get(f"https://arxiv.org/abs/{aid}")
        src = "abs"
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", body)))
    head = text[:7000] if src == "html" else text[:4000]
    matched = {}
    for name, pat in COMPANIES.items():
        m = re.search(pat, head)
        if m:
            matched[name] = head[max(0, m.start() - 70): m.end() + 70]
    c["screen_source"] = src
    c["company_matches"] = matched
    with lock:
        done[0] += 1
        print(f"[{done[0]}] {aid} {src} {'HIT ' + ','.join(matched) if matched else ''}", file=sys.stderr, flush=True)
    time.sleep(SLEEP)
    return c

data = json.load(open(SRC, encoding="utf-8"))
cands = sorted(data["candidates"], key=lambda c: c["submitted"], reverse=True)
print(f"screening {len(cands)} candidates with {WORKERS} workers", file=sys.stderr, flush=True)
with ThreadPoolExecutor(max_workers=WORKERS) as ex:
    results = list(ex.map(screen, cands))
hits = [c for c in results if c["company_matches"]]
json.dump({"candidates": results, "hits": hits}, open(OUT, "w", encoding="utf-8"), indent=1)
print(f"== screen done: {len(hits)} hits of {len(results)} ==", file=sys.stderr, flush=True)
