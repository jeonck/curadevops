---
title: "AKS Azure Files CSI driver gains workload identity for SMB mounts"
date: 2026-08-28T21:17:44.564118+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aks", "kubernetes", "azure"]
cves: []
source: "https://azure.microsoft.com/updates?id=570120"
source_name: "Azure Updates"
status: "active"
---
- **Platform/SRE — Plan:** This GA capability lets AKS pods authenticate to SMB file shares via workload identity instead of node-level managed identity, improving least-privilege posture. Evaluate replacing existing managed-identity-based Azure Files mounts with workload identity bindings in your next infrastructure review cycle.
- **CI/CD — Skip**
- **Leader — Skip**
- **Signals:** GA announcement
