---
name: motion-principles
category: design
description: "Define what motion is for in this product, and what it is not for."
output: "motion-principles.md"
used_by:
  - motion-designer
---

# Motion Principles

`design` · produces `motion-principles.md` · used by `motion-designer`

Define what motion is for in this product, and what it is not for.

## Procedure
1. State the purposes motion serves here: continuity, causality, feedback, and status.
2. Define the duration and easing scale as tokens.
3. Rule out decorative motion that delays the user.
4. Define how motion behaves when many elements change at once.
5. Document the reduced-motion contract for the whole product.

## Output contract
`motion-principles.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Purposes stated and decoration ruled out
- Reduced-motion contract documented
- The output states its confidence grade and names the evidence behind every load-bearing claim.
