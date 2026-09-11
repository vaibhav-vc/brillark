---
name: supply-chain-resilience-review
category: hardware
description: "Find where the supply chain would break."
output: "resilience-review.md"
used_by:
  - chief-hardware-officer-agent
---

# Supply Chain Resilience Review

`hardware` · produces `resilience-review.md` · used by `chief-hardware-officer-agent`

Find where the supply chain would break.

## Procedure
1. Map the chain to the sub-tier for critical components.
2. Identify single points of failure: sole sources, single regions, single processes.
3. Assess the time to recover from each failure.
4. Hold buffer or qualify alternates where recovery time exceeds tolerance.
5. Re-review when volumes, suppliers, or geopolitics change.

## Output contract
`resilience-review.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Mapped to sub-tier for critical components
- Recovery time assessed per failure point
- The output states its confidence grade and names the evidence behind every load-bearing claim.
