---
title: "Docker 29 defaults to containerd image store on new installs"
date: 2026-07-16T12:15:50.892178+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["docker", "containerd", "image-store"]
cves: []
source: "https://docs.docker.com/engine/storage/containerd"
source_name: "HN (docker)"
status: "active"
---
- **Platform/SRE — Plan:** New Docker 29 installs default to the containerd image store rather than the classic overlay store, which changes image management behavior. Audit IaC and provisioning scripts that stand up Docker nodes to verify compatibility with the new default before rolling out Docker 29 to new infrastructure.
- **CI/CD — Plan:** Ephemeral CI runners provisioned fresh on Docker 29 will silently get containerd-backed image storage, which can alter layer-caching behavior and multi-platform build handling. Test existing build and image-export workflows against the new default before adopting Docker 29 runner images.
- **Leader — Skip**
