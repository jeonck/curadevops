---
title: "AWS IAM Identity Center adds one-click multi-Region setup for new org instances"
date: 2026-08-08T11:21:15.863063+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws", "iam-identity-center", "multi-region"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-iam-identity-center-supports-one-click-multi-region-option-new-organization-instances"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** This GA simplification reduces friction for deploying resilient multi-Region identity access — if standing up a new IAM Identity Center organization instance, select the one-click multi-Region option rather than manually wiring KMS keys and Region replication. Existing instances are unaffected, so queue this for next new-instance or resilience-architecture work this quarter.
- **CI/CD — Skip**
- **Leader — Skip**
