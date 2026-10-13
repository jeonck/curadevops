---
title: "GitHub secret scanning adds Salesforce, blocks Anthropic keys by default"
date: 2026-10-13T17:52:48.720055+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["secret-scanning", "supply-chain", "github"]
cves: []
source: "https://github.blog/changelog/2026-10-13-secret-scanning-blocks-anthropic-keys-by-default-adds-salesforce"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** Verify your repositories have push protection enabled and audit any existing Anthropic API keys or Salesforce credentials in build logs or secrets; no deadline but this is a worthwhile supply-chain hardening step to schedule.
- **Leader — Skip**
