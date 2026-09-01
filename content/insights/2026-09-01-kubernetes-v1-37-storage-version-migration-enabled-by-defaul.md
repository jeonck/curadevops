---
title: "Kubernetes v1.37: Storage Version Migration graduates to GA"
date: 2026-09-01T15:20:27.675053+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["kubernetes", "storage-migration", "crd-lifecycle"]
cves: []
source: "https://kubernetes.io/blog/2026/08/31/kubernetes-v1-37-storage-version-migration-ga/"
source_name: "Kubernetes Blog"
status: "active"
---
- **Platform/SRE — Plan:** StorageVersionMigration API (storagemigration.k8s.io/v1) is now stable and enabled by default in Kubernetes 1.37, removing the need for manual migration scripts when promoting or dropping CRD API versions. Plan to incorporate SVM into your CRD lifecycle runbooks when scheduling the upgrade to 1.37 (EOL 2027-10-28).
- **CI/CD — Skip**
- **Leader — Skip**
- **Signals:** Kubernetes 1.37 EOL 2027-10-28 · GA announcement
