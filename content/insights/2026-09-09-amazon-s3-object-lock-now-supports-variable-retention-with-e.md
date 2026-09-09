---
title: "Amazon S3 Object Lock adds event-triggered variable retention holds"
date: 2026-09-09T14:56:08.335953+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["s3", "object-lock", "compliance"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-s3-object-lock-variable-retention/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA S3 Object Lock capability lets you anchor WORM retention to a future event (contract close, audit complete) rather than a fixed date — relevant for platform teams managing compliant storage under SEC 17a-4(f), FINRA 4511, or CFTC 1.31. Evaluate updating your S3 bucket policies and IAM condition keys to adopt event holds for regulated data this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** If the org operates in regulated industries, this Cohasset-assessed S3 capability closes a gap in event-driven retention compliance at no additional cost — useful context for understanding your AWS compliance posture, but no strategic decision or budget action required.
