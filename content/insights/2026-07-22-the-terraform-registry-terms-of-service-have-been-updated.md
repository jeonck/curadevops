---
title: "Terraform Registry Terms of Service Updated"
date: 2026-07-22T12:23:02.611708+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Learn"
verdict_leader: "Plan"
tags: ["terraform", "licensing", "vendor-risk"]
cves: []
source: "https://github.com/opentffoundation/roadmap/issues/24#issuecomment-1699535216"
source_name: "HN (terraform)"
status: "archived"
---
- **Platform/SRE — Plan:** The updated ToS may restrict how the Terraform Registry can be consumed, particularly by tooling or automation that competes with or mirrors registry content. Review current Terraform and provider-download patterns against the new terms and evaluate whether a migration to OpenTofu or a self-hosted registry should be scoped this quarter.
- **CI/CD — Learn:** Pipelines that pull Terraform providers and modules via the public registry could be indirectly affected if the new ToS introduces usage restrictions on automated clients; worth monitoring, but no concrete pipeline action is required yet.
- **Leader — Plan:** A ToS change on a registry that most Terraform-standardized orgs depend on is a direct vendor-risk signal; evaluate whether current registry consumption falls under any newly restricted terms and assess OpenTofu as a contingency before any enforcement timeline is announced.
