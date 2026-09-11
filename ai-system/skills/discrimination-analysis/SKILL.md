---
name: discrimination-analysis
category: improvement
description: "Check the evaluation actually separates good from bad."
output: "discrimination-report.md"
used_by:
  - eval-designer
---

# Discrimination Analysis

**Category:** `improvement` · **Output artifact:** `discrimination-report.md`

## What this skill does
Check the evaluation actually separates good from bad.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `eval-designer`.

## Procedure
1. Score a known-good and a known-bad example with the rubric.
2. Check the scores differ meaningfully.
3. Check the case set produces a spread rather than clustering at one score.
4. Identify cases everything passes and everything fails; both teach little.
5. Revise or retire non-discriminating cases and dimensions.

## Output contract
Write `discrimination-report.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** discrimination-analysis
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
- Known-good and known-bad verified to separate
- Non-discriminating cases retired
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
