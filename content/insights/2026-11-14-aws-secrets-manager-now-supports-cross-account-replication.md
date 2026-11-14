---
title: "AWS Secrets Manager adds cross-account secret replication"
date: 2026-11-14T16:48:22.800807+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["secrets-management", "aws", "multi-account"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-manager-cross-account/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** This new GA capability lets platform teams centralize secret ownership and rotation in a primary account while pushing always-current replicas to consuming accounts — eliminating cross-account KMS sharing and secret policies. Worth evaluating for multi-account architectures this quarter; no deadline drives urgency.
- **CI/CD — Skip**
- **Leader — Learn:** Useful context for multi-account isolation and DR posture — secrets can now live in a dedicated recovery account insulated from a compromised primary — but no strategic decision or cost/vendor-risk angle is triggered here.
