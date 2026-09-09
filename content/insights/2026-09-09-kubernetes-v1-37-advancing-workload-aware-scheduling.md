---
title: "Kubernetes v1.37 graduates gang scheduling and WAS APIs to Beta"
date: 2026-09-09T14:56:08.335953+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["kubernetes", "scheduling", "ai-ml"]
cves: []
source: "https://kubernetes.io/blog/2026/09/08/kubernetes-v1-37-advancing-workload-aware-scheduling/"
source_name: "Kubernetes Blog"
status: "active"
---
- **Platform/SRE — Learn:** Kubernetes 1.37 is a GA minor release (EOL 2027-10-28) with no urgent upgrade pressure, and its headline features — gang scheduling, Workload-Aware Preemption, CompositePodGroup — are Beta or newly introduced, capping this at Learn. Worth tracking for teams running AI/ML or large batch workloads on Kubernetes as these APIs stabilize toward GA.
- **CI/CD — Skip**
- **Leader — Learn:** The maturing Workload-Aware Scheduling APIs (gang scheduling, hierarchical PodGroups) signal that upstream Kubernetes is building native primitives for AI/ML batch infrastructure that previously required external schedulers — worth incorporating into the AI/ML platform strategy roadmap as these graduate to GA.
- **Signals:** Kubernetes 1.37 EOL 2027-10-28
