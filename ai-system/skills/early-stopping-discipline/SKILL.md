---
name: early-stopping-discipline
category: improvement
description: "Do not stop the trial when it starts looking good."
output: "trial-log.md"
used_by:
  - ab-test-runner
---

# Early Stopping Discipline

**Category:** `improvement` · **Output artifact:** `trial-log.md`

## What this skill does
Do not stop the trial when it starts looking good.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ab-test-runner`.

## Procedure
1. Commit to the planned sample before starting.
2. Do not inspect interim results unless a stopping rule was defined in advance.
3. If you must stop early, record it and treat the result as provisional.
4. Re-run to the full sample before adopting anything.
5. Record any deviation from the plan alongside the result.

## Output contract
Write `trial-log.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** early-stopping-discipline
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
- Interim inspection only under a pre-defined rule
- Early stops recorded and treated as provisional
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
