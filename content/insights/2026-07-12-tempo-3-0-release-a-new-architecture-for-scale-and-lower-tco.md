---
title: "Tempo 3.0: Kafka-native architecture, RF3 removed, TraceQL metrics GA"
date: 2026-07-12T11:52:23.513906+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["distributed-tracing", "observability", "grafana"]
cves: []
source: "https://grafana.com/blog/tempo-3-0-release-all-the-latest-features/"
source_name: "Grafana Blog"
status: "archived"
---
- **Platform/SRE — Plan:** This GA major release changes how Tempo is deployed at scale — removing the RF3 requirement reduces storage overhead and the new Kafka-compatible architecture decouples read/write paths. Teams running Tempo should schedule an upgrade evaluation this quarter to assess the operational and cost impact.
- **CI/CD — Skip**
- **Leader — Learn:** The RF3 removal and new architecture lower the infrastructure cost of running distributed tracing at scale, which is a useful data point if Tempo is part of the observability standard — but no strategic decision is forced by this release.
- **Signals:** GA announcement · major release (3.0)
