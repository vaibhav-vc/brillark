---
name: channel-cac-modeling
category: gtm
description: "Compute what each channel actually costs per acquired customer."
output: "channel-cac.md"
used_by:
  - cmo-agent
  - gtm-strategist
---

# Channel CAC Modeling

`gtm` · produces `channel-cac.md` · used by `cmo-agent`, `gtm-strategist`

Compute what each channel actually costs per acquired customer.

## Procedure
1. Include all costs: media, tools, content production, and people time.
2. Attribute conversions with a stated model, and acknowledge its limits.
3. Compute CAC and payback per channel, not blended.
4. Compare against the LTV-derived ceiling.
5. Rank channels and recommend which to scale, hold, or kill.

## Output contract
`channel-cac.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Fully loaded costs included
- Compared against an LTV-derived ceiling
- The output states its confidence grade and names the evidence behind every load-bearing claim.
