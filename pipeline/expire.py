#!/usr/bin/env python3
"""Auto-archive stale items.

A public daily channel must not let its front page grow without bound, and
there is no human operator marking items done. Learn items age out fastest
(they are reading material); Act/Plan items stay visible longer but also
archive eventually — the archive taxonomy keeps everything reachable.

Defaults: Learn after 14 days (LEARN_EXPIRE_DAYS), everything else after
30 days (EXPIRE_DAYS).

Usage:
    python pipeline/expire.py [--dry-run]
"""

import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content" / "insights"


def main() -> int:
    default_days = int(os.environ.get("EXPIRE_DAYS", "30"))
    learn_days = int(os.environ.get("LEARN_EXPIRE_DAYS", "14"))
    dry_run = "--dry-run" in sys.argv
    now = datetime.now(timezone.utc)

    archived = []
    for path in sorted(CONTENT_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not re.search(r'^status: "active"$', text, re.M):
            continue
        m = re.search(r"^date: (.+)$", text, re.M)
        if not m:
            continue
        try:
            posted = datetime.fromisoformat(m.group(1).strip())
        except ValueError:
            continue
        if posted.tzinfo is None:
            posted = posted.replace(tzinfo=timezone.utc)
        is_learn = re.search(r'^verdict: "Learn"$', text, re.M)
        cutoff = now - timedelta(days=learn_days if is_learn else default_days)
        if posted < cutoff:
            if not dry_run:
                path.write_text(
                    text.replace('status: "active"', 'status: "archived"', 1),
                    encoding="utf-8",
                )
            archived.append(path.name)

    suffix = " (dry-run)" if dry_run else ""
    print(f"auto-archived (Learn>{learn_days}d, others>{default_days}d): {len(archived)}{suffix}")
    for name in archived:
        print(f"  - {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
