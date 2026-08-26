---
title: "Minimus Registry Shutting Down Oct 22 — Migrate to Docker Hardened Images"
date: 2026-08-26T11:21:00.410731+00:00
verdict: "Act"
verdict_platform: "Act"
verdict_cicd: "Act"
verdict_leader: "Skip"
tags: ["base-images", "registry-migration", "docker"]
cves: []
source: "https://www.docker.com/blog/moving-from-minimus-to-docker-hardened-images/"
source_name: "Docker Blog"
status: "active"
---
- **Platform/SRE — Act:** The Minimus registry goes offline October 22, 2026; audit all Dockerfiles, Helm charts, and Kubernetes manifests for Minimus base image references and complete migration to Docker Hardened Images before that date to prevent broken image pulls in production.
- **CI/CD — Act:** Any pipeline pulling from the Minimus registry will break after October 22, 2026; inventory all build Dockerfiles and CI base-image references now and migrate to Docker Hardened Images using the provided migration path and Docker's free migration assistance before the deadline.
- **Leader — Skip**
