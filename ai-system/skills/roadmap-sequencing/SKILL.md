---
name: roadmap-sequencing
category: product
description: "Order the roadmap for learning value rather than for tidiness."
output: "roadmap.md"
used_by:
  - cpo-agent
---

# Roadmap Sequencing

`product` · produces `roadmap.md` · used by `cpo-agent`

Order the roadmap for learning value rather than for tidiness.

## Procedure
1. Identify what each item would teach us, not just what it would deliver.
2. Sequence the highest-uncertainty, highest-dependency items early.
3. Check capacity honestly against the sequence.
4. Group items that share technical foundations.
5. State what each quarter's sequence assumes and what would reorder it.

## Output contract
`roadmap.md` → `workspace/<venture-id>/product/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/product.tsv`.

## Quality bar
- Sequenced by learning value
- Capacity checked against the sequence
- The output states its confidence grade and names the evidence behind every load-bearing claim.
