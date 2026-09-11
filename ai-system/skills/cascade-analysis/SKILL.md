---
name: cascade-analysis
category: council
description: "Find failures that trigger other failures."
output: "cascade-analysis.md"
used_by:
  - council-risk-and-failure-modes
---

# Cascade Analysis

`council` · produces `cascade-analysis.md` · used by `council-risk-and-failure-modes`

Find failures that trigger other failures.

## Procedure
1. Map the dependencies between failure modes.
2. Identify single failures that would trigger three or more others.
3. Estimate the combined impact of each cascade.
4. Identify the circuit breaker that would stop the chain.
5. Prioritise mitigations at the cascade origin.

## Output contract
`cascade-analysis.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Cascade chains explicitly mapped
- Circuit breakers identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
