---
name: frontend-performance-budget
category: engineering
description: "Set and defend limits on what the client has to load and do."
output: "performance-budget.md"
used_by:
  - frontend-implementation-agent
---

# Frontend Performance Budget

`engineering` · produces `performance-budget.md` · used by `frontend-implementation-agent`

Set and defend limits on what the client has to load and do.

## Procedure
1. Set budgets for bundle size, time to interactive, and main-thread work.
2. Measure the current position against each budget.
3. Attribute the largest contributions to specific dependencies or code.
4. Enforce the budget in CI so regressions fail the build.
5. Review the budget when the target device or network profile changes.

## Output contract
`performance-budget.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Budget enforced in CI
- Largest contributors attributed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
