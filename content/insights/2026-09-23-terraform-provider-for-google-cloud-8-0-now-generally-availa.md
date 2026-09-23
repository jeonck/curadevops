---
title: "Terraform Google Cloud Provider 8.0 GA: breaking changes and removed services"
date: 2026-09-23T15:14:55.611695+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["terraform", "google-cloud", "infrastructure-as-code"]
cves: []
source: "https://www.hashicorp.com/blog/terraform-provider-for-google-cloud-80-now-generally-available"
source_name: "HashiCorp Blog"
status: "active"
---
- **Platform/SRE — Plan:** A semver-major release that removes retired GCP service resources and changes provider defaults — teams running GCP workloads via Terraform should plan a version pin audit and config migration before upgrading, as breaking changes will surface at apply time. No forced deadline exists, but deferring widens the upgrade gap.
- **CI/CD — Skip**
- **Leader — Skip**
- **Signals:** deprecation mentioned (no explicit date found) · GA announcement · major release (8.0)
