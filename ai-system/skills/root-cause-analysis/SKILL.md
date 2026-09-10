---
name: root-cause-analysis
category: orchestration
description: "Trace a failure back to the cause that can actually be changed."
output: "root-cause-analysis.md"
used_by:
  - retrospective-agent
---

# Root Cause Analysis

**Category:** `orchestration` · **Output artifact:** `root-cause-analysis.md`

## What this skill does
Trace a failure back to the cause that can actually be changed.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `retrospective-agent`.

## Procedure
1. Establish the factual timeline before interpreting anything.
2. Ask why repeatedly, stopping at the first cause under our control.
3. Distinguish the trigger from the underlying condition that allowed it.
4. Check for multiple contributing causes; single-cause stories are usually incomplete.
5. Propose a change to the condition, not a reminder to be careful.

## Output contract
Write `root-cause-analysis.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** root-cause-analysis
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
- Timeline established before analysis
- Fix targets the enabling condition
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
