---
name: accessibility-annotation
category: design
description: "Give engineering everything it needs to build the interface accessibly."
output: "a11y-annotations.md"
used_by:
  - accessibility-designer
---

# Accessibility Annotation

**Category:** `design` · **Output artifact:** `a11y-annotations.md`

## What this skill does
Give engineering everything it needs to build the interface accessibly.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `accessibility-designer`.

## Procedure
1. Annotate focus order for every interactive element.
2. Specify accessible names, roles, and descriptions where they differ from visible text.
3. Mark landmarks, headings, and their hierarchy.
4. Specify what is announced on state change and when.
5. Specify the keyboard interaction for every custom control.

## Output contract
Write `a11y-annotations.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** accessibility-annotation
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
- Focus order specified across the whole view
- Keyboard behaviour specified for custom controls
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
