---
title: "GuardDuty RDS Protection adds ML-based data exfiltration and destruction detection"
date: 2026-10-09T17:15:30.772048+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["guardduty", "aws-security", "rds-protection"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/guardduty-rds-data-exfiltration/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability for Aurora PostgreSQL and RDS for PostgreSQL that detects post-credential-compromise data exfiltration and destruction with no agent or config changes required; platform teams running RDS/Aurora should evaluate enabling the add-on for their organization this quarter via the GuardDuty console or CloudFormation.
- **CI/CD — Skip**
- **Leader — Learn:** GuardDuty now extends RDS threat detection beyond login anomalies to query-pattern behavior using ML, relevant for understanding current AWS-native security coverage breadth — no strategic decision or policy change is immediately required.
