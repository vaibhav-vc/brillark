---
name: thermal-interface-selection
category: hardware
description: "Choose the material at the contact, where most thermal designs fail."
output: "interface-spec.md"
used_by:
  - thermal-engineer
---

# Thermal Interface Selection

`hardware` · produces `interface-spec.md` · used by `thermal-engineer`

Choose the material at the contact, where most thermal designs fail.

## Procedure
1. Compute the required interface conductance from the path analysis.
2. Select for the real gap and its tolerance range, not the nominal gap.
3. Check pressure, pump-out, dry-out, and long-term degradation.
4. Specify application method and thickness so production can repeat it.
5. Verify performance after thermal cycling, not only when fresh.

## Output contract
`interface-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Selected for the gap tolerance range
- Performance verified after cycling
- The output states its confidence grade and names the evidence behind every load-bearing claim.
