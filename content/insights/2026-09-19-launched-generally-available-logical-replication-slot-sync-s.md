---
title: "Azure PostgreSQL Flexible Server adds logical replication slot sync metric"
date: 2026-09-19T14:03:42.839126+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["azure", "postgresql", "observability"]
cves: []
source: "https://azure.microsoft.com/updates?id=568414"
source_name: "Azure Updates"
status: "active"
---
- **Platform/SRE — Plan:** If you run Azure PostgreSQL Flexible Server with logical replication, add the new logical_replication_slot_sync_status Azure Monitor metric to your dashboards and alerts this quarter to catch slot lag before it bloats WAL retention.
- **CI/CD — Skip**
- **Leader — Skip**
- **Signals:** GA announcement
