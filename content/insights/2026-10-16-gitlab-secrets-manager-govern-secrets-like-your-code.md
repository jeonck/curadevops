---
title: "GitLab Secrets Manager now GA in 19.5, built on OpenBao"
date: 2026-10-16T15:05:37.577214+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Learn"
tags: ["secrets-management", "gitlab", "supply-chain-security"]
cves: []
source: "https://about.gitlab.com/blog/secrets-manager-ga/"
source_name: "GitLab Blog"
status: "active"
---
- **Platform/SRE — Plan:** GitLab Secrets Manager is now GA in 19.5 Premium/Ultimate, built on OpenBao — evaluate whether it can replace a standalone Vault deployment for GitLab-centric orgs, since it reuses the existing GitLab permission model and eliminates the sync-drift problem between vault access and project membership.
- **CI/CD — Plan:** Now GA in GitLab 19.5 — schedule evaluation of Secrets Manager as a replacement for unscoped CI/CD variables; it scopes credentials to individual jobs and attaches pipeline and job IDs to every credential read, making this a concrete supply-chain hardening step for GitLab-hosted pipelines.
- **Leader — Learn:** For orgs standardized on GitLab, this GA release shifts the build-vs-buy calculus on maintaining a separate secrets vault; no urgent vendor or licensing decision, but worth tracking as a potential toolchain consolidation as the feature matures on Dedicated.
- **Signals:** GitLab 19.5 EOL 2027-01-21 · GA announcement
