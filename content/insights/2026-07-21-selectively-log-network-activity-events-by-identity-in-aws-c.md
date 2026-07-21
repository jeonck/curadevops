---
title: "AWS CloudTrail adds UserIdentity filtering for VPC endpoint events"
date: 2026-07-21T12:20:39.125523+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-cloudtrail", "vpc-endpoints", "data-perimeter"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-cloudtrail-filter-useridentity-advance-selectors/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** This GA feature lets you reduce CloudTrail network activity event volume and cost by scoping logging to untrusted or access-denied identities on VPC endpoints — a concrete improvement for data perimeter monitoring. Update your CloudTrail advanced event selectors this quarter to filter trusted IAM roles and cut noise on VpceAccessDenied events.
- **CI/CD — Skip**
- **Leader — Learn:** This feature enables selective CloudTrail logging that can meaningfully reduce ingestion costs for high-volume VPC endpoint environments, relevant for FinOps conversations around AWS audit logging spend — no strategic decision required now.
