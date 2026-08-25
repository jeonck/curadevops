---
title: "Amazon EKS supports up to 10 external OIDC identity providers per cluster"
date: 2026-08-25T11:19:32.404793+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["eks", "oidc", "kubernetes"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-multiple-oidc-providers"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** This GA feature removes the need for an identity broker when authenticating multiple user populations (employees, contractors, CI/CD systems) to EKS clusters. Evaluate whether your clusters could simplify their auth architecture by replacing any intermediary OIDC broker with direct per-provider associations.
- **CI/CD — Skip**
- **Leader — Skip**
