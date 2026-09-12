---
title: "Amazon SageMaker HyperPod adds model caching to cut LLM inference cold starts"
date: 2026-09-12T13:49:10.028623+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws", "llm-inference", "autoscaling"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/sgm-hyperpod-model-caching-inf/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If you run LLM inference workloads on SageMaker HyperPod, this GA feature cuts scale-out time ~60% by pre-loading model weights to NVMe and pre-pulling container images; evaluate adding a modelCacheConfig block to InferenceEndpointConfig resources this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** HyperPod's new model caching substantially narrows the cold-start penalty for large-model inference, which is relevant context if evaluating HyperPod as the org's managed inference platform versus self-managed alternatives.
