---
title: "AWS IAM Identity Center multi-Region support expands to opt-in and GovCloud Regions"
date: 2026-10-02T16:25:37.540030+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["iam", "aws", "identity"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-iam-identity-center-extends-multi-region-support-to-more-aws-regions"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If you operate in opt-in or GovCloud/China regions, evaluate enabling multi-Region IAM Identity Center replication this quarter to improve SSO resilience; requires setting up a multi-Region customer-managed KMS key for existing instances.
- **CI/CD — Skip**
- **Leader — Learn:** IAM Identity Center now supports identity replication across opt-in and GovCloud regions, a useful resilience capability to factor into multi-region access strategy and compliance planning.
