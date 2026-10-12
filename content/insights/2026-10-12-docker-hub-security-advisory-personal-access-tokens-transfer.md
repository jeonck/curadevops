---
title: "Docker Hub CVE: PATs transferred during account-to-org conversions"
date: 2026-10-12T20:04:11.786944+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["docker-hub", "security", "credentials"]
cves: ["CVE-2026-105445"]
source: "https://www.docker.com/blog/docker-hub-security-advisory-cve-2026-105445/"
source_name: "Docker Blog"
status: "active"
---
- **Platform/SRE — Plan:** If any Docker Hub personal accounts were converted to organizations in your org, PATs used for image pulls in infrastructure tooling may have been re-assigned to unintended owners. Audit and rotate affected Docker Hub PATs; no hard deadline but treat as a near-term security hygiene task.
- **CI/CD — Plan:** Docker Hub PATs are widely embedded in CI/CD pipelines for registry auth; if any team converted a personal Docker Hub account to an org, those tokens may have changed hands. Identify any converted accounts and rotate all associated PATs in pipeline secrets before they can be leveraged.
- **Leader — Skip**
- **Signals:** CVE-2026-105445 — CISA KEV: not listed, EPSS n/a
