---
name: ergonomics-and-human-factors
category: hardware
description: "Fit the product to the range of people who will actually use it."
output: "ergonomics-report.md"
used_by:
  - industrial-designer
---

# Ergonomics And Human Factors

`hardware` · produces `ergonomics-report.md` · used by `industrial-designer`

Fit the product to the range of people who will actually use it.

## Procedure
1. Identify the postures, grips, and forces the product requires.
2. Check dimensions against anthropometric ranges, not a single average user.
3. Check reach, visibility, and control actuation for the extremes of the range.
4. Check the product one-handed, with gloves, and while moving where relevant.
5. Verify with physical mock-ups and real users before detailing.

## Output contract
`ergonomics-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Checked against a range, not an average user
- Verified with physical mock-ups
- The output states its confidence grade and names the evidence behind every load-bearing claim.
