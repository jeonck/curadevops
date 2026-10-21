---
title: "AWS IAM Identity Center now preserves identities when migrating from AD"
date: 2026-10-21T15:46:15.304693+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-iam", "identity-management", "active-directory"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/iam-identity-center-chg-id-src-from-ad/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability removes a major operational barrier: migrating IAM Identity Center from Active Directory to an external IdP (Okta, Entra ID) no longer requires recreating users, groups, and permission assignments. If an AD-to-IdP identity migration is on the roadmap, schedule an evaluation of this simplified path.
- **CI/CD — Skip**
- **Leader — Learn:** This lowers the migration cost for orgs considering a shift from on-prem AD to a cloud IdP as their AWS identity source — a previously high-friction strategic move is now substantially simpler, which may shift the build-vs-buy calculus for identity infrastructure.
