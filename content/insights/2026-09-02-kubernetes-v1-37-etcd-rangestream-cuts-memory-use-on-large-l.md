---
title: "Kubernetes v1.37: etcd RangeStream graduates to beta, cuts API server memory on large reads"
date: 2026-09-02T14:51:34.370509+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["kubernetes", "etcd", "memory-optimization"]
cves: []
source: "https://kubernetes.io/blog/2026/09/01/kubernetes-v1-37-etcd-range-stream/"
source_name: "Kubernetes Blog"
status: "active"
---
- **Platform/SRE — Learn:** RangeStream is still beta in v1.37 (requires etcd v3.7), so not yet production-adoptable, but SREs running clusters with many large objects (e.g., Pods at scale) should track this as a near-term mitigation for API server and etcd OOM risk during cache repopulation.
- **CI/CD — Skip**
- **Leader — Skip**
- **Signals:** Kubernetes 1.37 EOL 2027-10-28 · etcd 3.7 supported
