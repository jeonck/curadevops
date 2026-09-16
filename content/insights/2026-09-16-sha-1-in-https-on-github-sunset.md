---
title: "GitHub disables SHA-1 in HTTPS as of 2026-09-15"
date: 2026-09-16T15:13:50.183087+00:00
verdict: "Act"
verdict_platform: "Plan"
verdict_cicd: "Act"
verdict_leader: "Skip"
tags: ["github", "tls", "deprecation"]
cves: []
source: "https://github.blog/changelog/2026-09-15-sha-1-in-https-on-github-sunset"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Plan:** SHA-1 HTTPS on GitHub is now enforced (2026-09-15); audit any infrastructure tooling—Terraform module fetches, Helm chart sources, custom operators—that connects to GitHub via HTTPS and update any clients running legacy TLS libraries before they surface connectivity failures.
- **CI/CD — Act:** Enforcement is live as of 2026-09-15—any runner image or build tool using an old TLS stack that negotiates SHA-1 for HTTPS connections to GitHub is already failing; audit runner images and git client versions immediately and update or replace those using legacy OpenSSL/TLS configurations.
- **Leader — Skip**
- **Signals:** deprecation mentioned (no explicit date found)
