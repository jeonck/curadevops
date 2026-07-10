# Persona: Platform / SRE Engineer

## Who this is
The engineer who **operates** the shared infrastructure other teams build on and
is on the hook when it breaks. Typical titles: SRE, Platform Engineer,
Infrastructure Engineer, Cloud Engineer. They hold the pager. They own the
Kubernetes clusters, the cloud accounts, the service mesh, the observability
stack, and the internal platform (IDP) that application teams consume. When a
component reaches end-of-life or a control plane starts throwing errors, it is
their weekend.

## Environment assumptions
- Runs production workloads on at least one major cloud (AWS/Azure/GCP), usually
  on managed Kubernetes (EKS/GKE/AKS) or a self-managed cluster.
- Owns long-lived, stateful, hard-to-change infrastructure: control planes,
  node pools, ingress/load balancers, DNS, service mesh (Istio/Linkerd),
  secrets management (Vault), and the observability pipeline
  (Prometheus/Grafana/OpenTelemetry/Loki).
- Manages that infrastructure as code — Terraform/OpenTofu, Pulumi, Crossplane,
  Helm charts, Kustomize — and cares about provider/version drift.
- Lives with **version-skew and EOL constraints**: Kubernetes supports only the
  last ~3 minor versions; managed clouds force-upgrade clusters on a schedule.
- Upgrade windows are measured in weeks of planning for anything touching the
  control plane or a stateful data path; hotfixes for an active outage in hours.

## What they must decide from each item
"Does this touch infrastructure I **run in production**, and does it force me to
upgrade, migrate, reconfigure, or add monitoring — and on what deadline?"

## Verdict criteria
- **Act** — something they operate is on a clock or actively failing. Concrete signals:
  - a **hard EOL / forced-upgrade / removal date** for a version or API they run
    (e.g. a Kubernetes API removed in the next minor, a managed-service version
    deprecation, a cloud legacy-auth shutdown) — the date is the anchor;
  - a security fix (KEV-listed / active exploitation / public PoC) in
    infrastructure software they operate — control plane, ingress, mesh, Vault,
    a container runtime, a CNI plugin;
  - a released regression / data-loss / availability bug in a version they are
    likely running now.
  The note must name the action **and** the deadline: "upgrade EKS to 1.xx before
  <date>", "migrate off the removed `policy/v1beta1` API", "patch ingress-nginx
  to x.y.z".
- **Plan** — real exposure to their platform but no clock ticking yet: a new
  **GA** release worth adopting this quarter; an *announced but not-yet-enforced*
  deprecation with a distant date; a migration (e.g. Terraform→OpenTofu, a mesh
  upgrade) that needs a project, not a hotfix; a new managed-service capability
  that changes how they'd architect the platform.
- **Learn** — changes how they'd **design** infrastructure but requires no change
  to what's running: a new operator/pattern, a scaling or reliability post-mortem,
  a tool in beta/alpha worth evaluating, a benchmark. Anything not yet GA lands
  here, not in Act/Plan.
- **Skip** — a release in software they almost certainly don't operate; a purely
  application-developer-facing feature with no platform surface; vendor marketing;
  a re-announcement with no new version, date, or fix.

## What they do NOT care about (do not inflate verdicts for these)
- Application-framework / language-SDK releases with no infra footprint (that is
  the app teams' concern, not the platform's).
- CI/CD pipeline mechanics — build caching, runner config, release orchestration
  — unless the CI system itself runs *on their cluster* (that's the CI/CD persona).
- Pre-GA experiments and "we're exploring X" vendor blog posts — those are Learn
  at most, never Act.
- Strategy / cost / vendor-selection framing with no operational control to change
  (that's the Leader).
