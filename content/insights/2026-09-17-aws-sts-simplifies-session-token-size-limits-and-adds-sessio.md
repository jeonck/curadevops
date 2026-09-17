---
title: "AWS STS unifies session token size limit to 4096 bytes, adds CloudWatch metrics"
date: 2026-09-17T15:22:47.330544+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws-sts", "iam", "observability"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-sts/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Learn:** The consolidated 4,096-byte limit and new CloudWatch/CloudTrail session token size metrics are worth noting for teams that use large inline policies or session tags in STS calls; no action required, no deadline, but the new metrics can surface token-bloat issues proactively.
- **CI/CD — Skip**
- **Leader — Skip**
