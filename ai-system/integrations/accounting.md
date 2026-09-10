# Accounting and billing

**Source of truth for:** Financial actuals: revenue recognised, cash, spend, and the ledger.

**Primary agents:** `cfo-agent`, `finance-head`, `burn-runway-analyst`, `billing-systems-designer`, `tax-and-compliance-finance`

## Rules

- The ledger is authoritative for actuals. The model is authoritative for nothing — it is reconciled *to* the ledger, and when they disagree the model is what gets fixed.
- Cash balance is confirmed at the bank, not read from the ledger, before any runway calculation.
- Billing-to-ledger reconciliation is automated and alarms on drift.
- No figure leaves the building without passing `figure-reconciliation`.

## Contract

Read access is default. Writes are outward-facing actions requiring the owning agent's authority.
Everything entering memory from here carries provenance (system, query, timestamp) and an evidence
grade. If this system is unreachable, escalate — do not fall back to stale memory.
