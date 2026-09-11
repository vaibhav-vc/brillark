---
name: segmentation-analysis
category: market
description: "Divide the market into groups that behave differently and can be served differently."
output: "segmentation.md"
used_by:
  - market-researcher
---

# Segmentation Analysis

`market` · produces `segmentation.md` · used by `market-researcher`

Divide the market into groups that behave differently and can be served differently.

## Procedure
1. Segment on behaviour and needs, not only on firmographics.
2. Test that segments differ on something that changes how we sell or build.
3. Size each segment and estimate its reachability.
4. Score attractiveness: pain intensity, budget, accessibility, and competition.
5. Recommend one segment to start with and state why the others wait.

## Output contract
`segmentation.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Segments differ behaviourally, not just demographically
- One starting segment recommended
- The output states its confidence grade and names the evidence behind every load-bearing claim.
