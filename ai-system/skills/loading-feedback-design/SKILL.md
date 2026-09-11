---
name: loading-feedback-design
category: design
description: "Tell the user what is happening while they wait."
output: "loading-spec.md"
used_by:
  - motion-designer
---

# Loading Feedback Design

`design` · produces `loading-spec.md` · used by `motion-designer`

Tell the user what is happening while they wait.

## Procedure
1. Choose feedback by expected duration: instant, short wait, or long operation.
2. Show progress where it is knowable, and indeterminate feedback only where it is not.
3. Preserve layout so content does not jump when it arrives.
4. Let long operations be cancelled or backgrounded.
5. Design the timeout: what the user sees when it never finishes.

## Output contract
`loading-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Feedback matched to expected duration
- Timeout behaviour designed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
