---
name: moderation-discipline
category: design
description: "Run the session without contaminating the data."
output: "session-notes.md"
used_by:
  - usability-tester
---

# Moderation Discipline

**Category:** `design` · **Output artifact:** `session-notes.md`

## What this skill does
Run the session without contaminating the data.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `usability-tester`.

## Procedure
1. Explain that you are testing the product, not the participant, and mean it.
2. Ask what they expect to happen before they act.
3. Sit on your hands: never point, never hint, never explain the interface.
4. When they ask for help, ask what they would do if you were not there.
5. Save your explanation for the debrief, after all tasks are finished.

## Output contract
Write `session-notes.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** moderation-discipline
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
- No hints or rescues during tasks
- Expectations captured before each action
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
