---
title: "Pulumi SDK v3.268.0 pins Maven to 3.9.x to fix broken pulumi-java downloads"
date: 2026-10-12T20:54:00.392514+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["pulumi", "java", "iac"]
cves: []
source: "https://github.com/pulumi/pulumi/releases/tag/sdk%2Fv3.268.0"
source_name: "Releases: pulumi"
status: "active"
---
- **Platform/SRE — Plan:** If you use pulumi-java with Maven 3.10, plugin downloads are silently broken because Maven 3.10 mixes log output into stdout and corrupts JSON parsing; upgrade to Pulumi SDK v3.268.0 to restore correct behavior while the upstream Maven bug is resolved.
- **CI/CD — Skip**
- **Leader — Skip**
