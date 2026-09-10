---
title: "Monitor Cypress test metrics with Grafana Cloud via Pushgateway"
date: 2026-09-10T14:43:05.673701+00:00
verdict: "Learn"
verdict_platform: "Skip"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["test-observability", "cypress", "grafana-cloud"]
cves: []
source: "https://grafana.com/blog/how-to-monitor-cypress-tests-with-grafana-cloud/"
source_name: "Grafana Blog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Learn:** The pattern of pushing per-spec pass/fail and duration metrics to a Prometheus Pushgateway and forwarding them to Grafana Cloud gives CI engineers a durable way to spot flaky-test and slowdown trends across runs; no new release or deadline, and the tutorial lives on Grafana's own marketing blog.
- **Leader — Skip**
