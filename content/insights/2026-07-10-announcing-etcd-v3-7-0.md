---
title: "etcd v3.7.0 GA: RangeStream, v2store removal, protobuf overhaul"
date: 2026-07-10T11:00:57.610632-05:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["etcd", "kubernetes", "minor-release"]
cves: []
source: "https://kubernetes.io/blog/2026/07/08/announcing-etcd-3.7/"
source_name: "Kubernetes Blog"
status: "active"
---
- **Platform/SRE — Plan:** etcd is the Kubernetes control-plane datastore, so this GA minor release is directly relevant; evaluate adopting v3.7 this quarter, particularly if large result-set latency or v2store remnants are pain points — no forced-upgrade deadline exists yet.
- **CI/CD — Skip**
- **Leader — Skip**
- **Signals:** etcd 3.7 supported · etcd 3.6 supported
