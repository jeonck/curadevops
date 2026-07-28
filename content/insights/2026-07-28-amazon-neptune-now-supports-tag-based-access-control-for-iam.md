---
title: "Amazon Neptune adds tag-based IAM access control (TBAC)"
date: 2026-07-28T12:49:37.470724+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["amazon-neptune", "iam", "access-control"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-neptune-tbac/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA Neptune capability that replaces static ARN enumeration in IAM policies with attribute-based cluster access using resource and principal tags; plan to adopt TBAC if you operate multiple Neptune clusters in shared VPC environments to enforce team and environment isolation.
- **CI/CD — Skip**
- **Leader — Learn:** Neptune now supports attribute-based access governance across clusters via IAM tags, useful context for organizations running Neptune at scale, but no strategic, licensing, or cost decision is triggered.
