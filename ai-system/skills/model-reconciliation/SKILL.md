---
name: model-reconciliation
category: finance
description: "Check the model against reality and fix the model, not the reality."
output: "reconciliation.md"
used_by:
  - financial-model-builder
---

# Model Reconciliation

**Category:** `finance` · **Output artifact:** `reconciliation.md`

## What this skill does
Check the model against reality and fix the model, not the reality.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `financial-model-builder`.

## Procedure
1. Pull actuals for the closed period from the source systems.
2. Compare each driver against its modelled value, not just the totals.
3. Explain every variance above the materiality threshold.
4. Correct the model's assumptions where the variance is structural rather than noise.
5. Record the reconciliation and the resulting model version.

## Output contract
Write `reconciliation.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** model-reconciliation
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
- Driver-level comparison, not totals only
- Structural variances corrected in the model
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
