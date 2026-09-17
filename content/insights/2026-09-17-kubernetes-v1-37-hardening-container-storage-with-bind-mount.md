---
title: "Kubernetes v1.37 adds emptyDir permissions and bind mount security flags"
date: 2026-09-17T15:22:47.330544+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["kubernetes", "storage-security", "container-hardening"]
cves: []
source: "https://kubernetes.io/blog/2026/09/16/kubernetes-v1-37-hardening-container-storage/"
source_name: "Kubernetes Blog"
status: "active"
---
- **Platform/SRE — Plan:** Kubernetes v1.37 GA ships emptyDir permission modes (including sticky bit) and bind mount options (noexec, nosuid, nodev) — schedule evaluation and adoption as part of your 1.37 upgrade cycle to harden shared writable volumes; no forced deadline until EOL 2027-10-28.
- **CI/CD — Skip**
- **Leader — Skip**
- **Signals:** Kubernetes 1.37 EOL 2027-10-28
