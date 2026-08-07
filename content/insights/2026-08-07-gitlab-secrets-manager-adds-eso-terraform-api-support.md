---
title: "GitLab Secrets Manager adds ESO, Terraform, and API support via OpenBao"
date: 2026-08-07T00:23:45.191261+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Learn"
verdict_leader: "Learn"
tags: ["secrets-management", "kubernetes", "gitlab"]
cves: []
source: "https://about.gitlab.com/blog/gitlab-secrets-manager-add-eso-terraform-api-support/"
source_name: "GitLab Blog"
status: "active"
---
- **Platform/SRE — Plan:** This GA expansion lets platform teams consolidate Kubernetes (ESO), Terraform/OpenTofu, and Vault CLI secrets into a single OpenBao-backed store — worth evaluating this quarter as a replacement for fragmented per-tool secret stores, with no forcing deadline yet.
- **CI/CD — Learn:** GitLab CI/CD secret support landed in v19.0 already; the new ESO and Terraform integrations are primarily platform-side — no pipeline changes required today, but the unified API surface is worth noting for future supply-chain design.
- **Leader — Learn:** The consolidated single-store model (one audit trail, one access model across Kubernetes, IaC, and pipelines) is worth tracking as a vendor-consolidation data point when revisiting secrets-toolchain standards, but no pricing or license forcing function exists yet.
