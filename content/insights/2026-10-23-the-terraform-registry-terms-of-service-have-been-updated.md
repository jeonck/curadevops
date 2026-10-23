---
title: "Terraform Registry Terms of Service updated, restricting usage"
date: 2026-10-23T15:33:11.401461+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Plan"
tags: ["terraform", "iac", "vendor-risk"]
cves: []
source: "https://github.com/opentffoundation/roadmap/issues/24#issuecomment-1699535216"
source_name: "HN (terraform)"
status: "active"
---
- **Platform/SRE — Plan:** Platform teams pulling providers and modules from the public Terraform Registry are subject to the revised ToS; review the updated terms and evaluate whether to implement a provider network mirror or private registry to ensure automated and commercial usage remains compliant.
- **CI/CD — Plan:** CI pipelines that run `terraform init` against the public registry are exposed to ToS restrictions on automated usage; audit pipeline patterns and consider mirroring providers or switching to the OpenTofu registry to keep builds compliant.
- **Leader — Plan:** This ToS change compounds the earlier BSL relicensing as a vendor-risk signal for orgs standardized on Terraform; use this moment to formally evaluate OpenTofu as the org's IaC standard and assess whether current Registry usage complies with the new terms before the next planning cycle.
