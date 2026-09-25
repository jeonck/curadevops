---
title: "Amazon SageMaker HyperPod Inference Gateway GA on EKS"
date: 2026-09-25T15:41:44.461559+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["kubernetes", "llm-inference", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-hyperpod-inference-gateway/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** A new GA EKS managed add-on that replaces round-robin LB with real-time GPU-signal-aware routing (KV cache, queue depth, LoRA residency) for HyperPod clusters — evaluate adopting this quarter if your team runs SageMaker HyperPod inference workloads on EKS.
- **CI/CD — Skip**
- **Leader — Learn:** AWS's inference gateway pattern (single endpoint, multi-model routing, hardware-aware scheduling) signals a maturing managed alternative to self-built vLLM fleet management — worth tracking as it informs the build-vs-buy framing for LLM serving infrastructure.
