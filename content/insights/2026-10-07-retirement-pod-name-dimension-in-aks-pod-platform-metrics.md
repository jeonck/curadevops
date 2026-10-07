---
title: "AKS pod name dimension retiring from Azure Monitor metrics Sept 2027"
date: 2026-10-07T17:37:04.706337+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aks", "azure-monitor", "observability"]
cves: []
source: "https://azure.microsoft.com/updates?id=570232"
source_name: "Azure Updates"
status: "active"
---
- **Platform/SRE — Plan:** The pod name dimension on AKS platform metrics (kube_pod_status_phase and related) is being removed September 30, 2027; audit Azure Monitor dashboards and alerts that rely on per-pod granularity from these metrics and plan migration to aggregate counters or Prometheus-based alternatives before that date.
- **CI/CD — Skip**
- **Leader — Skip**
- **Signals:** deprecation/EOL deadline mentioned: September 30, 2027
