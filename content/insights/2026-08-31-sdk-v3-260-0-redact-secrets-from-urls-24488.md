---
title: "Pulumi SDK v3.260.0: redact URL secrets from logs"
date: 2026-08-31T18:45:38.217891+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["pulumi", "secrets", "iac"]
cves: []
source: "https://github.com/pulumi/pulumi/releases/tag/sdk%2Fv3.260.0"
source_name: "Releases: pulumi"
status: "active"
---
- **Platform/SRE — Plan:** If you use Pulumi with connection-string URLs (e.g. Postgres), upgrade to sdk/v3.260.0 to prevent passwords leaking into state/log output; no hard deadline but a meaningful security hygiene improvement.
- **CI/CD — Skip**
- **Leader — Skip**
