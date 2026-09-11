---
name: voice-of-customer-synthesis
category: gtm
description: "Turn scattered customer feedback into something product can act on."
output: "voc-digest.md"
used_by:
  - customer-success-agent
---

# Voice Of Customer Synthesis

`gtm` · produces `voc-digest.md` · used by `customer-success-agent`

Turn scattered customer feedback into something product can act on.

## Procedure
1. Collect feedback from support, sales, reviews, and usage data.
2. Code into themes and count frequency and severity.
3. Distinguish requested solutions from underlying problems.
4. Weight by segment value and strategic fit.
5. Deliver as ranked problems with evidence, not as a feature list.

## Output contract
`voc-digest.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Problems separated from requested solutions
- Themes counted and weighted
- The output states its confidence grade and names the evidence behind every load-bearing claim.
