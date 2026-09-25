---
title: "GitHub Actions: expired artifacts removed from UI and REST API"
date: 2026-09-25T15:41:44.461559+00:00
verdict: "Learn"
verdict_platform: "Skip"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["github-actions", "artifacts", "api-change"]
cves: []
source: "https://github.blog/changelog/2026-09-24-expired-github-actions-artifacts-no-longer-shown-in-ui-and-api"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Learn:** Expired artifacts no longer appear in the Actions run summary or via the REST API; any automation or scripts that queried the artifacts API and expected expired entries to be present may silently return fewer results — worth auditing artifact-listing logic.
- **Leader — Skip**
