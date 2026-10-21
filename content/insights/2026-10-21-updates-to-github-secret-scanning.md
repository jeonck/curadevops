---
title: "GitHub secret scanning audit log field change on Nov 12, 2026"
date: 2026-10-21T15:46:15.304693+00:00
verdict: "Act"
verdict_platform: "Skip"
verdict_cicd: "Act"
verdict_leader: "Skip"
tags: ["secret-scanning", "github", "audit-logs"]
cves: []
source: "https://github.blog/changelog/2026-10-20-updates-to-github-secret-scanning"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Act:** The `business` field in `secret_scanning_alert.*` and `secret_scanning_push_protection.bypass` audit log events changes on November 12, 2026; audit any automation, SIEM integrations, or compliance scripts that parse these events and update field references before that date.
- **Leader — Skip**
