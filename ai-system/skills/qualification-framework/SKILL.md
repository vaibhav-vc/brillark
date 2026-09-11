---
name: qualification-framework
category: gtm
description: "Decide quickly whether a deal is real."
output: "qualification-framework.md"
used_by:
  - sales-playbook-agent
---

# Qualification Framework

`gtm` · produces `qualification-framework.md` · used by `sales-playbook-agent`

Decide quickly whether a deal is real.

## Procedure
1. Define the qualification dimensions: need, authority, budget, timing, and fit.
2. Write the question that tests each dimension without interrogating.
3. Set the threshold below which a deal is disqualified.
4. Require evidence, not the seller's impression, per dimension.
5. Track how qualification score predicted actual outcomes and recalibrate.

## Output contract
`qualification-framework.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Evidence required per dimension
- Predictive accuracy tracked
- The output states its confidence grade and names the evidence behind every load-bearing claim.
