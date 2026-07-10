#!/usr/bin/env bash
# Pause collection — commits the .collect-paused marker so the daily/weekly
# cron skips collection & judgment (deploys keep working; resume: resume.sh)
# Also available from the web: Actions tab → Pipeline Control → pause
set -euo pipefail
cd "$(dirname "$0")/.."
[ -f .collect-paused ] && { echo "already paused"; exit 0; }
git pull -q --rebase
date -u +%FT%TZ > .collect-paused
git add .collect-paused
git commit -q -m "chore: pause collection"
git push -q
echo "collection paused (.collect-paused committed)"
echo "- daily/weekly cron: collection & judgment skipped"
echo "- push-triggered deploys: still active"
echo "- resume: ./pipeline/resume.sh"
