# CRM

**Source of truth for:** Pipeline, deal stages, customer relationships, and win/loss history.

**Primary agents:** `chief-revenue-officer-agent`, `sales-playbook-agent`, `customer-success-agent`, `partnership-bd-agent`

## Rules

- Stages are defined by observable buyer actions. If a stage means something different this week, the forecast is fiction.
- Win/loss reasons come from buyer interviews where possible — sellers and buyers give different accounts of the same deal.
- Lost-deal reasons route to product and marketing every cycle with evidence attached.
- Pipeline coverage feeds the revenue forecast; the forecast publishes its confidence interval.

## Contract

Read access is default. Writes are outward-facing actions requiring the owning agent's authority.
Everything entering memory from here carries provenance (system, query, timestamp) and an evidence
grade. If this system is unreachable, escalate — do not fall back to stale memory.
