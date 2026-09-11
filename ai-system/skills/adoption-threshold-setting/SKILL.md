---
name: adoption-threshold-setting
category: improvement
description: "Decide in advance what would justify adopting the change."
output: "adoption-threshold.md"
used_by:
  - improvement-head
  - prompt-optimizer
---

# Adoption Threshold Setting

**Category:** `improvement` · **Output artifact:** `adoption-threshold.md`

## What this skill does
Decide in advance what would justify adopting the change.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `improvement-head`, `prompt-optimizer`.

## Procedure
1. Set the minimum improvement worth the churn of changing.
2. Set the maximum acceptable regression elsewhere.
3. Define the sample the result must be based on.
4. Record the threshold before seeing any result.
5. Refuse to move the threshold after the fact.

## Output contract
Write `adoption-threshold.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** adoption-threshold-setting
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
- Threshold recorded before results are seen
- Post-hoc threshold changes refused
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
