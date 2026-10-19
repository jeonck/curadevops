---
title: "Terraform module for scalable GitHub Actions runners on AWS"
date: 2026-10-19T17:18:05.239721+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["github-actions", "terraform", "aws"]
cves: []
source: "https://github.com/philips-labs/terraform-aws-github-runner"
source_name: "HN (terraform)"
status: "active"
---
- **Platform/SRE — Plan:** This open-source module automates ephemeral, auto-scaling GitHub Actions runner fleets on AWS via Terraform — worth evaluating if the org self-hosts runners on EKS or EC2 and wants to reduce idle capacity costs.
- **CI/CD — Plan:** Teams running self-hosted GitHub Actions runners on AWS should evaluate this module to gain on-demand ephemeral runners and eliminate persistent runner maintenance overhead; no deadline, but a useful near-term adoption candidate.
- **Leader — Skip**
