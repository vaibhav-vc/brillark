---
name: lesson-to-guardrail-conversion
category: orchestration
description: "Turn a lesson into a constraint that prevents the repeat automatically."
output: "guardrail-change.md"
used_by:
  - retrospective-agent
---

# Lesson To Guardrail Conversion

**Category:** `orchestration` · **Output artifact:** `guardrail-change.md`

## What this skill does
Turn a lesson into a constraint that prevents the repeat automatically.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `retrospective-agent`.

## Procedure
1. State the failure precisely enough to recognise it happening again.
2. Identify the artifact that could have prevented it: a guardrail, a checklist line, a skill step, or a test.
3. Write the change into that artifact directly.
4. Add a detection signal so a recurrence is visible early.
5. Verify at the next retrospective that the guardrail held.

## Output contract
Write `guardrail-change.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** lesson-to-guardrail-conversion
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
- Change written into a real artifact
- Detection signal added
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
