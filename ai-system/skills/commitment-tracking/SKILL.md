---
name: commitment-tracking
category: finance
description: "Track money already promised but not yet paid."
output: "commitments.md"
used_by:
  - burn-runway-analyst
---

# Commitment Tracking

**Category:** `finance` · **Output artifact:** `commitments.md`

## What this skill does
Track money already promised but not yet paid.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `burn-runway-analyst`.

## Procedure
1. Inventory every signed contract, its term, and its notice period.
2. Record renewal and cancellation dates with the lead time needed to act.
3. Include contingent commitments and their trigger conditions.
4. Include these in runway calculations, not just paid invoices.
5. Alert before each notice-period deadline so renewals are a choice.

## Output contract
Write `commitments.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** commitment-tracking
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
- Notice periods tracked with lead time
- Commitments included in runway
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
