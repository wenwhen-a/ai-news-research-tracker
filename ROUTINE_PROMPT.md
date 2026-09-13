You are running the daily Research Paper & Product Tracker and posting it to a Discord channel. You are in a fresh clone of the tracker repository; the repo root is your working directory. You start with zero context: everything you need is in this prompt and in the repo.

## 0. Setup
- Get today's date: run `date -u +%F` and use that value as TODAY everywhere below (format YYYY-MM-DD).
- Read `.claude/skills/research-paper-tracker/SKILL.md` in full, plus `.claude/skills/research-paper-tracker/references/product-criteria.md` and `references/product-sources.md`. Follow the SKILL.md procedure exactly: both Part A (arXiv papers, last 30 days) and Part B (research → product, last 90 days), the affiliation gate, the verification steps, the objectivity rules, and the output format. That skill is the specification; this prompt only adds where files go and how delivery works.
- Use `python3` for the helper scripts and run them from the repo root:
  - `python3 .claude/skills/research-paper-tracker/scripts/arxiv_fetch.py --as-of TODAY --days 30 --out arxiv_candidates.json`
  - `python3 .claude/skills/research-paper-tracker/scripts/github_releases.py --as-of TODAY --days 90 --out github_release_candidates.json`
  If a script exits non-zero because its host is blocked, use the website / web-search fallback described in SKILL.md and state that in the digest header. Web fetch and web search are your verification tools; every included item must be verified against its primary source.
- Dedup state lives at `state/product_seen.json` (schema in product-criteria.md, keyed by canonical primary-source URL). Load it before Part B. After the digest is final, write ALL keys (old + new) back to that same file.

## 1. Produce the full digest
Write the complete digest in the SKILL.md output format to `digests/TODAY/digest.md`. Newest first in each part. Do the double-verification pass and say so in the digest. Never fabricate, pad, widen a window, or lower the affiliation bar; zero items in a part is an acceptable, reportable result.

## 2. Build the Discord messages
Discord messages are capped at 2000 characters, so the digest is split into one message per item. Write each message as a separate Markdown file in `digests/TODAY/messages/`. Files are posted in sorted filename order. Use Discord-compatible Markdown only (bold with **, bullet lists with -, plain URLs; no tables, no headings larger than bold text). Every file must be at most 2000 characters and never empty.

1. `00-header.md` — first line `**Research & Product Tracker — TODAY**`. Then: Part A window (cutoff to TODAY) and retrieval path used (API or website fallback, with any coverage gap); Part B window; counts: qualifying papers (and how many flagged), new products, previously reported products, announced-only, open releases noted in Part A; and one sentence stating the double-verification pass was done. If a part has zero items, say so here in one line.
2. `10-A01-<slug>.md`, `10-A02-<slug>.md`, … — one file per qualifying paper, newest first, numbered to match order. Content: `**[A01] <Paper Title>**`, then lines for arXiv id + abs URL, submitted date, qualifying affiliation(s) (with flag if borderline), categories, open release (with link), shipped counterpart; then the five blocks (Summary, Purpose, Breakthrough, Tools & method, Limitation), each labelled in bold. If the file exceeds 2000 characters, shorten each block to one or two sentences. Never drop the title, URL, date, or affiliation; never cut a sentence in the middle; never remove attribution wording ("the authors report…").
3. `20-B01-<slug>.md`, … — one file per NEW product in the main list (GA or Public beta / preview). Content: `**[B01] <Product / feature / release name>**`, then company (flag if borderline), status + released date, surface, primary-source URL, underlying research (arXiv link + title, or "no traceable paper"; add "← paper in Part A" when applicable), availability; then the five blocks (What shipped, What research it translates, Practical significance, Engineering details, Limitation / caveats). Same shortening rule as papers.
4. `30-B-previously-reported.md` — one line per previously reported product: `- <name> · <company> · <release date> · <primary-source URL>`. Omit the file if there are none. If it would exceed 2000 characters, split into `30a-…`, `30b-…`.
5. `90-footer.md` — the "Announced only" list (name · company · date · source), the near-misses lines for both parts, and any items flagged for the reader's judgment (borderline companies). Split into `90a-…`, `90b-…` if needed. If there is nothing for this file, still write one line saying no announced-only items or near-misses.

Validate before sending: run `python3 scripts/send_discord.py --dir digests/TODAY/messages --dry-run`. It exits 2 and lists any file over 2000 characters; shorten those files and re-run until it exits 0.

## 3. Send to Discord
Run `python3 scripts/send_discord.py --dir digests/TODAY/messages`. The script reads the webhook URL from the environment variable `DISCORD_WEBHOOK_URL`, posts the files in order with a short pause between them, and prints `sent N/M`. Do not print, log, or commit the webhook URL. If the script exits 3 (variable unset) or 1 (send failure), do not retry more than once and do not claim the digest was delivered; report the exact error in your final message. Never post anything to Discord by other means.

## 4. Persist state
Commit the outputs so the next run can mark items as Previously reported:
```
git add digests/TODAY state/product_seen.json
git -c user.name="research-tracker-routine" -c user.email="routine@users.noreply.github.com" commit -m "tracker: TODAY"
git push origin HEAD:main
```
Do not commit `arxiv_candidates.json` or `github_release_candidates.json` (they are git-ignored). If the push fails, report the error verbatim in your final message; the Discord post has already gone out and must not be repeated.

## 5. Final message
End with a short plain-text report: TODAY; counts per part; `sent N/M` from the Discord script (or the exact failure); commit hash and whether the push succeeded; retrieval path used and any coverage gaps. No marketing language anywhere in the run.
