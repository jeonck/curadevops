---
title: "Amazon S3 adds PrivateLink support for FIPS 140-3 endpoints"
date: 2026-09-04T14:38:54.847255+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-s3", "fips-compliance", "privatelink"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-s3-privatelink-fips-endpoints"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability lets platform teams route FIPS-validated S3 traffic entirely within the VPC — actionable for teams running regulated or federal workloads; schedule a review of existing VPC endpoint configs and update to the FIPS S3 endpoint where compliance requires it.
- **CI/CD — Skip**
- **Leader — Learn:** Useful signal for leaders with federal or regulated customers — AWS now offers a path to keep S3 traffic VPC-internal under FIPS 140-3, which may simplify future compliance audits or contract negotiations with government clients.
