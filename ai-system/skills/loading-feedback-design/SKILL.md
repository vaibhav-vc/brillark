---
name: loading-feedback-design
category: design
description: "Tell the user what is happening while they wait."
output: "loading-spec.md"
used_by:
  - motion-designer
---

# Loading Feedback Design

**Category:** `design` · **Output artifact:** `loading-spec.md`

## What this skill does
Tell the user what is happening while they wait.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `motion-designer`.

## Procedure
1. Choose feedback by expected duration: instant, short wait, or long operation.
2. Show progress where it is knowable, and indeterminate feedback only where it is not.
3. Preserve layout so content does not jump when it arrives.
4. Let long operations be cancelled or backgrounded.
5. Design the timeout: what the user sees when it never finishes.

## Output contract
Write `loading-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** loading-feedback-design
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
- Feedback matched to expected duration
- Timeout behaviour designed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
