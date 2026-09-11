---
name: termination-and-topology-design
category: hardware
description: "Control reflections before they become errors."
output: "termination-spec.md"
used_by:
  - signal-integrity-engineer
---

# Termination And Topology Design

`hardware` · produces `termination-spec.md` · used by `signal-integrity-engineer`

Control reflections before they become errors.

## Procedure
1. Determine whether each net is electrically long for its edge rate.
2. Choose the topology: point-to-point, daisy chain, or star, with reasons.
3. Select termination type and value for the driver and the topology.
4. Check the termination's power and space cost against the benefit.
5. Simulate or measure the resulting waveform at the receiver.

## Output contract
`termination-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Electrical length assessed against edge rate
- Waveform checked at the receiver
- The output states its confidence grade and names the evidence behind every load-bearing claim.
