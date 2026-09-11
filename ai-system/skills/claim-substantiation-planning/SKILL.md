---
name: claim-substantiation-planning
category: market
description: "Decide what proof each marketing claim needs before it is made."
output: "claim-proof-plan.md"
used_by:
  - value-proposition-designer
---

# Claim Substantiation Planning

`market` · produces `claim-proof-plan.md` · used by `value-proposition-designer`

Decide what proof each marketing claim needs before it is made.

## Procedure
1. List every claim the messaging makes, including implied ones.
2. Classify each as measurable, comparative, or subjective.
3. Define the proof required per claim: data, case study, benchmark, or guarantee.
4. Identify claims that cannot be proven and cut them.
5. Assign an owner and a deadline to gather each proof.

## Output contract
`claim-proof-plan.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Implied claims included
- Unprovable claims cut, not softened
- The output states its confidence grade and names the evidence behind every load-bearing claim.
