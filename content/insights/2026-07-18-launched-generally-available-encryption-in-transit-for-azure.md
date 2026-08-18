---
title: "AKS: Encryption in Transit for Azure Files NFS v4.1 Now GA"
date: 2026-07-18T11:46:40.266258+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["azure-kubernetes-service", "storage-security", "encryption"]
cves: []
source: "https://azure.microsoft.com/updates?id=567787"
source_name: "Azure Updates"
status: "archived"
---
- **Platform/SRE — Plan:** A new GA security capability for AKS clusters using Azure Files NFS v4.1 volumes via the CSI driver — worth evaluating this quarter for workloads with data-in-transit compliance requirements. Review existing PersistentVolume configurations and enable EiT where encryption mandates apply.
- **CI/CD — Skip**
- **Leader — Learn:** This GA feature expands available encryption controls on AKS-backed storage, which may inform security standards or compliance posture for teams running NFS workloads on Azure, but no strategic decision is forced.
- **Signals:** GA announcement
