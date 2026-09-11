---
name: workflow-change-measurement
category: improvement
description: "Prove the workflow change helped."
output: "workflow-change.md"
used_by:
  - workflow-optimizer
---

# Workflow Change Measurement

**Category:** `improvement` · **Output artifact:** `workflow-change.md`

## What this skill does
Prove the workflow change helped.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `workflow-optimizer`.

## Procedure
1. Record cycle time, rework rate, and escaped defects before the change.
2. Change one workflow at a time.
3. Measure the same three after, over comparable volume.
4. Check none of the three got worse.
5. Revert if any did, and record why.

## Output contract
Write `workflow-change.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** workflow-change-measurement
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
- One workflow changed at a time
- Reverted if any of the three measures worsened
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
