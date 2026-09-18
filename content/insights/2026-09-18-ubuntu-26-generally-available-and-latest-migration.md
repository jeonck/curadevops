---
title: "Ubuntu 26.04 GA on GitHub Actions; ubuntu-latest migration incoming"
date: 2026-09-18T14:42:50.222201+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["github-actions", "runner-images", "ubuntu"]
cves: []
source: "https://github.blog/changelog/2026-09-17-ubuntu-26-generally-available-and-latest-migration"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** ubuntu-latest will migrate to Ubuntu 26.04, which can silently change pre-installed toolchain versions and break pipelines; audit workflows using ubuntu-latest and validate against ubuntu-26.04 before the cutover date GitHub publishes.
- **Leader — Skip**
- **Signals:** Ubuntu 26.04 EOL 2031-05-29 · GA announcement
