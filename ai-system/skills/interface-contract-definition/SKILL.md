---
name: interface-contract-definition
category: hardware
description: "Write down the boundaries between disciplines so they stop moving."
output: "interface-contract.md"
used_by:
  - hardware-head
---

# Interface Contract Definition

`hardware` · produces `interface-contract.md` · used by `hardware-head`

Write down the boundaries between disciplines so they stop moving.

## Procedure
1. Define each interface: mechanical volume, mounting, connectors, pinout, and protocol.
2. Name an owner on each side of every interface.
3. Record tolerances and what happens at the extremes.
4. Version the contract and treat changes as decisions with owners.
5. Verify the built hardware against the contract, not against intent.

## Output contract
`interface-contract.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Owner named on each side of every interface
- Built hardware verified against the contract
- The output states its confidence grade and names the evidence behind every load-bearing claim.
