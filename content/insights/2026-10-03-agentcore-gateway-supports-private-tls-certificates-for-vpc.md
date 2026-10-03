---
title: "AgentCore Gateway adds private CA TLS support for VPC endpoints"
date: 2026-10-03T15:01:20.079187+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["bedrock", "vpc-lattice", "tls"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-gateway-private-tls-vpc/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Learn:** For teams operating Bedrock AgentCore workloads, this eliminates the need for an intermediate ALB when connecting to private VPC Lattice endpoints — worth evaluating if you're building that architecture, but no change required to existing infrastructure.
- **CI/CD — Skip**
- **Leader — Learn:** AWS is deepening native private-network integration for Bedrock's agent layer; useful context if your org is standardizing on AgentCore for AI agent workloads and evaluating VPC connectivity patterns, but no strategic decision is forced.
