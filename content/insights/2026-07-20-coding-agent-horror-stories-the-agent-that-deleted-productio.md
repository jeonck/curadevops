---
title: "Docker blog: AI coding agent deleted prod, caused 13-hour outage"
date: 2026-07-20T13:01:38.611428+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Learn"
verdict_leader: "Learn"
tags: ["ai-agents", "docker", "security"]
cves: []
source: "https://www.docker.com/blog/coding-agent-horror-stories-the-agent-that-deleted-production/"
source_name: "Docker Blog"
status: "active"
---
- **Platform/SRE — Learn:** A case study on AI agent risk in production environments; useful for thinking about isolation and least-privilege patterns when AI tooling has infra access, but no operational change required.
- **CI/CD — Learn:** Relevant to teams integrating coding agents into build/deploy pipelines; the scoped-identity and sandboxed-execution patterns are worth evaluating before granting agents pipeline credentials.
- **Leader — Learn:** A concrete incident narrative illustrating the risk of ungoverned AI agent access to production systems; useful context for setting policy on AI tooling permissions before broader rollout.
