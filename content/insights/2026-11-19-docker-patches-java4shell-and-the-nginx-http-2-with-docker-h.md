---
title: "Docker Hardened Images patched for Java4Shell and NGINX HTTP/2 CVEs"
date: 2026-11-19T19:16:29.978589+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["container-security", "docker-hardened-images", "vulnerability-patch"]
cves: []
source: "https://www.docker.com/blog/docker-patches-java4shell-and-the-nginx-http-2-with-docker-hardened-images/"
source_name: "Docker Blog"
status: "active"
---
- **Platform/SRE — Plan:** If your platform uses Docker Hardened Images as base images for infrastructure containers, audit current image versions and update to the patched DHI catalog entries covering Java4Shell and the NGINX HTTP/2 vulnerability; no hard deadline found in signals, but patch this quarter.
- **CI/CD — Plan:** If build pipelines use DHI catalog images as runner or build-step base images, update pinned digests to pull the patched versions for Java4Shell and NGINX HTTP/2; no forced deadline, but schedule soon to close the supply-chain exposure.
- **Leader — Skip**
