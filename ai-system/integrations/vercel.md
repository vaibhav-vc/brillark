# Vercel

**Source of truth for:** Deployment state, build and runtime logs, and web analytics.

**Primary agents:** `infra-devops-agent`, `release-manager`, `performance-engineer`, `observability-agent`

## Rules

- Deployment is decoupled from release via flags, so exposure is a business decision rather than a deployment event.
- Runtime logs and errors feed incident response; they are evidence, not conclusions.
- Web analytics feed the funnel model. Reconcile against the product's own instrumentation before trusting either.
- A rollback must be verified before the release, not attempted during the incident.

## Contract

Read access is default. Writes are outward-facing actions requiring the owning agent's authority.
Everything entering memory from here carries provenance (system, query, timestamp) and an evidence
grade. If this system is unreachable, escalate — do not fall back to stale memory.
