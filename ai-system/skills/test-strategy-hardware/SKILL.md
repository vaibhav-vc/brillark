---
name: test-strategy-hardware
category: hardware
description: "Decide what gets tested at each build phase and why."
output: "hw-test-strategy.md"
used_by:
  - hardware-test-engineer
---

# Test Strategy Hardware

`hardware` · produces `hw-test-strategy.md` · used by `hardware-test-engineer`

Decide what gets tested at each build phase and why.

## Procedure
1. Define what each phase must prove: EVT feasibility, DVT design, PVT process.
2. Map requirements to the phase where each will be verified.
3. Define sample sizes and pass criteria before building.
4. Plan for failures: what happens when a test fails at each phase.
5. Define what would block progression to the next phase.

## Output contract
`hw-test-strategy.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Each phase has a distinct thing to prove
- Progression blockers defined in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.
