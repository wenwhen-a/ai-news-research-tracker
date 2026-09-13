You are running the daily Research Paper & Product Tracker and posting it to a Discord channel. You are in a fresh clone of the tracker repository; the repo root is your working directory. You start with zero context: everything you need is in this prompt and in the repo. Work economically: the run is INCREMENTAL (only papers and products not yet checked are verified) and sub-agents write their results to files, not back to you.

## 0. Setup
- TODAY = output of `date -u +%F`. CUTOFF_A = TODAY minus 30 days. CUTOFF_B = TODAY minus 90 days. WEEKDAY = output of `date -u +%u` (1 = Monday).
- Read `.claude/skills/research-paper-tracker/SKILL.md` and its `references/product-criteria.md` and `references/product-sources.md`. Follow the SKILL.md rules (affiliation gate, verification, objectivity, block format). This prompt only adds file locations, the incremental logic and delivery.
- Use `python3`, run scripts from the repo root, and create `digests/TODAY/` first. State files: `state/papers_seen.json` (every arXiv id already checked, with status) and `state/product_seen.json` (products already reported, keyed by primary-source URL).

## 1. Part A — new papers only
1. Candidates: `python3 .claude/skills/research-paper-tracker/scripts/arxiv_fetch.py --as-of TODAY --days 30 --sleep 4 --out arxiv_candidates.json`. If it exits non-zero (rate-limited), run `python3 scripts/arxiv_site_scan.py site_candidates.json TODAY CUTOFF_A` and stop it after its "discovery done" line (the JSON is written at that point).
2. Screen: `python3 scripts/arxiv_affil_screen.py <candidates file> screened.json`. It automatically skips every id already in `state/papers_seen.json`, so on a normal day only the last day or two of new ids are fetched. Its "hits" are LEADS ONLY: keep ids whose first four digits fall in the window months, drop obviously off-topic titles (medical, physics, NLP, recommender systems, GUI agents), and remember that "Google" on abstract-only pages usually comes from the "Google Scholar" link and "Meta" often matches "meta-learning".
3. Verify the remaining leads (typically 3 to 15 per day). For batches larger than 8, spawn Sonnet sub-agents, at most 15 papers each. Each agent fetches `https://arxiv.org/abs/<id>` (v1 date, title, authors, categories, withdrawal) and `https://arxiv.org/html/<id>` (affiliations under the author names). No PDF fallback: if there is no HTML version, record the paper as a near-miss "affiliation unverifiable". Apply the SKILL.md gate; purely academic papers become near-misses; comparable labs not on the list are kept with "FLAG: borderline". Confirm the topic from the abstract.
4. Each agent WRITES its results to `digests/TODAY/partA_raw_<batch>.md` (paper blocks in the SKILL.md Part A format, then a `# Near-misses` section of `- <id> · <title> · <reason>` lines) and returns only a three-line summary (counts, file path, problems). If you verify papers yourself, write the same file. Blocks must contain concrete content from the paper (problem, method, reported numbers, datasets and hardware, stated limitations), no placeholders.
5. `python3 scripts/update_papers_seen.py digests/TODAY TODAY <candidates file> screened.json` records every checked id so tomorrow skips them. Papers reported on earlier days that are still inside the window are listed automatically by the assembler as one-line "previously reported" entries.

## 2. Part B — weekly sweep, daily light check
- If WEEKDAY is 1 (Monday): full sweep. Run `python3 .claude/skills/research-paper-tracker/scripts/github_releases.py --as-of TODAY --days 90 --out github_release_candidates.json` (leads only), then walk `references/product-sources.md` company by company with web search and primary-page fetches. Use at most three Sonnet sub-agents (Western big tech and publishers; NVIDIA/Adobe/engines; Chinese tech), each capped at about 40 web calls and each writing its findings to `digests/TODAY/partB_raw_<group>.md`.
- Any other day: light check only. Fetch or search about ten primary surfaces (NVIDIA developer blog and GeForce news, Unreal Engine news and forum announcements, Unity news, Roblox newsroom, Adobe blog, Tencent Hunyuan, ByteDance Volcano Engine and Seed, Alibaba Model Studio release notes, Kuaishou Kling release notes, PlayStation Blog) for items dated in the last 7 days on the four topics. Verify any hit on its primary page. Do not re-verify items already in `state/product_seen.json`.
- Write `digests/TODAY/partB.md` in the SKILL.md Part B format: the `# Part B — Research → Product` heading and `Window:` line; full five-block items only for NEW products; every product already in `state/product_seen.json` and still inside the 90-day window as a one-line item whose Status line contains "Previously reported" (title, company, released date, primary source); then `### Announced only (not yet usable)`, a `Near-misses:` line and a `Verification:` line. Update `state/product_seen.json` with all keys (schema in `product-criteria.md`).

## 3. Assemble, split, check
- `python3 scripts/assemble_digest.py digests/TODAY TODAY CUTOFF_A "<retrieval note: API or website fallback, coverage gaps>"` writes `digests/TODAY/digest.md` (new papers newest first, previously reported papers as one line each, counts filled in, Part B appended).
- `python3 scripts/build_messages.py digests/TODAY/digest.md digests/TODAY/messages` produces one Discord message per new item plus collapsed list messages and a footer, each at most 2000 characters.
- `python3 scripts/send_discord.py --dir digests/TODAY/messages --dry-run` must exit 0; if it exits 2, shorten the named files by hand (never mid-sentence, never dropping title, URL, date or affiliation) and re-run.

## 4. Send to Discord
`python3 scripts/send_discord.py --dir digests/TODAY/messages`. It reads the webhook from the environment variable `DISCORD_WEBHOOK_URL` and prints `sent N/M`. Never print, log or commit the webhook URL. On exit 3 (variable unset) or 1 (send failure), retry at most once, do not claim delivery, and report the exact error. Never post to Discord by any other means. A day with zero new papers and zero new products still posts the header and footer, which say so plainly.

## 5. Persist state
```
git add digests/TODAY state/papers_seen.json state/product_seen.json
git -c user.name="research-tracker-routine" -c user.email="routine@users.noreply.github.com" commit -m "tracker: TODAY"
git push origin HEAD:main
```
Do not commit candidate JSON files or logs (git-ignored). If the push fails, report the error verbatim; the Discord post has already gone out and must not be repeated.

## 6. Final message
A short plain-text report: TODAY; counts (new papers, previously reported, flagged, products new and previously reported, announced-only, near-misses); `sent N/M` or the exact failure; commit hash and push result; retrieval path used and any coverage gap. Never fabricate, pad, widen a window or lower the affiliation bar. No marketing language anywhere.
