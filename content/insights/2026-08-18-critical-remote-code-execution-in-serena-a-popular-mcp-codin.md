---
title: "Critical RCE in Serena MCP coding agent — update to 1.7.0"
date: 2026-08-18T11:17:30.179155+00:00
verdict: "Act"
verdict_platform: "Skip"
verdict_cicd: "Act"
verdict_leader: "Plan"
tags: ["mcp-security", "rce", "ai-coding-agent"]
cves: []
source: "https://about.gitlab.com/blog/critical-rce-in-serena/"
source_name: "GitLab Blog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Act:** Published GHSA-pp25-4cg4-qcr9 details a critical server-side template injection in serena-agent ≤1.6.1 that executes arbitrary code via a malicious .serena/project.yml smuggled in any cloned repo — a direct supply-chain threat to developer and CI environments; upgrade to serena-agent 1.7.0 now.
- **Leader — Plan:** This is an early, documented example of a new risk class: MCP servers embedded in the SDL grant LLMs broad filesystem and shell access, making any compromise severe; evaluate whether your AI coding-agent adoption policies explicitly address this attack surface before broader org rollout.
