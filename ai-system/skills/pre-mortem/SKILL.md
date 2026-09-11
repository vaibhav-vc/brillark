---
name: pre-mortem
category: council
description: "Assume the venture failed and reconstruct how."
output: "pre-mortem.md"
used_by:
  - chief-risk-officer-agent
  - council-risk-and-failure-modes
---

# Pre Mortem

`council` · produces `pre-mortem.md` · used by `chief-risk-officer-agent`, `council-risk-and-failure-modes`

Assume the venture failed and reconstruct how.

## Procedure
1. Set the scene: it is twelve months later and this failed.
2. Write the story of the failure in specific steps.
3. Trace back to the earliest point the failure was detectable.
4. Identify which failures were recoverable and which were not.
5. Propose an early indicator for each failure path.

## Output contract
`pre-mortem.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Failure written as a specific narrative
- Earliest detection point identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
