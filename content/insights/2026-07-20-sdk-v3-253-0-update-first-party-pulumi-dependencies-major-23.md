---
title: "Pulumi SDK v3.253.0: major bumps to actions v7 and install-cli v2"
date: 2026-07-20T14:01:18.449662+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["pulumi", "github-actions", "iac"]
cves: []
source: "https://github.com/pulumi/pulumi/releases/tag/sdk%2Fv3.253.0"
source_name: "Releases: pulumi"
status: "archived"
---
- **Platform/SRE — Plan:** If your pipelines use pulumi/actions or pulumi/action-install-pulumi-cli, both have major version bumps (v6→v7, v1→v2) that likely include breaking changes; audit your workflow files and update action refs this quarter.
- **CI/CD — Plan:** pulumi/actions jumped v6→v7 and pulumi/action-install-pulumi-cli jumped v1→v2 — major bumps that may break existing pipeline steps; review release notes for both actions and update workflow references before Renovate auto-merges cause unexpected failures.
- **Leader — Skip**
