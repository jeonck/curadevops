---
title: "HCP SCIM provisioning GA for automated identity lifecycle management"
date: 2026-08-27T20:52:16.263478+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["hashicorp", "identity", "scim"]
cves: []
source: "https://www.hashicorp.com/blog/streamline-identity-lifecycle-management-on-hcp-with-scim-provisioning"
source_name: "HashiCorp Blog"
status: "active"
---
- **Platform/SRE — Plan:** If your org uses HCP (Vault, Terraform Cloud, etc.) and an external IdP, evaluate enabling SCIM provisioning to automate user/group sync and reduce manual access management overhead; no deadline, but worth scheduling this quarter.
- **CI/CD — Skip**
- **Leader — Plan:** SCIM provisioning on HCP reduces IAM admin overhead and improves access consistency across HCP services — worth adding to your identity governance standards review if the org is standardized on HashiCorp HCP.
