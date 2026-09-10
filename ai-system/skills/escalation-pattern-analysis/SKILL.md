---
name: escalation-pattern-analysis
category: orchestration
description: "Find the process defects behind repeated escalations."
output: "escalation-pattern-report.md"
used_by:
  - escalation-manager
---

# Escalation Pattern Analysis

**Category:** `orchestration` · **Output artifact:** `escalation-pattern-report.md`

## What this skill does
Find the process defects behind repeated escalations.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `escalation-manager`.

## Procedure
1. Group escalations by root cause rather than by symptom or reporter.
2. Identify causes appearing three or more times.
3. Trace each recurring cause to the process step that permits it.
4. Propose a process change, not a reminder to try harder.
5. Verify next cycle whether the pattern actually stopped.

## Output contract
Write `escalation-pattern-report.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** escalation-pattern-analysis
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
- Grouping by cause, not symptom
- Fix targets the process, not individual effort
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
