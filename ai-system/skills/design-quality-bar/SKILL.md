---
name: design-quality-bar
category: design
description: "Define what finished means for a design."
output: "quality-bar.md"
used_by:
  - design-head
---

# Design Quality Bar

`design` · produces `quality-bar.md` · used by `design-head`

Define what finished means for a design.

## Procedure
1. Require a stated user problem with evidence.
2. Require the full flow, all view states, and the unhappy paths.
3. Require accessibility annotation and contrast verification.
4. Require design system compliance or a recorded exception.
5. Require validation with real users before build.

## Output contract
`quality-bar.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- All states and unhappy paths required
- Accessibility required before build, not after
- The output states its confidence grade and names the evidence behind every load-bearing claim.
