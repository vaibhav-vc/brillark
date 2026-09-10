---
name: dilution-modeling
category: finance
description: "Show what a financing actually costs in ownership."
output: "dilution-model.md"
used_by:
  - cap-table-steward
  - fundraising-strategist
---

# Dilution Modeling

**Category:** `finance` · **Output artifact:** `dilution-model.md`

## What this skill does
Show what a financing actually costs in ownership.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cap-table-steward`, `fundraising-strategist`.

## Procedure
1. Start from the current fully diluted cap table.
2. Model the new money, the pre-money valuation, and the option pool top-up.
3. Show whether the pool is created pre- or post-money and what that costs founders.
4. Project through the next round to show cumulative dilution.
5. Present ownership percentages, not just dollar values.

## Output contract
Write `dilution-model.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** dilution-modeling
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
- Pool timing effect made explicit
- Cumulative dilution projected forward
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
