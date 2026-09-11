---
name: design-strategy-alignment
category: design
description: "Check the design direction actually serves the strategy."
output: "alignment-review.md"
used_by:
  - chief-design-officer-agent
---

# Design Strategy Alignment

`design` · produces `alignment-review.md` · used by `chief-design-officer-agent`

Check the design direction actually serves the strategy.

## Procedure
1. Restate the strategy and the customer it serves.
2. Check the design direction supports that customer's judgement criteria.
3. Identify where design is optimising something the strategy does not need.
4. Identify where the strategy requires an experience we cannot yet deliver.
5. Recommend the realignment explicitly.

## Output contract
`alignment-review.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Misaligned optimisation identified
- Undeliverable strategy requirements surfaced
- The output states its confidence grade and names the evidence behind every load-bearing claim.
