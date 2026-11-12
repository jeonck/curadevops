---
title: "Amazon EKS Provisioned Control Plane gets 24 GB etcd on 4XL/8XL tiers"
date: 2026-11-12T18:39:17.321944+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["eks", "kubernetes", "etcd"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-provisioned-control-plane-larger-etcd-database/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capacity increase for large EKS clusters — if you operate 4XL/8XL Provisioned Control Plane clusters running EKS 1.34+, existing clusters get the upgrade automatically; evaluate whether large-scale workloads (AI/ML training, high-object-count batch jobs) now justify moving to these tiers to avoid etcd saturation events.
- **CI/CD — Skip**
- **Leader — Skip**
