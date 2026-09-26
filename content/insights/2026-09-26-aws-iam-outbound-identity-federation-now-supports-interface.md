---
title: "AWS IAM OIDC discovery endpoints now available via VPC interface endpoints"
date: 2026-09-26T14:49:11.187076+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws-iam", "vpc-endpoints", "oidc"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-sts-vpc-oidc/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Workloads in private VPCs without internet egress can now verify JWTs via PrivateLink rather than requiring internet access; evaluate creating an interface VPC endpoint if you run air-gapped or restricted-egress VPCs that rely on IAM outbound identity federation.
- **CI/CD — Skip**
- **Leader — Skip**
