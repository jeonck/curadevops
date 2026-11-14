---
title: "AWS Batch on EKS gains seccomp, Linux capabilities, and pod-level security context"
date: 2026-11-14T16:48:22.800807+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws-batch", "eks", "pod-security"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-batch-eks-security-context/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If your EKS clusters enforce the Kubernetes restricted Pod Security Standard, this GA feature unblocks Batch workloads that previously required elevated privileges; evaluate updating job definitions to set seccomp profiles and drop capabilities in RegisterJobDefinition this quarter.
- **CI/CD — Skip**
- **Leader — Skip**
