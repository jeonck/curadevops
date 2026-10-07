---
title: "Kubernetes cgroup v1 Deprecated: Nodes Blocked from Starting in K8s 1.35+"
date: 2026-10-07T17:37:04.706337+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["kubernetes", "cgroups", "deprecation"]
cves: []
source: "https://kubernetes.io/blog/2026/10/06/kubernetes-cgroups-v2-shift/"
source_name: "Kubernetes Blog"
status: "active"
---
- **Platform/SRE — Plan:** Kubernetes 1.35 (currently GA, EOL 2027-02-28) defaults failCgroupV1 to true, meaning kubelet refuses to start on cgroup v1 nodes without an explicit override. Audit all Linux nodes for cgroup version and complete migration to cgroup v2 before upgrading any cluster to 1.35 or later.
- **CI/CD — Skip**
- **Leader — Skip**
- **Signals:** Kubernetes 1.31 is past EOL (2025-11-11, 330d ago) · Kubernetes 1.25 is past EOL (2023-10-27, 1076d ago) · Kubernetes 1.35 EOL 2027-02-28 · deprecation mentioned (no explicit date found)
