---
name: reduced-motion-design
category: design
description: "Give an equivalent experience to people who have turned motion off."
output: "reduced-motion-spec.md"
used_by:
  - motion-designer
---

# Reduced Motion Design

`design` · produces `reduced-motion-spec.md` · used by `motion-designer`

Give an equivalent experience to people who have turned motion off.

## Procedure
1. Honour the system reduced-motion preference everywhere.
2. Replace movement with an instant change or a simple fade, never nothing at all.
3. Ensure state changes remain perceivable without motion.
4. Never make reduced motion a degraded or slower experience.
5. Test the entire flow with the preference enabled.

## Output contract
`reduced-motion-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Preference honoured across the whole product
- State changes perceivable without motion
- The output states its confidence grade and names the evidence behind every load-bearing claim.
