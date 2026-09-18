---
title: "AWS Transfer Family SFTP adds source IP preservation via NLB Proxy Protocol v2"
date: 2026-09-18T14:42:50.222201+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws", "networking", "sftp"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-source-ip-nlb/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Teams using Transfer Family SFTP behind an NLB for compliance or IP-based access controls should evaluate enabling this feature; no deadline, but it unlocks accurate audit logs and identity-provider IP filtering that may be required for security reviews.
- **CI/CD — Skip**
- **Leader — Skip**
