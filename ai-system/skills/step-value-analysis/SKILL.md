---
name: step-value-analysis
category: improvement
description: "Find workflow steps that change no outcome."
output: "step-value.md"
used_by:
  - workflow-optimizer
---

# Step Value Analysis

**Category:** `improvement` · **Output artifact:** `step-value.md`

## What this skill does
Find workflow steps that change no outcome.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `workflow-optimizer`.

## Procedure
1. For each step, ask what decision or artifact it changes.
2. Check the historical record: did this step ever alter an outcome?
3. Distinguish a step that rarely fires from one that never matters.
4. Flag ceremony steps for removal.
5. Keep steps that are the only evidence for a gate, however rarely they fire.

## Output contract
Write `step-value.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** step-value-analysis
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
- Rarely-firing distinguished from never-mattering
- Gate-evidence steps protected
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
