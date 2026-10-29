---
title: "Amazon EKS Dashboard adds fleet-wide CA rotation visibility"
date: 2026-10-29T17:12:51.882644+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["eks", "certificate-management", "platform-ops"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-eks-dashboard-fleet-wide-visibility-certificate-authority-ca-rotation/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Enable EKS Dashboard trusted access via AWS Organizations to get consolidated CA rotation status across all clusters and regions — clusters created since 2018 carry 10-year CAs that are now entering the window where rotation planning should begin. No hard expiration deadline is cited, but this is a free GA capability worth enabling this quarter to surface clusters approaching rotation.
- **CI/CD — Skip**
- **Leader — Skip**
