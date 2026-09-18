---
title: "HCP Vagrant deprecated: migration required in 2026"
date: 2026-09-18T14:42:50.222201+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["vagrant", "hashicorp", "deprecation"]
cves: []
source: "https://www.hashicorp.com/blog/hcp-vagrant-deprecation-important-dates-and-migration-guidance"
source_name: "HashiCorp Blog"
status: "active"
---
- **Platform/SRE — Plan:** Teams hosting or consuming Vagrant boxes via HCP should identify an alternative registry (self-hosted or otherwise) and plan migration before HCP Vagrant shuts down; no specific cutoff date is published yet, so treat this as a Q4 2026 planning item.
- **CI/CD — Skip**
- **Leader — Learn:** HashiCorp sunsetting HCP Vagrant signals continued consolidation of their cloud platform away from legacy VM-based dev tooling; worth noting if Vagrant is still part of the org's standard developer environment stack.
- **Signals:** deprecation mentioned (no explicit date found)
