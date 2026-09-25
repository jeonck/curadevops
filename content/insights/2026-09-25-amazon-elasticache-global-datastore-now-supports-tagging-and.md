---
title: "ElastiCache Global Datastore adds tagging and tag-based access control"
date: 2026-09-25T15:41:44.461559+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws", "elasticache", "iam"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-elasticache-global-datastore-tagging/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Teams running ElastiCache Global Datastore across regions can now enforce consistent IAM/SCP policies and cost allocation via tags; worth updating your tagging standards and IAM policies this quarter to close the permission-model gap.
- **CI/CD — Skip**
- **Leader — Learn:** This closes a cost-allocation and access-control gap in multi-region ElastiCache deployments, useful context if the org is standardizing FinOps tagging policies across AWS resources.
