---
name: inter-rater-calibration
category: improvement
description: "Get different scorers to agree."
output: "calibration-report.md"
used_by:
  - eval-designer
---

# Inter Rater Calibration

**Category:** `improvement` · **Output artifact:** `calibration-report.md`

## What this skill does
Get different scorers to agree.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `eval-designer`.

## Procedure
1. Have multiple scorers rate the same sample independently.
2. Measure agreement per dimension, not just overall.
3. Discuss the disagreements and find the ambiguity in the rubric.
4. Revise the anchors rather than asking scorers to try harder.
5. Re-measure agreement after the revision.

## Output contract
Write `calibration-report.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** inter-rater-calibration
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
- Agreement measured per dimension
- Rubric revised rather than exhorting scorers
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
