---
name: blocker-detection
category: orchestration
description: "Find work that has stopped moving before someone reports it."
output: "blocker-report.md"
used_by:
  - progress-tracker
---

# Blocker Detection

**Category:** `orchestration` · **Output artifact:** `blocker-report.md`

## What this skill does
Find work that has stopped moving before someone reports it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `progress-tracker`.

## Procedure
1. Compare each task's elapsed time against its expected duration.
2. Flag tasks with no artifact change since the last check.
3. Distinguish blocked from not-started from slow.
4. Identify the specific missing input or decision for each blocker.
5. Age every blocker and escalate on the age threshold.

## Output contract
Write `blocker-report.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** blocker-detection
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
- Blocked distinguished from slow
- Each blocker names its missing input
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
