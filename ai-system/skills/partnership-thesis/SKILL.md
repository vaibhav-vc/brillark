---
name: partnership-thesis
category: gtm
description: "State why a partnership would create value before pursuing one."
output: "partnership-thesis.md"
used_by:
  - chief-strategy-officer-agent
  - partnership-bd-agent
---

# Partnership Thesis

`gtm` · produces `partnership-thesis.md` · used by `chief-strategy-officer-agent`, `partnership-bd-agent`

State why a partnership would create value before pursuing one.

## Procedure
1. Name the specific gap: distribution, capability, or credibility.
2. Describe what a partner gains, in their terms and their metrics.
3. Identify the partner types that have both the asset and the incentive.
4. Estimate the value created and how it would be shared.
5. Define what would prove the thesis wrong within one quarter.

## Output contract
`partnership-thesis.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Partner's own incentive articulated
- Disproof condition set within a quarter
- The output states its confidence grade and names the evidence behind every load-bearing claim.
