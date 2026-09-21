---
title: "containerd API v1.12.0 ships with shim and runc options deprecations"
date: 2026-09-21T17:51:59.466596+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["containerd", "container-runtime", "deprecation"]
cves: []
source: "https://github.com/containerd/containerd/releases/tag/api%2Fv1.12.0"
source_name: "Releases: containerd"
status: "active"
---
- **Platform/SRE — Plan:** This GA release deprecates the containerd.io/runtime-allow-mounts shim annotation (replaced by MountCapabilities extension) and task API address/version fields in runc options; plan migration away from both, though no removal date is confirmed yet.
- **CI/CD — Skip**
- **Leader — Skip**
- **Signals:** containerd 2.4 EOL 2027-05-16 · deprecation mentioned (no explicit date found)
