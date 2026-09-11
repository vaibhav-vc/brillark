---
name: process-selection
category: hardware
description: "Choose the manufacturing process for the real volume."
output: "process-decision.md"
used_by:
  - dfm-engineer
---

# Process Selection

`hardware` · produces `process-decision.md` · used by `dfm-engineer`

Choose the manufacturing process for the real volume.

## Procedure
1. Establish the volume forecast and its uncertainty.
2. Compare candidate processes on tooling cost, unit cost, and lead time.
3. Compute the crossover volume between candidates.
4. Check tolerance and finish capability, not just cost.
5. Recommend with the crossover stated, so a volume change can be re-decided.

## Output contract
`process-decision.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Crossover volume computed
- Tolerance capability checked alongside cost
- The output states its confidence grade and names the evidence behind every load-bearing claim.
