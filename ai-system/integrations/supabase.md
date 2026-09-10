# Supabase

**Source of truth for:** Application data, authentication, and the usage events that billing and analytics depend on.

**Primary agents:** `data-model-designer`, `backend-implementation-agent`, `chief-data-officer-agent`, `data-protection-officer-agent`

## Rules

- Schema changes go through `migration-planning`: reversible, backwards compatible, tested at production-shaped volume.
- Every field carries a privacy classification before it exists. `data-protection-officer-agent` blocks unclassified fields.
- Metering events are the billable source of truth. Their definition is owned by `billing-systems-designer` and changing it is a decision record, not a code change.
- Never copy production personal data into a test environment.

## Contract

Read access is default. Writes are outward-facing actions requiring the owning agent's authority.
Everything entering memory from here carries provenance (system, query, timestamp) and an evidence
grade. If this system is unreachable, escalate — do not fall back to stale memory.
