---
name: market-structure-analysis
category: strategy
description: "Understand who captures value in this market and why."
output: "market-structure.md"
used_by:
  - chief-strategy-officer-agent
---

# Market Structure Analysis

`strategy` · produces `market-structure.md` · used by `chief-strategy-officer-agent`

Understand who captures value in this market and why.

## Procedure
1. Map the value chain from raw input to end customer.
2. Identify where margin actually accumulates and what protects it.
3. Assess the bargaining power at each link.
4. Determine where we sit and whether that position can hold.
5. Identify the structural shift that could change the answer.

## Output contract
`market-structure.md` → `workspace/<venture-id>/strategy/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/strategy.tsv`.

## Quality bar
- Margin capture located in the chain
- Positional durability assessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
