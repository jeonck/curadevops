---
title: "Critical RCE (CVSS 10.0) in vm2 Node.js sandbox, patched in 3.11.7"
date: 2026-09-03T14:50:54.558994+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["security", "nodejs", "supply-chain"]
cves: []
source: "https://about.gitlab.com/blog/critical-remote-code-execution-in-vm2/"
source_name: "GitLab Blog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** Audit build scripts, custom GitHub Actions, and any Node.js-based pipeline tooling for vm2 usage; if found, update to 3.11.7 and disable require.external — the blog post describes a working exploit path (CVSS 10.0), so exposure is concrete even without a KEV entry. No forced deadline, but the publicly documented exploit makes this a near-term project, not a watch item.
- **Leader — Skip**
