---
name: regression-sweep
category: improvement
description: "Check the change did not break something else."
output: "regression-sweep.md"
used_by:
  - improvement-head
  - prompt-optimizer
---

# Regression Sweep

**Category:** `improvement` · **Output artifact:** `regression-sweep.md`

## What this skill does
Check the change did not break something else.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `improvement-head`, `prompt-optimizer`.

## Procedure
1. Run the full evaluation suite, not only the targeted cases.
2. Compare per case, since aggregates hide offsetting changes.
3. Investigate every case that moved down, however small.
4. Block adoption on an unexplained regression.
5. Record accepted regressions with an explicit justification.

## Output contract
Write `regression-sweep.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** regression-sweep
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
- Per-case comparison, not aggregate only
- Unexplained regressions block adoption
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
