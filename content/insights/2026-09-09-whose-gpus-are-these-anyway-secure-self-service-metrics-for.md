---
title: "Secure self-service GPU metrics for multi-tenant Kubernetes"
date: 2026-09-09T14:56:08.335953+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["kubernetes", "gpu", "observability"]
cves: []
source: "https://www.cncf.io/blog/2026/09/09/whose-gpus-are-these-anyway-secure-self-service-metrics-for-multi-tenant-kubernetes/"
source_name: "CNCF Blog"
status: "active"
---
- **Platform/SRE — Learn:** Explores patterns for exposing per-tenant GPU utilization metrics without cross-tenant visibility leakage — worth reviewing if you operate shared GPU clusters, but no tooling release or deadline anchors this as actionable now.
- **CI/CD — Skip**
- **Leader — Learn:** Addresses the cost-attribution problem for shared GPU infrastructure, relevant if GPU spend is a significant and hard-to-attribute budget line, but this is a design pattern post rather than a strategic decision trigger.
