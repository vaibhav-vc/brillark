---
name: realtime-timing-verification
category: hardware
description: "Measure the timing rather than reasoning about it."
output: "timing-report.md"
used_by:
  - embedded-firmware-engineer
---

# Realtime Timing Verification

`hardware` · produces `timing-report.md` · used by `embedded-firmware-engineer`

Measure the timing rather than reasoning about it.

## Procedure
1. Identify the deadlines that actually matter to product behaviour.
2. Instrument entry and exit of critical paths with a measurable output.
3. Measure worst-case latency under full load, not average under idle.
4. Check interrupt latency and priority inversion explicitly.
5. Record margins against the deadlines.

## Output contract
`timing-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Worst case measured under full load
- Interrupt latency and inversion checked
- The output states its confidence grade and names the evidence behind every load-bearing claim.
