---
name: savings-verification
category: finance
description: "Prove a claimed saving actually appeared in the accounts."
output: "savings-verification.md"
used_by:
  - cost-optimization-analyst
---

# Savings Verification

**Category:** `finance` · **Output artifact:** `savings-verification.md`

## What this skill does
Prove a claimed saving actually appeared in the accounts.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cost-optimization-analyst`.

## Procedure
1. Record the claimed saving with its baseline and expected timing.
2. Check the next period's actuals for the specific line.
3. Adjust for volume changes that would have moved the cost anyway.
4. Mark the saving realised, partial, or not realised.
5. Report the realisation rate so future claims can be discounted appropriately.

## Output contract
Write `savings-verification.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** savings-verification
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
- Verified against actuals, not forecasts
- Volume effects adjusted out
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
