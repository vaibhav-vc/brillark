---
name: rubric-design
category: improvement
description: "Build a scoring scheme different reviewers apply the same way."
output: "rubric.md"
used_by:
  - eval-designer
---

# Rubric Design

**Category:** `improvement` · **Output artifact:** `rubric.md`

## What this skill does
Build a scoring scheme different reviewers apply the same way.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `eval-designer`.

## Procedure
1. Define independent dimensions; overlapping ones double-count.
2. Anchor every score level with a real example.
3. Avoid dimensions that reduce to overall impression.
4. Pilot on a small sample and check agreement.
5. Revise or drop dimensions where scorers persistently disagree.

## Output contract
Write `rubric.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** rubric-design
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
- Every level anchored with a real example
- Disagreeing dimensions dropped
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
