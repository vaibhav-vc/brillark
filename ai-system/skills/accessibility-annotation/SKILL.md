---
name: accessibility-annotation
category: design
description: "Give engineering everything it needs to build the interface accessibly."
output: "a11y-annotations.md"
used_by:
  - accessibility-designer
---

# Accessibility Annotation

`design` · produces `a11y-annotations.md` · used by `accessibility-designer`

Give engineering everything it needs to build the interface accessibly.

## Procedure
1. Annotate focus order for every interactive element.
2. Specify accessible names, roles, and descriptions where they differ from visible text.
3. Mark landmarks, headings, and their hierarchy.
4. Specify what is announced on state change and when.
5. Specify the keyboard interaction for every custom control.

## Output contract
`a11y-annotations.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Focus order specified across the whole view
- Keyboard behaviour specified for custom controls
- The output states its confidence grade and names the evidence behind every load-bearing claim.
