---
name: capability-target-setting
category: improvement
description: "Set improvement targets that can be judged."
output: "capability-targets.md"
used_by:
  - chief-learning-officer-agent
---

# Capability Target Setting

**Category:** `improvement` · **Output artifact:** `capability-targets.md`

## What this skill does
Set improvement targets that can be judged.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-learning-officer-agent`.

## Procedure
1. State the capability in terms of an observable outcome.
2. Set the current baseline from measurement.
3. Set a target and a date.
4. State what evidence would show the target was met.
5. State what would make the target wrong to pursue.

## Output contract
Write `capability-targets.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** capability-target-setting
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
- Baseline measured, not assumed
- Evidence of success defined in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
