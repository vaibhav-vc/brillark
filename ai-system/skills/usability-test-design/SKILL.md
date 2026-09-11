---
name: usability-test-design
category: design
description: "Design a test that produces findings rather than reassurance."
output: "test-plan.md"
used_by:
  - usability-tester
---

# Usability Test Design

**Category:** `design` · **Output artifact:** `test-plan.md`

## What this skill does
Design a test that produces findings rather than reassurance.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `usability-tester`.

## Procedure
1. Write the tasks as goals the participant would actually have, never as instructions naming the UI.
2. Define the success criterion for each task before recruiting.
3. Recruit to the target segment; wrong participants produce confident wrong findings.
4. Plan five participants per segment per round, and plan the rounds.
5. Prepare what you will not say, so you do not rescue the participant mid-task.

## Output contract
Write `test-plan.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** usability-test-design
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
- Tasks stated as goals, not UI instructions
- Success criteria set before recruitment
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
