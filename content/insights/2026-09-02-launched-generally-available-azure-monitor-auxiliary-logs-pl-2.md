---
title: "Azure Monitor Auxiliary Logs plan switching now GA"
date: 2026-09-02T14:51:34.370509+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["azure-monitor", "observability", "cost-optimization"]
cves: []
source: "https://azure.microsoft.com/updates?id=569904"
source_name: "Azure Updates"
status: "active"
---
- **Platform/SRE — Plan:** This GA capability lets platform teams migrate high-volume compliance and audit Azure tables to the lower-cost Auxiliary plan without rebuilding pipelines. Evaluate which existing Log Analytics tables qualify for plan switching this quarter to reduce observability ingestion costs.
- **CI/CD — Skip**
- **Leader — Plan:** The plan-switching capability is a concrete FinOps lever for reducing Azure Monitor spend on high-volume, rarely-queried compliance logs. Worth scheduling an audit of Log Analytics table plans to identify cost-reduction opportunities within the current planning cycle.
- **Signals:** GA announcement
