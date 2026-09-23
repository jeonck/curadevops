---
title: "GitHub removing legacy SSH algorithms, requiring larger RSA keys"
date: 2026-09-23T15:14:55.611695+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["ssh-security", "github", "supply-chain"]
cves: []
source: "https://github.blog/changelog/2026-09-22-security-improvements-for-ssh"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Plan:** Review any SSH keys used for infrastructure automation against GitHub repos (deploy keys, Ansible/Terraform git sources) to confirm they meet the new algorithm and minimum RSA key-size requirements before the removals take effect; no hard deadline is published yet.
- **CI/CD — Plan:** Audit SSH deploy keys and runner SSH credentials used to pull private repos or push artifacts via GitHub to ensure they use accepted algorithms and sufficiently large RSA keys; schedule rotation for any that don't comply before the removal lands.
- **Leader — Skip**
