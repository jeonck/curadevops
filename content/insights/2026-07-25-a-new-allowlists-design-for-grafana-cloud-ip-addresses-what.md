---
title: "Grafana Cloud replaces per-product IP allowlists with unified API by Jan 2027"
date: 2026-07-25T11:58:38.501915+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["grafana-cloud", "networking", "observability"]
cves: []
source: "https://grafana.com/blog/a-new-allowlists-design-for-grafana-cloud-ip-addresses-what-you-need-to-know/"
source_name: "Grafana Blog"
status: "active"
---
- **Platform/SRE — Plan:** Teams using IP allowlisting to permit Grafana Cloud traffic must migrate from legacy per-product endpoints (JSON, txt, DNS) to the new unified Allowlist API before January 31, 2027, when the old formats stop being maintained; schedule the allowlist automation update and test before the deadline.
- **CI/CD — Skip**
- **Leader — Skip**
