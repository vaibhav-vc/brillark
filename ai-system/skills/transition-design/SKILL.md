---
name: transition-design
category: design
description: "Move between states so the user can follow what happened."
output: "transition-spec.md"
used_by:
  - motion-designer
---

# Transition Design

`design` · produces `transition-spec.md` · used by `motion-designer`

Move between states so the user can follow what happened.

## Procedure
1. Identify what changed and make the motion explain that change.
2. Preserve the spatial relationship so elements come from where they belong.
3. Keep the duration short enough that it never becomes a wait.
4. Avoid animating large areas; movement at the edges is distracting.
5. Test the transition when triggered repeatedly in quick succession.

## Output contract
`transition-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Motion explains the specific change
- Tested under rapid repeat triggering
- The output states its confidence grade and names the evidence behind every load-bearing claim.
