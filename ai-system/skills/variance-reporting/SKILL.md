---
name: variance-reporting
category: orchestration
description: "Report the gap between plan and reality early and without spin."
output: "variance-report.md"
used_by:
  - progress-tracker
---

# Variance Reporting

**Category:** `orchestration` · **Output artifact:** `variance-report.md`

## What this skill does
Report the gap between plan and reality early and without spin.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `progress-tracker`.

## Procedure
1. Compare actual against plan for schedule, scope, and budget.
2. Report variance as soon as it is detectable, not at the deadline.
3. Explain the cause, distinguishing estimation error from scope change from blockage.
4. State the revised forecast and its confidence.
5. Propose the recovery option or state that there is none.

## Output contract
Write `variance-report.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** variance-reporting
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
- Reported before the deadline
- Cause classified, not just described
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
