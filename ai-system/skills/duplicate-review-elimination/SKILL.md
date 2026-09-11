---
name: duplicate-review-elimination
category: improvement
description: "Remove reviews that check the same thing twice."
output: "review-map.md"
used_by:
  - workflow-optimizer
---

# Duplicate Review Elimination

**Category:** `improvement` · **Output artifact:** `review-map.md`

## What this skill does
Remove reviews that check the same thing twice.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `workflow-optimizer`.

## Procedure
1. Map every review step and what each checks.
2. Identify overlapping checks across steps.
3. Keep the review closest to where the defect originates.
4. Remove the duplicate rather than coordinating between them.
5. Watch for escaped defects after removal.

## Output contract
Write `review-map.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** duplicate-review-elimination
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
- Review kept closest to defect origin
- Escaped defects watched after removal
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
