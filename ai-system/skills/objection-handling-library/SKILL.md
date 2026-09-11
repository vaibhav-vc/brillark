---
name: objection-handling-library
category: gtm
description: "Build evidenced answers to the objections that actually lose deals."
output: "objection-library.md"
used_by:
  - sales-playbook-agent
---

# Objection Handling Library

`gtm` · produces `objection-library.md` · used by `sales-playbook-agent`

Build evidenced answers to the objections that actually lose deals.

## Procedure
1. Collect objections from lost-deal records, not from imagination.
2. Rank by frequency and by how often they end the deal.
3. Write the answer for each, grounded in proof rather than reassurance.
4. Attach the specific asset — data, case study, or reference.
5. Review quarterly and retire objections the product has fixed.

## Output contract
`objection-library.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Objections sourced from lost deals
- Each answer carries a proof asset
- The output states its confidence grade and names the evidence behind every load-bearing claim.
