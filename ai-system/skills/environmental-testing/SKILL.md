---
name: environmental-testing
category: hardware
description: "Test the conditions the product will actually meet."
output: "environmental-report.md"
used_by:
  - hardware-test-engineer
---

# Environmental Testing

`hardware` · produces `environmental-report.md` · used by `hardware-test-engineer`

Test the conditions the product will actually meet.

## Procedure
1. Define the environmental profile from the real use and shipping conditions.
2. Test temperature, humidity, and thermal cycling to the profile.
3. Test ingress, corrosion, and chemical exposure where relevant.
4. Run long enough to expose degradation, not just survival.
5. Inspect after test for damage that still functions but will not last.

## Output contract
`environmental-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Profile drawn from real use and shipping
- Post-test inspection for latent damage
- The output states its confidence grade and names the evidence behind every load-bearing claim.
