---
name: pre-compliance-testing
category: hardware
description: "Find the failures before the accredited lab does."
output: "precompliance-report.md"
used_by:
  - compliance-emc-engineer
---

# Pre Compliance Testing

`hardware` · produces `precompliance-report.md` · used by `compliance-emc-engineer`

Find the failures before the accredited lab does.

## Procedure
1. Test on real hardware in a representative configuration with real cables.
2. Scan emissions across the required range and compare to the limit with margin.
3. Test immunity for the interfaces most likely to fail.
4. Identify the source of each excursion rather than masking it.
5. Retest after every fix and before booking the accredited lab.

## Output contract
`precompliance-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Tested with real cables and configuration
- Excursions traced to source rather than masked
- The output states its confidence grade and names the evidence behind every load-bearing claim.
