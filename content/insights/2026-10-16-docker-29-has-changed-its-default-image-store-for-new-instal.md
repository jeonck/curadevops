---
title: "Docker 29 switches default image store to containerd for new installs"
date: 2026-10-16T15:05:37.577214+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["docker", "containerd", "container-runtime"]
cves: []
source: "https://docs.docker.com/engine/storage/containerd"
source_name: "HN (docker)"
status: "active"
---
- **Platform/SRE — Plan:** New Docker 29 installs default to the containerd image store, which has different behavior for image layering, multi-platform support, and tooling compatibility; review and test before rolling out Docker 29 on new nodes or golden AMIs to avoid unexpected differences from existing hosts still on the legacy store.
- **CI/CD — Plan:** Any CI runner provisioning that installs Docker 29 fresh will get the containerd image store by default, which may affect build caching behavior and image layer handling; audit runner provisioning scripts and validate build pipelines against Docker 29 before upgrading runner images.
- **Leader — Skip**
