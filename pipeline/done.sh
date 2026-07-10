#!/usr/bin/env bash
# Manual archive: front matter status: "active" → "archived"
# usage: pipeline/done.sh content/insights/2026-07-10-some-post.md
set -euo pipefail
[ $# -ge 1 ] || { echo "usage: $0 <content/insights/file.md> [...]"; exit 1; }
for f in "$@"; do
  sed -i.bak 's/^status: "active"/status: "archived"/' "$f" && rm -f "$f.bak"
  echo "archived: $f"
done
