---
name: build-phase-gating
category: hardware
description: "Exit each build phase on evidence, not on schedule."
output: "phase-gate.md"
used_by:
  - hardware-head
---

# Build Phase Gating

`hardware` · produces `phase-gate.md` · used by `hardware-head`

Exit each build phase on evidence, not on schedule.

## Procedure
1. Define entry and exit criteria per phase before the phase starts.
2. Require the verification matrix results as exit evidence.
3. Decide explicitly: proceed, repeat the phase, or redesign.
4. Never cut tooling on an unfrozen design, whatever the schedule pressure.
5. Record the decision and the evidence that supported it.

## Output contract
`phase-gate.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Exit criteria defined before the phase starts
- Tooling never cut on an unfrozen design
- The output states its confidence grade and names the evidence behind every load-bearing claim.
