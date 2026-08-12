---
title: "AWS Secrets Manager adds managed rotation for Jenkins and SonarQube tokens"
date: 2026-08-12T11:40:52.953542+00:00
verdict: "Plan"
verdict_platform: "Learn"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["secrets-management", "jenkins", "sonarqube"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/secrets-manager-integration-jenkins-sonarqube/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Learn:** New GA capability for automating credential rotation without custom code; worth knowing for teams already using Secrets Manager managed external secrets, but no operational urgency.
- **CI/CD — Plan:** Teams using Jenkins or SonarQube with AWS Secrets Manager can now automate token rotation natively — schedule evaluation and adoption to reduce manual credential lifecycle work and lower the risk of stale tokens in pipelines.
- **Leader — Skip**
