---
name: runway-forecast
category: finance
description: "Determine the date the venture runs out of money."
output: "runway.md"
used_by:
  - burn-runway-analyst
  - finance-head
---

# Runway Forecast

**Category:** `finance` · **Output artifact:** `runway.md`

## What this skill does
Determine the date the venture runs out of money.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `burn-runway-analyst`, `finance-head`.

## Procedure
1. Start from the current cash balance, confirmed against the bank, not the ledger.
2. Project net burn month by month from the hiring plan and committed contracts.
3. Include committed but uninvoiced obligations.
4. Produce the runway date under base and downside cases.
5. Set threshold alerts at 12, 9, and 6 months with pre-agreed actions.

## Output contract
Write `runway.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** runway-forecast
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
- Cash balance confirmed at source
- Committed obligations included
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
