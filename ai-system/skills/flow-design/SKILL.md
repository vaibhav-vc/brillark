---
name: flow-design
category: design
description: "Design the complete path through a task, including the ways it goes wrong."
output: "flow-spec.md"
used_by:
  - interaction-designer
---

# Flow Design

**Category:** `design` · **Output artifact:** `flow-spec.md`

## What this skill does
Design the complete path through a task, including the ways it goes wrong.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `interaction-designer`.

## Procedure
1. Map the entry points; users rarely arrive at step one.
2. Design the happy path, then every branch off it.
3. Design interruption and re-entry: what happens if they leave halfway.
4. Specify what each step needs from the user and what it gives back.
5. Identify the step most likely to be abandoned and reduce its cost.

## Output contract
Write `flow-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** flow-design
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
- Entry, interruption, and re-entry all designed
- Every branch specified, not just the happy path
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
