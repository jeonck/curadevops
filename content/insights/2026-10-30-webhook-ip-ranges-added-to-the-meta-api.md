---
title: "GitHub webhook IP ranges added to Meta API hooks field"
date: 2026-10-30T16:53:40.221998+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["github", "webhooks", "networking"]
cves: []
source: "https://github.blog/changelog/2026-10-29-webhook-ip-ranges-added-to-the-meta-api"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Plan:** If your org maintains a firewall or security-group allowlist for incoming GitHub webhook traffic, update it to include the new IP ranges from the Meta API hooks field before deployments that rely on webhooks start failing.
- **CI/CD — Plan:** Pipelines that trigger via GitHub webhooks and sit behind a strict inbound allowlist may silently drop deliveries; pull the updated ranges from the Meta API and refresh your allowlist rules.
- **Leader — Skip**
