---
title: "AWS Nitro Sandboxes GA on EKS, ECS, and EC2 for hardware-isolated workloads"
date: 2026-11-09T21:13:22.907131+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws", "kubernetes", "container-security"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/nitro-sandboxes-eks-ecs-ec2/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Nitro Sandboxes are now GA on EKS and ECS, enabling per-pod or per-task VM-level isolation with a one-line config change and near-native performance. Evaluate this quarter for multi-tenant, regulated, or AI agent workloads where stronger isolation boundaries are required.
- **CI/CD — Skip**
- **Leader — Learn:** Nitro Sandboxes let teams run untrusted or regulated workloads on shared EC2 instances with hardware isolation, potentially reducing compute costs while improving security posture for AI agent execution. Worth tracking as this pattern matures, but no toolchain strategy decision is pending yet.
