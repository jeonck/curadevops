---
title: "Kubernetes v1.37 HPA scale-to-zero now Beta, enabled by default"
date: 2026-09-03T14:50:54.558994+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["kubernetes", "autoscaling", "hpa"]
cves: []
source: "https://kubernetes.io/blog/2026/09/02/kubernetes-v1-37-hpa-scale-to-zero-beta/"
source_name: "Kubernetes Blog"
status: "active"
---
- **Platform/SRE — Learn:** Beta (pre-GA) feature that eliminates the need for external add-ons to scale queue consumers and GPU/CPU batch workloads to zero; worth evaluating in non-production clusters now, with a plan to adopt when it reaches GA.
- **CI/CD — Skip**
- **Leader — Learn:** The scale-to-zero HPA capability has meaningful cost-reduction potential for GPU and dedicated-CPU workloads, but it is still Beta; track for inclusion in platform cost-optimization standards when it reaches GA.
- **Signals:** Kubernetes 1.37 EOL 2027-10-28
