---
name: supplier-quoting
category: hardware
description: "Compare quotes on more than price."
output: "quote-comparison.md"
used_by:
  - prototyping-fabrication-agent
---

# Supplier Quoting

`hardware` · produces `quote-comparison.md` · used by `prototyping-fabrication-agent`

Compare quotes on more than price.

## Procedure
1. Send an identical package to every supplier so quotes are comparable.
2. Compare on capability, tolerance, lead time, and price together.
3. Check what is excluded: tooling, setup, inspection, and freight.
4. Check capacity and their record on schedule, not only their quote.
5. Record the decision and the rejected quotes with reasons.

## Output contract
`quote-comparison.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Identical package sent to every supplier
- Exclusions and capacity compared, not just price
- The output states its confidence grade and names the evidence behind every load-bearing claim.
