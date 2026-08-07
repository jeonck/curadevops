---
title: "jc-rs: Rust static binary for converting CLI output to JSON (98 ★)"
date: 2026-08-07T11:39:24.969027+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["cli-tooling", "rust", "json-parsing"]
cves: []
source: "https://github.com/OlegSotnikov/jc-rs"
source_name: "GitHub Trending"
status: "active"
---
- **Platform/SRE — Learn:** A no-runtime static binary parsing 237 command formats into JSON is genuinely useful for minimal container images and infrastructure automation scripts — worth evaluating as a drop-in where Python-based jc adds runtime overhead.
- **CI/CD — Learn:** Could simplify pipeline scripts that need structured output from system commands without pulling in a Python runtime; evaluate against existing jc or jq-based approaches before adopting.
- **Leader — Skip**
