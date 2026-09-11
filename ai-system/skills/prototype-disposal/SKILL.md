---
name: prototype-disposal
category: design
description: "Retire the prototype instead of letting it become the product."
output: "disposal-note.md"
used_by:
  - prototyper
---

# Prototype Disposal

`design` · produces `disposal-note.md` · used by `prototyper`

Retire the prototype instead of letting it become the product.

## Procedure
1. Record the answer the prototype produced.
2. Extract the learnings into the design spec.
3. Archive or delete the artifact rather than extending it.
4. Resist reusing prototype code in production; its shortcuts are invisible later.
5. Note if any part is genuinely production-worthy and why.

## Output contract
`disposal-note.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Learnings extracted into the spec
- Prototype not promoted into production
- The output states its confidence grade and names the evidence behind every load-bearing claim.
