---
title: "Amazon EKS adds managed CA rotation with automated lifecycle safeguards"
date: 2026-08-21T11:18:28.032860+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["eks", "kubernetes", "certificate-management"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-eks-certificate-authority-ca-rotation-automated-lifecycle-management"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** EKS clusters created in 2018 have 10-year CAs now approaching expiry (~2028); audit cluster creation dates and schedule CA rotation this quarter — worker nodes must be replaced and external API clients updated to trust the successor CA before activation, which AWS will not do automatically.
- **CI/CD — Learn:** Pipelines that connect directly to EKS API servers (kubectl, Helm deploys, kubeconfig-based auth) qualify as external clients under the shared-responsibility model and would need CA trust updates during any rotation; no immediate action required but worth noting when rotation is scheduled by Platform.
- **Leader — Skip**
