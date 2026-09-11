---
name: improvement-return-analysis
category: improvement
description: "Judge whether the improvement effort was worth it."
output: "return-analysis.md"
used_by:
  - chief-learning-officer-agent
---

# Improvement Return Analysis

**Category:** `improvement` · **Output artifact:** `return-analysis.md`

## What this skill does
Judge whether the improvement effort was worth it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-learning-officer-agent`.

## Procedure
1. Sum the cost of the improvement work for the period.
2. Sum the measured gains from adopted changes that held.
3. Subtract the cost of changes that were reverted.
4. Report the net honestly, including negative periods.
5. Recommend continuing, refocusing, or reducing the effort.

## Output contract
Write `return-analysis.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** improvement-return-analysis
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
- Reverted changes counted as cost
- Negative periods reported honestly
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
