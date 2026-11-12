---
title: "EKS Auto Mode adds security groups for Pods (GA, K8s 1.36+)"
date: 2026-11-12T18:39:17.321944+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["eks", "kubernetes", "networking"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-auto-mode-security-groups-for-pods/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** EKS Auto Mode now supports pod-level security group assignment via SecurityGroupPolicy, eliminating the need for dedicated node pools per security boundary; evaluate adopting for workloads requiring direct VPC resource access (RDS, ElastiCache) — requires Kubernetes 1.36 or later on Auto Mode clusters.
- **CI/CD — Skip**
- **Leader — Learn:** Pod-level security groups in EKS Auto Mode can reduce node pool sprawl and simplify VPC segmentation strategy; worth factoring into cluster architecture standards review but no immediate decision required.
