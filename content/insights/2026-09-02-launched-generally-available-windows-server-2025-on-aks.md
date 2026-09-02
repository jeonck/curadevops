---
title: "Windows Server 2025 now GA on AKS"
date: 2026-09-02T14:51:34.370509+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aks", "windows", "kubernetes"]
cves: []
source: "https://azure.microsoft.com/updates?id=570090"
source_name: "Azure Updates"
status: "active"
---
- **Platform/SRE — Plan:** Windows Server 2025 is now a supported node OS on AKS, giving teams a clear upgrade target as older Windows Server versions approach end of support. Schedule evaluation of Windows node pool migration this quarter, especially if running 2019 or 2022 nodes — no forced-upgrade date is signaled yet, but the deprecation mention warrants adding it to the roadmap.
- **CI/CD — Skip**
- **Leader — Learn:** AKS now supports Windows Server 2025, extending the viability of Windows-based workloads on managed Kubernetes — useful context if the org is evaluating its Windows modernization strategy, but no strategic or cost decision is required now.
- **Signals:** deprecation mentioned (no explicit date found) · GA announcement
