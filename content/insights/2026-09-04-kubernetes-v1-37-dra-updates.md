---
title: "Kubernetes 1.37: DRA Extended Resource Support Reaches GA"
date: 2026-09-04T14:38:54.847255+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["kubernetes", "dra", "platform"]
cves: []
source: "https://kubernetes.io/blog/2026/09/03/kubernetes-v1-37-dra-updates/"
source_name: "Kubernetes Blog"
status: "active"
---
- **Platform/SRE — Plan:** DRA Extended Resource support is now stable in 1.37, letting existing extended-resource workloads (e.g. example.com/gpu) route through DRA drivers without ResourceClaims or device plugins — a meaningful adoption path to evaluate this quarter. EOL for 1.37 is 2027-10-28, so no forced upgrade yet; plan an evaluation of DRA adoption for GPU/device workloads in the current planning cycle.
- **CI/CD — Skip**
- **Leader — Learn:** DRA reaching GA means GPU and accelerator workloads can now use a unified allocation model without dual plugin stacks — worth understanding for future platform architecture decisions around AI/ML infrastructure, but no toolchain strategy or budget action is required now.
- **Signals:** Kubernetes 1.37 EOL 2027-10-28
