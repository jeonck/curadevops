---
title: "npm extends 72-hour security hold to all accounts after recovery-code sign-in"
date: 2026-09-11T14:43:59.795234+00:00
verdict: "Learn"
verdict_platform: "Skip"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["npm", "supply-chain-security", "account-security"]
cves: []
source: "https://github.blog/changelog/2026-09-09-npm-extends-recovery-code-security-holds-to-all-accounts"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Learn:** npm now applies a 72-hour security hold to any account following a recovery-code sign-in, broadening a protection previously limited to high-impact accounts; no pipeline changes are needed since CI automation should use tokens, not recovery codes, but this informs npm supply-chain security posture.
- **Leader — Skip**
