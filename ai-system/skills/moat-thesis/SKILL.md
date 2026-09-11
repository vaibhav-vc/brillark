---
name: moat-thesis
category: strategy
description: "State the defensibility as a mechanism, not as a feature list."
output: "moat-thesis.md"
used_by:
  - chief-strategy-officer-agent
---

# Moat Thesis

`strategy` · produces `moat-thesis.md` · used by `chief-strategy-officer-agent`

State the defensibility as a mechanism, not as a feature list.

## Procedure
1. Identify the candidate mechanism: network effect, switching cost, scale economy, brand, or proprietary data.
2. Explain how it strengthens as we grow, specifically.
3. Estimate how long a well-funded competitor would need to replicate it.
4. Identify what would erode it.
5. State the evidence that it is actually forming, not just intended.

## Output contract
`moat-thesis.md` → `workspace/<venture-id>/strategy/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/strategy.tsv`.

## Quality bar
- Mechanism compounds with scale
- Formation evidence, not intention
- The output states its confidence grade and names the evidence behind every load-bearing claim.
