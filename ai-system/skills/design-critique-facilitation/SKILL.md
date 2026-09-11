---
name: design-critique-facilitation
category: design
description: "Run critique that improves the work rather than asserting rank."
output: "critique-record.md"
used_by:
  - design-critic
  - design-head
---

# Design Critique Facilitation

**Category:** `design` · **Output artifact:** `critique-record.md`

## What this skill does
Run critique that improves the work rather than asserting rank.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-critic`, `design-head`.

## Procedure
1. Have the designer state the goal, the constraints, and the open questions first.
2. Restrict feedback to the stated goal.
3. Require each objection to name who fails to do what.
4. Separate 'does not work' from 'I would have done it differently'.
5. Close with decisions and owners, not a list of opinions.

## Output contract
Write `critique-record.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** design-critique-facilitation
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
- Feedback restricted to the stated goal
- Closes with decisions, not opinions
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
