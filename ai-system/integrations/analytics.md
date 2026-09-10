# Product analytics

**Source of truth for:** Product behaviour, funnel conversion, cohort retention, and experiment results.

**Primary agents:** `chief-data-officer-agent`, `revenue-forecaster`, `growth-loop-designer`, `customer-success-agent`

## Rules

- Every metric here must exist in the metric dictionary with one definition and one owner.
- Experiments are pre-registered: hypothesis, primary metric, threshold, and sample size before launch. A result from an unregistered experiment is `estimated` at best.
- Cohort retention, not blended churn, feeds LTV. Blended churn hides the thing you need to see.
- Report negative results with the same prominence as positive ones.

## Contract

Read access is default. Writes are outward-facing actions requiring the owning agent's authority.
Everything entering memory from here carries provenance (system, query, timestamp) and an evidence
grade. If this system is unreachable, escalate — do not fall back to stale memory.
