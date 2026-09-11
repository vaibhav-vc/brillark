---
name: persona-development
category: market
description: "Describe the people involved in the purchase and what each one needs."
output: "personas.md"
used_by:
  - icp-persona-builder
---

# Persona Development

`market` · produces `personas.md` · used by `icp-persona-builder`

Describe the people involved in the purchase and what each one needs.

## Procedure
1. Separate the buyer, the user, the influencer, and the blocker.
2. For each, capture their goal, their risk, and what makes them say no.
3. Ground every attribute in interview evidence, not imagination.
4. Record their vocabulary for the problem.
5. Note where each persona goes for information.

## Output contract
`personas.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Every attribute traced to evidence
- Blocker persona included
- The output states its confidence grade and names the evidence behind every load-bearing claim.
