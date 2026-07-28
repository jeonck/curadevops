---
title: "Kubernetes Pod-per-agent vs shared runtime for AI agents (kagent)"
date: 2026-07-14T12:06:40.063321+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["kubernetes", "ai-agents", "platform-architecture"]
cves: []
source: "https://www.cncf.io/blog/2026/07/14/is-a-pod-the-right-deployment-unit-for-an-ai-agent/"
source_name: "CNCF Blog"
status: "archived"
---
- **Platform/SRE — Learn:** Explores the architectural tradeoffs of running each AI agent in its own Pod/ServiceAccount versus a shared runtime on Kubernetes — useful context for platform engineers who may be asked to support AI agent workloads. No action required today.
- **CI/CD — Skip**
- **Leader — Learn:** Offers mental-model framing for how AI agent workloads map onto Kubernetes primitives, which could inform a platform strategy for AI/ML infrastructure — but no vendor, licensing, or cost decision is at stake.
