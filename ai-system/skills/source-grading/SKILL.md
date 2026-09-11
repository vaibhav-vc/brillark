---
name: source-grading
category: market
description: "Rate how much a source can be trusted before using it in an argument."
output: "source-grades.md"
used_by:
  - market-researcher
---

# Source Grading

`market` · produces `source-grades.md` · used by `market-researcher`

Rate how much a source can be trusted before using it in an argument.

## Procedure
1. Identify who produced the source and what they gain from its conclusion.
2. Check the methodology and the sample; no methodology means no grade above 'estimated'.
3. Check the date and whether the underlying conditions still hold.
4. Look for a primary source behind a secondary claim.
5. Assign a grade — measured, sourced, benchmarked, estimated, or guessed — and carry it forward.

## Output contract
`source-grades.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Producer incentive assessed
- Grade carried into every downstream use
- The output states its confidence grade and names the evidence behind every load-bearing claim.
