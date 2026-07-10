# Persona: CI/CD & Release Engineer

## Who this is
The engineer who owns how code goes from a commit to production: the pipelines,
the build system, the artifact supply chain, and the release process. Typical
titles: Release Engineer, Build Engineer, DevOps Engineer (pipeline-focused),
Developer Experience / Developer Productivity Engineer. They are measured by
build speed, pipeline reliability, and whether releases ship safely. When a
runner image changes, an action is deprecated, or an artifact registry changes
auth, **their pipelines turn red for every team at once**.

## Environment assumptions
- Owns pipelines on at least one CI/CD system: GitHub Actions, GitLab CI,
  Jenkins, CircleCI, Buildkite, Argo Workflows, or Tekton — often more than one.
- Owns the **software supply chain**: package registries (npm/PyPI/Maven/Go
  proxy), container registries (GHCR/ECR/Artifactory/Harbor), base images,
  dependency pinning/lockfiles, and increasingly SBOM / provenance / signing
  (Sigstore/cosign, SLSA).
- Owns deployment mechanics downstream of build: GitOps (Argo CD/Flux),
  progressive delivery (canary/blue-green), release automation, feature flags.
- Cares deeply about **pinned versions and reproducibility** — a silently updated
  action, runner, or base image breaking a build is their top pain.
- Fix window: a broken pipeline blocking all merges is effectively an outage
  (hours); a deprecation with a migration deadline is a planned project.

## What they must decide from each item
"Does this change how builds, tests, artifacts, or deployments **execute** — do I
need to pin, migrate, re-sign, or rewrite a pipeline, and how soon?"

## Verdict criteria
- **Act** — something in the build/release path is breaking or on a hard clock:
  - a CI/CD platform **deprecation or removal with a date** (a runner image
    retirement, an Actions/GitLab feature sunset, a required-version bump, a
    Node/runtime EOL in the runner) that will red-line pipelines;
  - a **supply-chain compromise** — a malicious/backdoored package, a poisoned
    popular action, a registry/token leak — requiring an audit or credential
    rotation in build logs *now*;
  - a security fix (KEV / active exploitation / public PoC) in a CI system,
    runner, registry, or build tool they run.
  The note must name the action and deadline: "pin actions/x to a SHA before the
  <date> runner change", "rotate registry tokens, audit builds for package Y",
  "upgrade the Jenkins controller to patch CVE-…".
- **Plan** — real relevance to the pipeline, no clock yet: a new **GA** CI feature
  or build-cache/remote-execution capability worth adopting; a supply-chain
  hardening step to schedule (adopt SBOM, enable provenance/signing, move to
  pinned digests); an *announced* deprecation with a distant date; a migration
  between CI systems or to GitOps as a project.
- **Learn** — changes how they'd **design** pipelines but nothing to change today:
  new release patterns, a DevEx/build-speed post-mortem, a beta tool to evaluate,
  emerging supply-chain standards not yet actionable.
- **Skip** — infra-only operational news with no build/release surface (that's
  Platform); pure app-framework releases; vendor marketing; re-announcements with
  no new deprecation, version, or fix.

## What they do NOT care about (do not inflate verdicts for these)
- Cluster/infrastructure operations — node pools, mesh, ingress, observability —
  unless the CI system or artifact store *runs on* that infra in a way that
  changes pipelines (otherwise it's Platform).
- Runtime/production incidents that don't originate in the build or deploy path.
- Toolchain **strategy and cost** decisions with no concrete pipeline change to
  make (that's the Leader).
- Pre-GA / experimental features — Learn at most, never Act.
