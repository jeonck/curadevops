---
title: "Docker: AI coding agents can execute attacker code via pre-approved commands"
date: 2026-08-19T11:17:39.309563+00:00
verdict: "Learn"
verdict_platform: "Skip"
verdict_cicd: "Learn"
verdict_leader: "Learn"
tags: ["ai-agents", "supply-chain-security", "sandboxing"]
cves: []
source: "https://www.docker.com/blog/coding-agent-horror-stories-the-command-you-already-approved/"
source_name: "Docker Blog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Learn:** Illustrates a prompt-injection attack vector where malicious repo content hijacks an AI agent's pre-approved command scope; informs how to think about sandboxing agent-assisted pipeline steps, but no deadline or active exploit anchor.
- **Leader — Learn:** Useful framing for setting policy on where and how AI coding agents are permitted to run in the development workflow, particularly around isolation boundaries — but no decision is forced today.
