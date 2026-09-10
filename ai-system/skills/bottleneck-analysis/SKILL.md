---
name: bottleneck-analysis
category: orchestration
description: "Find the one constraint limiting the whole system's output."
output: "bottleneck-report.md"
used_by:
  - coo-agent
---

# Bottleneck Analysis

**Category:** `orchestration` · **Output artifact:** `bottleneck-report.md`

## What this skill does
Find the one constraint limiting the whole system's output.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `coo-agent`.

## Procedure
1. Measure queue length and wait time at each stage.
2. Identify the stage where work accumulates fastest.
3. Confirm it is the constraint by checking whether upstream speed-ups help at all.
4. Exploit the constraint before adding capacity elsewhere.
5. Re-measure after the change; the constraint usually moves.

## Output contract
Write `bottleneck-report.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** bottleneck-analysis
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
- Constraint confirmed, not assumed
- Re-measured after intervention
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
