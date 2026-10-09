---
title: "AKS Managed StandardV2 NAT Gateway Now GA, New Default for New Clusters"
date: 2026-10-09T17:15:30.772048+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aks", "networking", "azure"]
cves: []
source: "https://azure.microsoft.com/updates?id=574430"
source_name: "Azure Updates"
status: "active"
---
- **Platform/SRE — Plan:** StandardV2 is now the default managed NAT Gateway SKU for new AKS clusters in supported regions, which may affect cluster provisioning templates and IaC modules. Review and update cluster-creation configurations to account for the new default SKU before spinning up new clusters.
- **CI/CD — Skip**
- **Leader — Learn:** AKS now manages a higher-performance NAT Gateway SKU by default for new clusters, shifting the networking default without a licensing or cost-model change — worth noting as AKS managed networking capabilities mature.
- **Signals:** GA announcement
