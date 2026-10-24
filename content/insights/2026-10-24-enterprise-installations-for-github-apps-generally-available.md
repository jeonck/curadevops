---
title: "GitHub Apps enterprise installations now generally available"
date: 2026-10-24T14:11:23.013433+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Learn"
tags: ["github-apps", "enterprise-auth", "supply-chain"]
cves: []
source: "https://github.blog/changelog/2026-10-23-enterprise-installations-for-github-apps-generally-available"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** GitHub Apps can now replace classic PATs for enterprise-wide automation; schedule an audit of existing PAT-based pipeline credentials and migrate to GitHub App installations for tighter scope and auditability — no forced deadline, but a clear security improvement to queue this quarter.
- **Leader — Learn:** This GA capability enables org-wide policy to standardize on GitHub Apps over classic PATs for automation, which strengthens credential hygiene and reduces blast radius of leaked tokens; worth factoring into enterprise GitHub governance standards but no immediate decision required.
- **Signals:** GA announcement
