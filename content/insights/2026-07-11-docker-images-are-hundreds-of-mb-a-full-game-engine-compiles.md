---
title: "WASM vs Docker: 35MB game engine binary vs hundreds-of-MB images"
date: 2026-07-11T15:50:13.633791+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["wasm", "containers", "developer-experience"]
cves: []
source: "https://bogomolov.work/blog/posts/wasm-vs-docker/"
source_name: "HN (docker)"
status: "archived"
---
- **Platform/SRE — Learn:** Interesting size/portability comparison between WASM and container images, but no production infrastructure change warranted — worth tracking as WASM runtimes mature for platform workloads.
- **CI/CD — Learn:** WASM artifacts could eventually shrink build/publish times and registry storage costs, but no actionable pipeline change today — monitor for when toolchain support matures.
- **Leader — Skip**
