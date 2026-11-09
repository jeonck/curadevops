---
title: "Amazon Athena adds system tables for query observability and cost allocation"
date: 2026-11-09T21:13:22.907131+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["athena", "observability", "finops"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/athena-system-tables/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability lets platform teams build cost-allocation dashboards by querying Athena's query_executions table directly with SQL — no custom ETL required. Evaluate enabling system tables this quarter for workgroup-level spend visibility.
- **CI/CD — Skip**
- **Leader — Learn:** Athena now exposes usage data as managed Iceberg tables, simplifying FinOps reporting for teams that run Athena at scale; worth noting as an option when reviewing observability and cost-attribution tooling.
