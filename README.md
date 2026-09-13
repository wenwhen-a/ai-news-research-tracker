# AI News and Research Paper — daily tracker → Discord

A Claude Code cloud routine clones this repo every morning, runs the
`research-paper-tracker` skill (Part A: arXiv papers from tracked industry
labs, last 30 days; Part B: research that shipped as a product, last 90
days), posts one Discord message per item through a webhook, and pushes the
digest and dedup state back here.

## Layout

| Path | Purpose |
|---|---|
| `.claude/skills/research-paper-tracker/` | The tracker skill (spec, arXiv + GitHub helper scripts, source lists) |
| `scripts/send_discord.py` | Posts a folder of `*.md` messages to a Discord webhook; refuses to send if any file is over 2000 chars |
| `state/product_seen.json` | Products already reported (keyed by primary-source URL); updated by each run |
| `digests/YYYY-MM-DD/digest.md` | Full digest for that day |
| `digests/YYYY-MM-DD/messages/*.md` | The exact messages that were posted, in order |
| `ROUTINE_PROMPT.md` | The prompt the cloud routine runs. Edit here, then update the routine |

## Schedule

Routine `daily-research-tracker-discord`, cron `0 15 * * *` UTC
(8:00 AM Pacific Daylight Time, 7:00 AM Pacific Standard Time), model
`claude-opus-5`. Manage it at https://claude.ai/code/routines.

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
