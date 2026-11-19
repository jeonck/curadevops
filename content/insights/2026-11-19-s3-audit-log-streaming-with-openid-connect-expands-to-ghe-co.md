---
title: "GitHub Enterprise Cloud adds S3 audit log streaming via OIDC"
date: 2026-11-19T19:16:29.978589+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["github-enterprise", "audit-logging", "oidc"]
cves: []
source: "https://github.blog/changelog/2026-11-19-s3-audit-log-streaming-with-openid-connect-expands-to-ghe-com"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Plan:** GHE.com (data residency) orgs can now replace long-lived S3 credentials with OIDC-based streaming for audit logs; worth scheduling if your org uses GHE.com and centralizes audit data in S3 for compliance or SIEM ingestion.
- **CI/CD — Skip**
- **Leader — Learn:** Minor capability parity for GHE.com data-residency customers — if your org is on GHE.com and needs audit log streaming, this removes a previous blocker, but no strategic decision is required.
