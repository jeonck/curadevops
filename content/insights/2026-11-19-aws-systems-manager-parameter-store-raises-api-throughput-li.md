---
title: "AWS SSM Parameter Store raises API throughput limits by 5×"
date: 2026-11-19T19:16:29.978589+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws", "ssm", "configuration-management"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/parameter-store-raises-api-throughput-limits/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Learn:** Parameter Store throughput limits have already been raised (e.g., GetParametersByPath now 500 TPS), so this updates what the service can handle at scale — worth revisiting any throttle-mitigation workarounds in IaC or Lambda config-loading patterns, but no deadline or breaking change triggers action now.
- **CI/CD — Skip**
- **Leader — Skip**
