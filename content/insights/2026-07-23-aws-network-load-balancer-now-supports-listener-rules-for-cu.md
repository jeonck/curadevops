---
title: "AWS NLB adds listener rules for IPv4/IPv6 source-based routing"
date: 2026-07-23T12:19:57.837621+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws", "network-load-balancer", "dual-stack"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-network-load-balancer-supports-listener-rules/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA NLB capability worth evaluating this quarter for teams running dual-stack workloads: a single NLB can now route IPv4 and IPv6 clients to same-family targets without protocol translation or a second load balancer. Audit existing dual-stack NLB deployments and update Terraform/IaC to add listener rules where protocol translation is currently causing IP preservation issues.
- **CI/CD — Skip**
- **Leader — Skip**
