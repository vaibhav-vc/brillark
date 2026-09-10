---
name: regression-detection
category: orchestration
description: "Catch quality drops when a prompt, skill, or agent definition changes."
output: "regression-report.md"
used_by:
  - evaluation-harness-agent
---

# Regression Detection

**Category:** `orchestration` · **Output artifact:** `regression-report.md`

## What this skill does
Catch quality drops when a prompt, skill, or agent definition changes.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `evaluation-harness-agent`.

## Procedure
1. Run the evaluation suite before and after the change.
2. Compare scores per case, not just in aggregate — averages hide regressions.
3. Investigate any case that moved down, however small the aggregate change.
4. Block the change or accept the regression explicitly with a reason.
5. Record the result alongside the change in version history.

## Output contract
Write `regression-report.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** regression-detection
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
- Per-case comparison, not just aggregate
- Accepted regressions explicitly justified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
