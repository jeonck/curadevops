---
title: "docker-rollout-action: zero-downtime Docker Compose deploys via SSH"
date: 2026-09-30T16:35:00.804229+00:00
verdict: "Learn"
verdict_platform: "Skip"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["docker-compose", "deployment", "github-actions"]
cves: []
source: "https://github.com/mtizima/docker-rollout-action"
source_name: "GitHub Trending"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Learn:** Interesting pattern for teams still running Docker Compose over SSH: health-checked rollout with automatic rollback and a migrations hook baked in as a plain-Bash GitHub Action; worth bookmarking if you support non-Kubernetes deployment targets, but no deadline or adoption pressure.
- **Leader — Skip**
