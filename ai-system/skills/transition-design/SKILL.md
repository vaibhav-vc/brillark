---
name: transition-design
category: design
description: "Move between states so the user can follow what happened."
output: "transition-spec.md"
used_by:
  - motion-designer
---

# Transition Design

**Category:** `design` · **Output artifact:** `transition-spec.md`

## What this skill does
Move between states so the user can follow what happened.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `motion-designer`.

## Procedure
1. Identify what changed and make the motion explain that change.
2. Preserve the spatial relationship so elements come from where they belong.
3. Keep the duration short enough that it never becomes a wait.
4. Avoid animating large areas; movement at the edges is distracting.
5. Test the transition when triggered repeatedly in quick succession.

## Output contract
Write `transition-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** transition-design
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
- Motion explains the specific change
- Tested under rapid repeat triggering
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
