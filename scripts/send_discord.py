#!/usr/bin/env python3
"""Post a folder of Markdown message files to a Discord channel via webhook.

Stdlib only. Intended to be run by the daily research-tracker routine.

Usage:
    python3 scripts/send_discord.py --dir digests/2026-09-13/messages --dry-run
    python3 scripts/send_discord.py --dir digests/2026-09-13/messages
    python3 scripts/send_discord.py --file path/to/one_message.md

Behaviour:
  * Messages are the *.md files in --dir, posted in sorted filename order.
  * Pre-flight: every file is read and measured first. If ANY file exceeds
    Discord's 2000-character limit, nothing is sent; offenders are listed and
    the exit code is 2. Shorten those files and re-run.
  * The webhook URL is read from the environment variable named by
    --webhook-env (default DISCORD_WEBHOOK_URL). Missing -> exit 3, nothing sent.
  * Each message is POSTed with ?wait=true so Discord returns the created
    message; HTTP 429 is retried after the reported retry_after (max 5 tries);
    any other failure aborts with exit 1 and reports how many were sent.
  * allowed_mentions is set to parse nothing, so @everyone / @here in the
    digest text never ping anyone.
  * --dry-run validates and prints the plan without any network access.

Exit codes: 0 ok · 1 send failure · 2 over-length message(s) · 3 config error.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

DISCORD_LIMIT = 2000
USER_AGENT = "research-tracker-discord/1.0 (+stdlib urllib)"


def load_messages(path_dir: str | None, path_file: str | None) -> list[tuple[str, str]]:
    """Return [(label, content), ...] in posting order."""
    items: list[tuple[str, str]] = []
    if path_file:
        with open(path_file, "r", encoding="utf-8") as fh:
            items.append((os.path.basename(path_file), fh.read()))
        return items
    if not path_dir or not os.path.isdir(path_dir):
        raise SystemExit(f"[config] messages directory not found: {path_dir!r} (exit 3)")
    names = sorted(n for n in os.listdir(path_dir) if n.lower().endswith(".md"))
    for name in names:
        with open(os.path.join(path_dir, name), "r", encoding="utf-8") as fh:
            items.append((name, fh.read()))
    return items


def preflight(items: list[tuple[str, str]]) -> list[tuple[str, int]]:
    """Return list of (label, length) for messages that are empty or too long."""
    bad: list[tuple[str, int]] = []
    for label, content in items:
        n = len(content.rstrip("\n"))
        if n == 0 or n > DISCORD_LIMIT:
            bad.append((label, n))
    return bad


def post_one(webhook: str, content: str, max_tries: int = 5) -> None:
    url = webhook + ("&" if "?" in webhook else "?") + "wait=true"
    body = json.dumps(
        {"content": content.rstrip("\n"), "allowed_mentions": {"parse": []}}
    ).encode("utf-8")
    for attempt in range(1, max_tries + 1):
        req = urllib.request.Request(
            url,
            data=body,
            method="POST",
            headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                if 200 <= resp.status < 300:
                    return
                raise RuntimeError(f"unexpected HTTP {resp.status}")
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < max_tries:
                retry_after = 2.0
                try:
                    payload = json.loads(e.read().decode("utf-8", "replace"))
                    retry_after = float(payload.get("retry_after", retry_after))
                except Exception:
                    pass
                time.sleep(min(retry_after + 0.25, 30))
                continue
            detail = ""
            try:
                detail = e.read().decode("utf-8", "replace")[:300]
            except Exception:
                pass
            raise RuntimeError(f"HTTP {e.code} {e.reason} {detail}".strip()) from None
        except urllib.error.URLError as e:
            if attempt < max_tries:
                time.sleep(2.0 * attempt)
                continue
            raise RuntimeError(f"network error: {e.reason}") from None
    raise RuntimeError("gave up after repeated 429 responses")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--dir", help="directory of *.md message files, posted in sorted order")
    src.add_argument("--file", help="a single message file")
    ap.add_argument("--webhook-env", default="DISCORD_WEBHOOK_URL", help="env var holding the webhook URL")
    ap.add_argument("--dry-run", action="store_true", help="validate lengths and print the plan; no network")
    ap.add_argument("--sleep", type=float, default=1.0, help="seconds between messages (default 1.0)")
    args = ap.parse_args()

    try:
        items = load_messages(args.dir, args.file)
    except SystemExit as e:
        print(str(e), file=sys.stderr)
        return 3

    if not items:
        print("[config] no .md message files found; nothing to send (exit 3)", file=sys.stderr)
        return 3

    bad = preflight(items)
    for label, content in items:
        print(f"  {label}: {len(content.rstrip(chr(10)))} chars")
    if bad:
        print(f"\n[preflight] {len(bad)} message(s) empty or over {DISCORD_LIMIT} chars; NOTHING SENT:", file=sys.stderr)
        for label, n in bad:
            print(f"  - {label}: {n} chars", file=sys.stderr)
        return 2

    if args.dry_run:
        print(f"\n[dry-run] {len(items)} message(s) valid; would post in the order above.")
        return 0

    raw = os.environ.get(args.webhook_env, "")
    # tolerate stray quotes, whitespace, CR/LF or punctuation pasted around the value
    webhook = raw.strip().strip("\"'`<>").strip()
    webhook = re.sub(r"[^A-Za-z0-9_\-]+$", "", webhook)
    m = re.match(r"^https://(?:ptb\.|canary\.)?discord(?:app)?\.com/api/webhooks/\d+/[A-Za-z0-9_\-]+$", webhook)
    if not m:
        shape = re.sub(r"[0-9]", "9", re.sub(r"[A-Za-z]", "x", raw.strip()))[:60]
        print(f"[config] environment variable {args.webhook_env} is unset or not a Discord webhook URL "
              f"(expected https://discord.com/api/webhooks/<id>/<token>; got length {len(raw)}, masked shape '{shape}'); NOTHING SENT (exit 3)", file=sys.stderr)
        return 3

    sent = 0
    for i, (label, content) in enumerate(items, 1):
        try:
            post_one(webhook, content)
        except RuntimeError as e:
            print(f"\n[send] failed on message {i}/{len(items)} ({label}): {e}", file=sys.stderr)
            print(f"[send] sent {sent}/{len(items)} before the failure (exit 1)", file=sys.stderr)
            return 1
        sent += 1
        print(f"  sent {sent}/{len(items)}: {label}")
        if i < len(items):
            time.sleep(args.sleep)
    print(f"\n[send] done: sent {sent}/{len(items)} messages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
