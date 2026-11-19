---
title: "Azure Cosmos DB throughput buckets now generally available"
date: 2026-11-19T19:16:29.978589+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["azure-cosmos-db", "cloud-database", "multi-tenancy"]
cves: []
source: "https://azure.microsoft.com/updates?id=571488"
source_name: "Azure Updates"
status: "active"
---
- **Platform/SRE — Plan:** If you run Cosmos DB containers shared across multiple workloads, throughput buckets provide per-workload consumption limits GA today — evaluate adopting this quarter to improve noisy-neighbor isolation without container-level partitioning.
- **CI/CD — Skip**
- **Leader — Learn:** New Cosmos DB capability enabling workload-level throughput governance on shared containers; worth factoring into multi-tenant database architecture discussions and cost-allocation strategy.
- **Signals:** GA announcement
