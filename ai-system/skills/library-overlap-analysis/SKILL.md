---
name: library-overlap-analysis
category: improvement
description: "Find skills that have blurred into each other, and gaps between them."
output: "overlap-report.md"
used_by:
  - skill-refiner
---

# Library Overlap Analysis

**Category:** `improvement` · **Output artifact:** `overlap-report.md`

## What this skill does
Find skills that have blurred into each other, and gaps between them.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `skill-refiner`.

## Procedure
1. Compare skills within a category for overlapping procedures.
2. Check whether agents actually distinguish them in practice.
3. Identify decisions no skill currently covers.
4. Recommend merge, split, or leave alone — most should be left alone.
5. Check every reference before recommending a merge.

## Output contract
Write `overlap-report.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** library-overlap-analysis
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
- Practical distinguishability tested, not just textual similarity
- References checked before merge
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
