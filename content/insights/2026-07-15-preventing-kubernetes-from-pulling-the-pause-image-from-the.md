---
title: "Prevent Kubernetes from pulling pause image from internet"
date: 2026-07-15T12:10:55.908816+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["kubernetes", "security", "air-gap"]
cves: []
source: "https://kyle.cascade.family/posts/preventing-kubernetes-from-pulling-the-pause-image-from-the-internet/"
source_name: "HN (kubernetes)"
status: "archived"
---
- **Platform/SRE — Learn:** Useful pattern for air-gapped or registry-mirrored clusters: configure kubelet to use an internal mirror for the pause/infra image instead of registry.k8s.io. No deadline, but worth evaluating if egress control is a concern.
- **CI/CD — Skip**
- **Leader — Skip**
