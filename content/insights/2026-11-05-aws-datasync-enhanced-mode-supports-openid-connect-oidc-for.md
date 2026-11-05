---
title: "AWS DataSync Enhanced mode adds OIDC auth for GCS and Azure Blob"
date: 2026-11-05T18:24:13.891932+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["datasync", "cloud-security", "oidc"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/datasync-enhanced-oidc-google-azure/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If you use DataSync to move data between AWS and Google Cloud Storage or Azure Blob Storage, you can now replace long-lived HMAC/SAS credentials with IAM-role-based short-lived OIDC tokens, improving your security posture. Evaluate migrating existing DataSync locations to OIDC this quarter if your org has policies against static credentials.
- **CI/CD — Skip**
- **Leader — Skip**
