---
title: "Amazon EC2 T8i burstable instances now generally available"
date: 2026-09-18T14:42:50.222201+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Learn"
verdict_leader: "Plan"
tags: ["ec2", "aws", "cost-optimization"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/ec2-t8i-instances-ga/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** T8i instances offer up to 30% better price performance than T3 with the same CPU credit model, making them a straightforward drop-in upgrade for burstable workloads like small databases, ingress gateways, or low-traffic internal services; evaluate swapping T3 instances this quarter to reduce compute TCO.
- **CI/CD — Learn:** T8i instances are explicitly called out as suitable for CI/CD pipelines and could reduce runner costs compared to T3, but no pipeline migration is required — worth noting if self-hosted runners are being right-sized.
- **Leader — Plan:** T8i delivers up to 30% better price performance over T3 with no migration complexity due to compatible CPU credit mechanics; flag this for the next FinOps review as a low-effort TCO reduction for burstable workload fleets.
- **Signals:** GA announcement
