---
title: "CodeQL build tracing breaks on macOS 27 due to dropped x86_64 binaries"
date: 2026-10-19T17:18:05.239721+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["codeql", "swift", "github-actions"]
cves: []
source: "https://github.blog/changelog/2026-10-19-codeql-changes-for-macos-27-xcode-27-and-swift-6-4"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** Teams running CodeQL on Swift projects will need to update their scanning configuration when adopting macOS 27 or Xcode 27 runners, as Apple has removed Intel x86_64 code from system binaries CodeQL depends on for build tracing. No forced deadline, but plan this alongside any macOS 27 runner migration.
- **Leader — Skip**
