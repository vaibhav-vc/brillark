---
name: bookkeeping-standard
category: finance
description: "Define how transactions are recorded so the books stay auditable."
output: "bookkeeping-standard.md"
used_by:
  - tax-and-compliance-finance
---

# Bookkeeping Standard

**Category:** `finance` · **Output artifact:** `bookkeeping-standard.md`

## What this skill does
Define how transactions are recorded so the books stay auditable.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `tax-and-compliance-finance`.

## Procedure
1. Define the chart of accounts and what belongs in each.
2. Set the rules for revenue, prepayments, and accruals.
3. Define the documentation required per transaction type.
4. Set the close calendar and its checklist.
5. Define who may post, who reviews, and how corrections are recorded.

## Output contract
Write `bookkeeping-standard.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** bookkeeping-standard
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
- Documentation requirement defined per type
- Correction process explicit
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
