---
title: "Amazon MSK Connect adds pause/resume for connectors (GA)"
date: 2026-10-24T14:11:23.013433+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["managed-kafka", "aws-msk", "platform-ops"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-connect-pause-resume"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If you run MSK Connect, update your maintenance runbooks to use pause/resume instead of delete/recreate — this preserves offsets and config, reducing risk during source/sink maintenance windows. No deadline; schedule adoption this quarter.
- **CI/CD — Skip**
- **Leader — Skip**
