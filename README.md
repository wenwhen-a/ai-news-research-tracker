# AI News and Research Paper — daily tracker → Discord

A Claude Code cloud routine clones this repo every morning, produces the Simplified-Chinese games + AI news digest, runs the
`research-paper-tracker` skill (Part A: arXiv papers from tracked industry
labs, last 30 days; Part B: research that shipped as a product, last 90
days), posts one Discord message per item through a webhook, and pushes the
digest and dedup state back here.

## Layout

| Path | Purpose |
|---|---|
| `.claude/skills/game-ai-news-digest/` | The news skill (Simplified-Chinese games + AI digest: 5 in-depth, 20 brief, 10 flash items) |
| `scripts/dedup_and_filter.py` | The news skill's helper (recency window, dedup, repeat check against `state/news_previous_items.json`) |
| `scripts/build_news_messages.py` | Splits `news.md` into Discord messages: one per in-depth item, brief and flash items grouped with links |
| `state/news_previous_items.json` | News items already posted, so the flash section stays fresh |
| `.claude/skills/research-paper-tracker/` | The tracker skill (spec, arXiv + GitHub helper scripts, source lists) |
| `scripts/send_discord.py` | Posts a folder of `*.md` messages to a Discord webhook; refuses to send if any file is over 2000 chars |
| `scripts/arxiv_site_scan.py` | Website fallback for Part A discovery when the arXiv API is rate-limited (exact-phrase searches on arxiv.org) |
| `scripts/arxiv_affil_screen.py` | Fetches each candidate's arxiv.org/html page and flags tracked company names near the author block (leads only) |
| `scripts/assemble_digest.py` | Sorts verified paper blocks newest first and writes `digest.md` with Part B appended |
| `scripts/build_messages.py` | Splits `digest.md` into per-item Discord messages, each ≤2000 characters |
| `scripts/send_local.ps1` / `scripts/test_discord.ps1` | Send a messages folder / a test message from this PC (asks for the webhook URL, hidden) |
| `state/product_seen.json` | Products already reported (keyed by primary-source URL); updated by each run |
| `state/papers_seen.json` | Every arXiv id already checked (qualified / near-miss / screened-out); the screener skips these, so daily runs only verify new papers |
| `scripts/update_papers_seen.py` | Merges a day's results into `papers_seen.json` |

| `digests/YYYY-MM-DD/news.md` | Full news digest for that day (Simplified Chinese) |
| `digests/YYYY-MM-DD/digest.md` | Full research digest for that day |
| `digests/YYYY-MM-DD/messages/*.md` | The exact messages that were posted, in order (news first, then research) |
| `ROUTINE_PROMPT.md` | The prompt the cloud routine runs. Edit here, then update the routine |

Cost model: the first run verified a full 30-day backlog. Daily runs are incremental (only new arXiv ids),
Part B does a full company sweep on Mondays and a light newsroom check on other days, verification
sub-agents run on Sonnet and write straight to disk, and papers without an arXiv HTML version are
listed as unverifiable rather than parsed from PDF. The news digest is produced fresh every day.

## Schedule

Routine `daily-research-tracker-discord`, cron `0 15 * * *` UTC
(8:00 AM Pacific Daylight Time, 7:00 AM Pacific Standard Time), model
`claude-sonnet-5`. Manage it at https://claude.ai/code/routines.

## One-time setup (done by the repo owner)

1. **Discord webhook**: in Discord, open the target channel → Edit Channel →
   Integrations → Webhooks → New Webhook → Copy Webhook URL.
2. **Cloud environment variable**: on https://claude.ai/code, open Environments →
   the environment used by the routine → add `DISCORD_WEBHOOK_URL` with that URL.
   The URL is a secret; never commit it to this repo.
3. **Network access**: the same environment must be allowed to reach
   `export.arxiv.org`, `arxiv.org`, `api.github.com`, `discord.com`, and the
   company sites listed in
   `.claude/skills/research-paper-tracker/references/product-sources.md`.
   Unrestricted outbound access is simplest; a locked-down network produces
   empty digests because every item must be verified against its primary source.
4. **Repo access**: the Claude GitHub app needs read and write access to this
   repo so the routine can clone it and push `digests/` and `state/`.
5. Optional: add `GITHUB_TOKEN` to the environment to raise the GitHub API
   rate limit used by `github_releases.py` (60/h anonymous → 5000/h).

## Running or testing locally

```bash
# validate a messages folder without sending
python scripts/send_discord.py --dir digests/2026-09-13/messages --dry-run

# send for real (set the variable in your own shell first)
python scripts/send_discord.py --dir digests/2026-09-13/messages
```

Exit codes: 0 sent · 1 send failure · 2 a message is empty or over 2000 chars · 3 missing webhook variable or folder.

## Changing behaviour

- Companies, topics, sources: edit the files under
  `.claude/skills/research-paper-tracker/` (SKILL.md and `references/`).
- Message shape or delivery steps: edit `ROUTINE_PROMPT.md`, then update the
  routine's prompt (ask Claude Code to update the routine, or edit it at
  https://claude.ai/code/routines).
- Time: change the routine's cron expression (UTC).
