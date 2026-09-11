---
name: task-success-measurement
category: design
description: "Measure whether people can actually complete the task."
output: "task-metrics.md"
used_by:
  - usability-tester
---

# Task Success Measurement

**Category:** `design` · **Output artifact:** `task-metrics.md`

## What this skill does
Measure whether people can actually complete the task.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `usability-tester`.

## Procedure
1. Record completion, assisted completion, and failure as distinct outcomes.
2. Time the task and note where the time actually went.
3. Count errors and whether the participant recovered unaided.
4. Report rates with the sample size visible.
5. Compare against the prior round rather than an absolute target.

## Output contract
Write `task-metrics.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** task-success-measurement
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
- Assisted completion counted separately from success
- Sample size reported with every rate
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
