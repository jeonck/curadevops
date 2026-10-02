---
title: "ConfigPoisoning in DeepSeek-Reasonix Studio: git config can exec attacker code"
date: 2026-10-02T16:25:37.540030+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Learn"
verdict_leader: "Plan"
tags: ["supply-chain", "security", "ai-coding-agents"]
cves: ["CVE-2026-102437"]
source: "https://about.gitlab.com/blog/deepseek-reasonix-vulnerability-discovered/"
source_name: "GitLab Blog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Learn:** The ConfigPoisoning class — attacker-controlled execution via .git/config and .gitattributes — is worth understanding when hardening pipelines that clone external or untrusted repos; the specific exploit requires the DeepSeek-Reasonix desktop client, but GitLab notes multiple coding agents share the same root flaw.
- **Leader — Plan:** GitLab's research found the ConfigPoisoning class affects multiple widely-used AI coding agents, not just DeepSeek-Reasonix; if the org is standardizing on AI coding assistants, add security vetting of approved tools to the golden-path policy before broad rollout.
- **Signals:** CVE-2026-102437 — CISA KEV: not listed, EPSS 0.01
