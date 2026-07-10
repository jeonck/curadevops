#!/usr/bin/env bash
# Resume collection paused by pause.sh
# Also available from the web: Actions tab → Pipeline Control → resume
set -euo pipefail
cd "$(dirname "$0")/.."
[ -f .collect-paused ] || { echo "collection already running"; exit 0; }
git pull -q --rebase
git rm -q .collect-paused
git commit -q -m "chore: resume collection"
git push -q
echo "collection resumed — next cron runs normally"
echo "- to collect once right now: gh workflow run daily.yml"
