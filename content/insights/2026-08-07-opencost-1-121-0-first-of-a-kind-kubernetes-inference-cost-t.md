---
title: "OpenCost 1.121.0 adds Kubernetes inference cost tracking"
date: 2026-08-07T00:23:45.191261+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["kubernetes", "finops", "gpu"]
cves: []
source: "https://www.cncf.io/blog/2026/08/05/opencost-1-121-0-first-of-a-kind-kubernetes-inference-cost-tracking/"
source_name: "CNCF Blog"
status: "active"
---
- **Platform/SRE — Plan:** This GA release adds per-token inference cost attribution to OpenCost, directly addressing GPU cost visibility for platform teams running AI workloads on Kubernetes. Evaluate upgrading OpenCost to 1.121.0 this quarter if your clusters host inference workloads.
- **CI/CD — Skip**
- **Leader — Plan:** First GA implementation of per-token inference cost tracking in an open CNCF tool is a meaningful FinOps development for orgs with growing GPU spend; evaluate adopting OpenCost 1.121.0 as part of your AI cost attribution strategy this planning cycle.
