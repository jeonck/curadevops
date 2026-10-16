---
title: "Oracle Database@AWS ODB peering adds aggregate and default route support"
date: 2026-10-16T15:05:37.577214+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["oracle-database-aws", "vpc-peering", "networking"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/oracle-database-aws-aggregate-routes-odb/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If you run Oracle Database@AWS, this new GA capability lets you advertise a single aggregate CIDR or default route (0.0.0.0/0) over ODB peering instead of managing per-network entries — worth updating your ODB network peering config during your next network ops review cycle.
- **CI/CD — Skip**
- **Leader — Skip**
