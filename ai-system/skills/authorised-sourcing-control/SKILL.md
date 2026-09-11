---
name: authorised-sourcing-control
category: hardware
description: "Buy only what you can trace."
output: "sourcing-record.md"
used_by:
  - electronics-component-engineer
---

# Authorised Sourcing Control

`hardware` · produces `sourcing-record.md` · used by `electronics-component-engineer`

Buy only what you can trace.

## Procedure
1. Buy through the manufacturer or authorised distribution.
2. Require traceability documentation for every lot.
3. Treat broker purchases as a last resort with incoming inspection.
4. Inspect and test incoming parts where counterfeiting risk is real.
5. Record the source for every lot so a field failure can be traced.

## Output contract
`sourcing-record.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Traceability documented per lot
- Broker purchases inspected, not assumed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
