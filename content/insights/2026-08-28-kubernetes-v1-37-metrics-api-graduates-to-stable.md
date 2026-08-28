---
title: "Kubernetes v1.37: metrics.k8s.io API graduates to stable v1"
date: 2026-08-28T21:17:44.564118+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["kubernetes", "metrics-api", "api-graduation"]
cves: []
source: "https://kubernetes.io/blog/2026/08/27/kubernetes-v1-37-metrics-api-ga/"
source_name: "Kubernetes Blog"
status: "active"
---
- **Platform/SRE — Learn:** The metrics.k8s.io/v1 API is functionally identical to v1beta1 — no field changes, no behavioral differences. Worth noting when planning a v1.37 upgrade so any hardcoded v1beta1 API paths in tooling or manifests get updated, but no v1beta1 deprecation deadline is announced.
- **CI/CD — Skip**
- **Leader — Skip**
