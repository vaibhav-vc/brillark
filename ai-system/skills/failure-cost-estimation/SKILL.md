---
name: failure-cost-estimation
category: improvement
description: "Put a number on what each failure pattern costs."
output: "failure-costs.md"
used_by:
  - failure-miner
---

# Failure Cost Estimation

**Category:** `improvement` · **Output artifact:** `failure-costs.md`

## What this skill does
Put a number on what each failure pattern costs.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `failure-miner`.

## Procedure
1. Count the rework hours or agent runs consumed.
2. Add the delay imposed on downstream work.
3. Add the cost of decisions made on corrupted information.
4. Note where the cost is unknown rather than assuming it is small.
5. Rank patterns by total cost per cycle.

## Output contract
Write `failure-costs.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** failure-cost-estimation
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
- Decision-corruption cost included
- Unknown costs marked rather than assumed small
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
