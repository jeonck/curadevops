---
title: "Azure Key Vault Secrets Provider Extension for Arc Kubernetes retires Oct 2027"
date: 2026-10-10T16:03:07.603064+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["azure", "kubernetes", "secrets-management"]
cves: []
source: "https://azure.microsoft.com/updates?id=570313"
source_name: "Azure Updates"
status: "active"
---
- **Platform/SRE — Plan:** If you run Azure Arc-enabled Kubernetes clusters, plan migration from the Azure Key Vault Secrets Provider Extension to the Azure Key Vault Secret Store Extension before the hard retirement date of October 9, 2027. One year is enough runway to schedule the migration, but start scoping which clusters are affected now.
- **CI/CD — Skip**
- **Leader — Plan:** Azure is retiring a secrets-integration extension for Arc-enabled Kubernetes with a clear replacement in the same ecosystem; ensure teams using Arc clusters have this migration on their roadmap before October 9, 2027, as there is no stay-on-current option beyond that date.
- **Signals:** deprecation/EOL deadline mentioned: October 9, 2027
