---
name: frontend-performance-budget
category: engineering
description: "Set and defend limits on what the client has to load and do."
output: "performance-budget.md"
used_by:
  - frontend-implementation-agent
---

# Frontend Performance Budget

**Category:** `engineering` · **Output artifact:** `performance-budget.md`

## What this skill does
Set and defend limits on what the client has to load and do.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `frontend-implementation-agent`.

## Procedure
1. Set budgets for bundle size, time to interactive, and main-thread work.
2. Measure the current position against each budget.
3. Attribute the largest contributions to specific dependencies or code.
4. Enforce the budget in CI so regressions fail the build.
5. Review the budget when the target device or network profile changes.

## Output contract
Write `performance-budget.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** frontend-performance-budget
- **Author agent:** <agent-id>
- **Date:** <ISO-8601>
- **Confidence:** measured | sourced | benchmarked | estimated | guessed

## Summary
<the answer in three sentences or fewer>

## Body
<the substance produced by the procedure above>

## Evidence
| Claim | Source | Grade |
|---|---|---|

## Open questions
<what remains unknown, and who could answer it>

## Next action
<the single next step and its owner>
```

## Quality bar
- Budget enforced in CI
- Largest contributors attributed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
