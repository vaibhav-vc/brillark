---
name: status-tracking
category: orchestration
description: "Report the true state of work from artifacts rather than self-assessment."
output: "status-board.md"
used_by:
  - progress-tracker
---

# Status Tracking

**Category:** `orchestration` · **Output artifact:** `status-board.md`

## What this skill does
Report the true state of work from artifacts rather than self-assessment.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `progress-tracker`.

## Procedure
1. Derive status from artifact existence and DoD checks, not from percentages.
2. Use a strict state set: not started, in progress, blocked, in review, done.
3. Record the last observed change and its timestamp.
4. Flag any divergence between reported and observed status.
5. Publish on a fixed cadence so absence of news is itself information.

## Output contract
Write `status-board.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** status-tracking
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
- Status derived from artifacts
- Divergence from self-reports flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
