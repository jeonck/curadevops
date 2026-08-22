---
title: "Amazon EKS managed Argo CD capability gains custom argocd-cm config support"
date: 2026-08-22T11:13:23.946157+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["kubernetes", "argo-cd", "gitops"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-argo-cd-configuration"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** The managed EKS Argo CD capability now accepts argocd-cm ConfigMap settings, including custom health checks for CRDs that can hold sync waves until resources finish provisioning. If your clusters use this managed capability, evaluate adding custom health checks for your Custom Resources this quarter.
- **CI/CD — Learn:** Custom health check logic for CRDs in EKS-managed Argo CD means sync wave advancement can now be gated on actual resource readiness rather than Argo CD's default no-op behavior; worth factoring into GitOps deployment design if your org uses this specific managed capability.
- **Leader — Skip**
