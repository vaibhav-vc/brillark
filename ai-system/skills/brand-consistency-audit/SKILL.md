---
name: brand-consistency-audit
category: gtm
description: "Find where the brand has drifted from its guidelines."
output: "brand-audit.md"
used_by:
  - brand-narrative-agent
---

# Brand Consistency Audit

`gtm` · produces `brand-audit.md` · used by `brand-narrative-agent`

Find where the brand has drifted from its guidelines.

## Procedure
1. Inventory every customer-facing surface.
2. Compare each against the voice and visual guidelines.
3. Record drift with a specific example and its location.
4. Prioritise by audience reach rather than by how much it irritates.
5. Fix and set the review cadence.

## Output contract
`brand-audit.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Drift recorded with specific examples
- Prioritised by reach
- The output states its confidence grade and names the evidence behind every load-bearing claim.
