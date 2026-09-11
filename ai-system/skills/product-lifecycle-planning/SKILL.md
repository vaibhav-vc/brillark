---
name: product-lifecycle-planning
category: hardware
description: "Plan the product's whole life before shipping the first unit."
output: "lifecycle-plan.md"
used_by:
  - chief-hardware-officer-agent
---

# Product Lifecycle Planning

`hardware` · produces `lifecycle-plan.md` · used by `chief-hardware-officer-agent`

Plan the product's whole life before shipping the first unit.

## Procedure
1. Plan the revision strategy and how field units are supported across revisions.
2. Plan spares: what, how many, and for how long.
3. Plan service: what is repairable, by whom, and with what documentation.
4. Plan end of life: last-time-buy, final builds, and support commitments.
5. Plan disposal and recycling obligations per market.

## Output contract
`lifecycle-plan.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Spares and service planned before first shipment
- End-of-life and recycling obligations included
- The output states its confidence grade and names the evidence behind every load-bearing claim.
