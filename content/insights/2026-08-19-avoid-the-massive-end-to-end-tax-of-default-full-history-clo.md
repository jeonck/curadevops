---
title: "Optimize git clone strategies to cut CI build times by up to 93%"
date: 2026-08-19T11:17:39.309563+00:00
verdict: "Plan"
verdict_platform: "Learn"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["git-optimization", "ci-performance", "agentic-ai"]
cves: []
source: "https://about.gitlab.com/blog/git-clone-override-policy/"
source_name: "GitLab Blog"
status: "active"
---
- **Platform/SRE — Learn:** Relevant for teams self-hosting GitLab — shallow and partial clones reduce server-side pack-building load, which compounds as agentic workloads increase clone frequency. No operational change required today, but useful context for capacity planning.
- **CI/CD — Plan:** Audit pipeline clone configurations and migrate to shallow (`--depth=1`) or partial (`--filter=blob:none`) clones; benchmarks show up to 93% time and 98% disk reduction per clone. No hard deadline, but AI-agent-driven clone volume makes this a near-term efficiency project worth scheduling this quarter.
- **Leader — Skip**
