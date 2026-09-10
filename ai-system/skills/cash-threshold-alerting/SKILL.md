---
name: cash-threshold-alerting
category: finance
description: "Make the cash position trigger action automatically."
output: "cash-alert-policy.md"
used_by:
  - burn-runway-analyst
---

# Cash Threshold Alerting

**Category:** `finance` · **Output artifact:** `cash-alert-policy.md`

## What this skill does
Make the cash position trigger action automatically.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `burn-runway-analyst`.

## Procedure
1. Set thresholds in months of runway, not in currency.
2. Define the specific action each threshold triggers.
3. Assign the person or agent who executes on each trigger.
4. Wire the alert to the actual data source so it cannot be forgotten.
5. Test the alert once to confirm it fires.

## Output contract
Write `cash-alert-policy.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** cash-threshold-alerting
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
- Thresholds in months of runway
- Alert tested, not just configured
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
