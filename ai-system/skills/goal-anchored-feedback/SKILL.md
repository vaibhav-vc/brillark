---
name: goal-anchored-feedback
category: design
description: "Give feedback that can be acted on."
output: "feedback-notes.md"
used_by:
  - design-critic
---

# Goal Anchored Feedback

**Category:** `design` · **Output artifact:** `feedback-notes.md`

## What this skill does
Give feedback that can be acted on.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-critic`.

## Procedure
1. Restate the goal before commenting.
2. Describe the problem you observed, not the solution you prefer.
3. Say who it affects and in what situation.
4. Rate how much it matters against the goal.
5. Offer a direction rather than a redesign.

## Output contract
Write `feedback-notes.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** goal-anchored-feedback
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
- Problem described rather than solution prescribed
- Impact tied to the goal
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
