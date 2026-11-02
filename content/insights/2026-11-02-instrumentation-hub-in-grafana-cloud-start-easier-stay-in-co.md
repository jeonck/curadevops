---
title: "Grafana Cloud Instrumentation Hub reaches GA with OTel SDK injection"
date: 2026-11-02T20:36:17.574365+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["observability", "opentelemetry", "grafana-cloud"]
cves: []
source: "https://grafana.com/blog/instrumentation-hub-start-your-observability-journey-easier-and-still-stay-in-control/"
source_name: "Grafana Blog"
status: "active"
---
- **Platform/SRE — Plan:** Platform teams owning the observability stack should evaluate Instrumentation Hub this quarter — the GA eBPF + OTel SDK auto-injection could replace weeks of manual instrumentation work per service, but requires validating fit with existing Prometheus/OTel pipelines before adopting.
- **CI/CD — Skip**
- **Leader — Learn:** This shapes thinking around observability golden paths — auto-instrumentation via eBPF and OTel injection could shrink the months of toil teams currently spend on coverage gaps, but there is no strategic decision or cost change forcing action now.
- **Signals:** GA announcement
