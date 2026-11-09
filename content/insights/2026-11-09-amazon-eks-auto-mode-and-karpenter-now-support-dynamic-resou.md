---
title: "EKS Auto Mode and Karpenter gain Dynamic Resource Allocation for GPUs/EFA"
date: 2026-11-09T21:13:22.907131+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["eks", "gpu", "kubernetes"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-auto-mode-karpenter-dra/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If you run GPU or EFA-backed workloads on EKS Auto Mode or Karpenter, DRA enables GPU sharing across pods and topology-aligned device allocation — evaluate adopting ResourceClaim objects this quarter to reduce device oversubscription risk and potentially lower instance costs.
- **CI/CD — Skip**
- **Leader — Learn:** DRA-based GPU sharing across pods could meaningfully reduce EC2 GPU instance spend for ML/inference workloads; worth flagging to platform teams if the org runs significant GPU clusters on EKS, but no immediate strategic decision is forced.
