---
title: "Azure VM vCore Customization GA: Disable SMT and Constrained Cores"
date: 2026-08-20T11:19:17.091246+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["azure", "virtual-machines", "compute"]
cves: []
source: "https://azure.microsoft.com/updates?id=569051"
source_name: "Azure Updates"
status: "active"
---
- **Platform/SRE — Plan:** Now GA, these features let you right-size compute for workloads needing predictable single-threaded performance (e.g. licensed-per-core DBs) or reduced licensing costs; evaluate whether any production node pools or VM fleets would benefit from constrained-core configurations this quarter.
- **CI/CD — Skip**
- **Leader — Plan:** Constrained Cores can reduce per-core software licensing costs on Azure VMs; evaluate whether standardizing on constrained-core SKUs in the next planning cycle would yield material savings for licensed-per-core workloads.
- **Signals:** GA announcement
