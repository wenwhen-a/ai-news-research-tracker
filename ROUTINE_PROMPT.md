You are running the daily Research Paper & Product Tracker and posting it to a Discord channel. You are in a fresh clone of the tracker repository; the repo root is your working directory. You start with zero context: everything you need is in this prompt and in the repo.

## 0. Setup
- Get today's date: run `date -u +%F` and use that value as TODAY everywhere below (format YYYY-MM-DD). CUTOFF_A = TODAY minus 30 days; CUTOFF_B = TODAY minus 90 days.
- Read `.claude/skills/research-paper-tracker/SKILL.md` in full, plus `references/product-criteria.md` and `references/product-sources.md` in the same skill folder. Follow the SKILL.md procedure exactly: both Part A (arXiv papers) and Part B (research → product), the affiliation gate, verification steps, objectivity rules and output format. That skill is the specification; this prompt only adds where files go and how delivery works.
- Use `python3` for scripts and run them from the repo root. Create `digests/TODAY/` first.

## 1. Part A candidates
- Try the API first: `python3 .claude/skills/research-paper-tracker/scripts/arxiv_fetch.py --as-of TODAY --days 30 --sleep 4 --out arxiv_candidates.json`.
- If it exits non-zero (HTTP 429 or blocked), use the website fallback that lives in this repo:
  1. `python3 scripts/arxiv_site_scan.py site_candidates.json TODAY CUTOFF_A` (exact-phrase searches on arxiv.org; runs 15 to 25 minutes; only its discovery phase is needed, so you may stop it after the "discovery done" line and the JSON is written, since step 2 does the screen faster).
  2. `python3 scripts/arxiv_affil_screen.py site_candidates.json screened.json` (fetches arxiv.org/html for each candidate and regex-matches tracked company names near the author block; 3 workers; 30 to 45 minutes for about 900 candidates).
  3. Treat `screened.json` "hits" as LEADS ONLY. Keep only ids whose first four digits match the window months (the arXiv id encodes the v1 month, e.g. 2608/2609 for an Aug 14 to Sep 13 window), drop titles that are obviously off-topic (medical, physics, NLP, recommender systems, GUI agents), and note that "Google" matches on abs-only pages usually come from the "Google Scholar" link and "Meta" often matches "meta-learning".
- Verify every remaining lead by fetching `https://arxiv.org/abs/<id>` (v1 date from the submission history, title, authors, categories, withdrawal) and `https://arxiv.org/html/<id>` (or `/pdf/<id>`) to read the real affiliations. Apply the SKILL.md gate: at least one author at a tracked company, or a comparable lab flagged "FLAG: borderline"; purely academic papers go to near-misses. Confirm the topic from the abstract. Write each qualifying paper as a block in the SKILL.md Part A format into one or more files named `digests/TODAY/partA_raw_<batch>.md`, each file ending with a `# Near-misses` section of `- <id> · <title> · <reason>` lines. You may use sub-agents for batches of 15 to 20 papers each; every block must contain concrete content from the paper (problem, method, reported numbers, datasets/hardware, stated limitations) and no placeholders.

## 2. Part B
- Run `python3 .claude/skills/research-paper-tracker/scripts/github_releases.py --as-of TODAY --days 90 --out github_release_candidates.json` (leads only; set GITHUB_TOKEN if available).
- Walk `references/product-sources.md` company by company with web search and fetch of primary pages (newsrooms, release notes, model catalogs, app-store notes). Load `state/product_seen.json` first; anything whose primary-source URL is already a key is "Previously reported". Verify every item on its primary page, then write `digests/TODAY/partB.md` in the SKILL.md Part B format, starting with the `# Part B — Research → Product` heading and its `Window:` line, items newest first, then the `### Announced only (not yet usable)` list, a `Near-misses:` line and a `Verification:` line.
- Update `state/product_seen.json` with all keys (old + new) using the schema in `product-criteria.md`.

## 3. Assemble and split
- `python3 scripts/assemble_digest.py digests/TODAY TODAY CUTOFF_A "<retrieval note: API or website fallback, with any coverage gap>"` writes `digests/TODAY/digest.md` (papers sorted newest first, counts filled in, Part B appended).
- `python3 scripts/build_messages.py digests/TODAY/digest.md digests/TODAY/messages` splits it into one Discord message per item (header, one file per paper, one per new product, a collapsed previously-reported list, footer), each at most 2000 characters, trimming blocks sentence by sentence when needed.
- `python3 scripts/send_discord.py --dir digests/TODAY/messages --dry-run` must exit 0. If it exits 2, shorten the named files by hand (never mid-sentence, never dropping title, URL, date or affiliation) and re-run.

## 4. Send to Discord
Run `python3 scripts/send_discord.py --dir digests/TODAY/messages`. It reads the webhook URL from the environment variable `DISCORD_WEBHOOK_URL`, posts the files in order with a short pause, and prints `sent N/M`. Never print, log or commit the webhook URL. If it exits 3 (variable unset) or 1 (send failure), do not retry more than once and do not claim delivery; report the exact error in your final message. Never post to Discord by any other means.

## 5. Persist state
```
git add digests/TODAY state/product_seen.json
git -c user.name="research-tracker-routine" -c user.email="routine@users.noreply.github.com" commit -m "tracker: TODAY"
git push origin HEAD:main
```
Do not commit `*_candidates.json`, `site_candidates.json`, `screened.json` or logs (they are git-ignored). If the push fails, report the error verbatim; the Discord post has already gone out and must not be repeated.

## 6. Final message
A short plain-text report: TODAY; counts (papers, flagged, products new/previously reported, announced-only, near-misses); `sent N/M` from the Discord script or the exact failure; commit hash and push result; retrieval path used and any coverage gap. Never fabricate, pad, widen a window or lower the affiliation bar; zero items in a part is an acceptable, reportable result. No marketing language anywhere.
