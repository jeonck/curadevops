---
title: "GitHub CLI Linux package signing key expires September 5"
date: 2026-09-04T14:38:54.847255+00:00
verdict: "Act"
verdict_platform: "Act"
verdict_cicd: "Act"
verdict_leader: "Skip"
tags: ["github-cli", "package-signing", "linux"]
cves: []
source: "https://github.blog/changelog/2026-09-03-github-cli-linux-package-signing-key-expires-september-5"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Act:** The PGP signing key for GitHub CLI APT/RPM repos expires 2026-09-05; any managed Linux host that auto-installs or updates `gh` via apt/rpm will fail package-signature verification on the first release after that date. Update the trusted keyring on those hosts today.
- **CI/CD — Act:** Pipelines that install `gh` on Linux runners via apt or rpm will break signature verification starting with the first release after 2026-09-05; update the keyring import step in CI configs, runner setup scripts, or Dockerfiles immediately to add the new PGP key before pipelines go red.
- **Leader — Skip**
