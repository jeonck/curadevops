---
title: "AWS Lambda public preview: managed runtimes for Node.js 26 and Python 3.15"
date: 2026-08-26T11:21:00.410731+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["lambda", "aws", "runtime"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-lambda-node-js-python-public-preview/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Learn:** AWS's new preview model lets platform teams validate Lambda workloads against upcoming runtimes before GA; pre-GA and explicitly unsupported for production, so evaluate only in non-critical environments.
- **CI/CD — Learn:** Notable design detail: preview runtimes use the same identifier as the eventual GA release, so Lambda functions automatically graduate with no pipeline or IaC changes required — worth factoring into future Lambda deployment workflows once GA.
- **Leader — Skip**
- **Signals:** pre-GA (alpha/beta/RC/preview) · breaking-change flagged
