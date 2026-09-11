---
name: sample-sizing
category: improvement
description: "Work out how many cases the trial needs."
output: "sample-plan.md"
used_by:
  - ab-test-runner
---

# Sample Sizing

**Category:** `improvement` · **Output artifact:** `sample-plan.md`

## What this skill does
Work out how many cases the trial needs.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ab-test-runner`.

## Procedure
1. State the smallest improvement that would be worth adopting.
2. Estimate the variability from previous runs.
3. Compute the sample needed to detect that effect reliably.
4. If the sample is unaffordable, say the trial cannot answer the question.
5. Never reduce the sample and keep the original claim.

## Output contract
Write `sample-plan.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** sample-sizing
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
- Minimum worthwhile effect stated first
- Underpowered trials declared, not run anyway
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
