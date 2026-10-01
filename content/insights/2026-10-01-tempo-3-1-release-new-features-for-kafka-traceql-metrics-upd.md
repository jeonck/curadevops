---
title: "Tempo 3.1 adds Kafka TLS/SASL, trace redaction, and TraceQL metrics updates"
date: 2026-10-01T17:14:12.201245+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["observability", "distributed-tracing", "kafka"]
cves: []
source: "https://grafana.com/blog/tempo-3-1-release-all-the-latest-features/"
source_name: "Grafana Blog"
status: "active"
---
- **Platform/SRE — Plan:** Platform teams running Tempo 3.0 in microservices mode with Kafka-based ingestion shipped without TLS support — a real security gap. Upgrading to 3.1 closes it with TLS and additional SASL mechanisms (SCRAM-SHA-256/512, OAUTHBEARER, AWS_MSK_IAM); schedule the upgrade this quarter if Kafka ingestion is in use.
- **CI/CD — Skip**
- **Leader — Skip**
