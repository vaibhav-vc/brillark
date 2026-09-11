---
name: hardware-strategy
category: hardware
description: "Decide whether and how to be a hardware company."
output: "hardware-strategy.md"
used_by:
  - chief-hardware-officer-agent
---

# Hardware Strategy

`hardware` · produces `hardware-strategy.md` · used by `chief-hardware-officer-agent`

Decide whether and how to be a hardware company.

## Procedure
1. Challenge whether hardware is required to deliver the value at all.
2. Compare building, licensing, and partnering on capital, control, and speed.
3. Model the cash cycle: hardware consumes cash long before it returns it.
4. Assess the capability required against the capability available.
5. Record the decision and what would reverse it.

## Output contract
`hardware-strategy.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Hardware necessity challenged before capital is committed
- Cash cycle modelled, not just unit margin
- The output states its confidence grade and names the evidence behind every load-bearing claim.
