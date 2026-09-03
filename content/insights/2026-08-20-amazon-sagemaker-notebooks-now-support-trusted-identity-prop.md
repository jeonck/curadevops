---
title: "SageMaker Notebooks gain per-user identity propagation via IAM Identity Center"
date: 2026-08-20T11:19:17.091246+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws", "iam", "data-access-control"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-sagemaker/"
source_name: "AWS What's New"
status: "archived"
---
- **Platform/SRE — Learn:** Relevant if your org runs SageMaker and Lake Formation with fine-grained data access; this GA feature removes the need for shared execution roles and adds per-user CloudTrail audit trails. No immediate action required unless you're actively designing a multi-user analytics platform.
- **CI/CD — Skip**
- **Leader — Learn:** Per-user data boundaries enforced at the Lake Formation layer with automatic identity propagation reduces compliance friction for orgs with strict data governance requirements; worth noting when evaluating SageMaker Unified Studio for enterprise analytics use cases.
