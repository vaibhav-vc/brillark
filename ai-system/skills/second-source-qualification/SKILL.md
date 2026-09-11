---
name: second-source-qualification
category: hardware
description: "Make sure one supplier cannot stop the line."
output: "second-source-report.md"
used_by:
  - electronics-component-engineer
---

# Second Source Qualification

`hardware` · produces `second-source-report.md` · used by `electronics-component-engineer`

Make sure one supplier cannot stop the line.

## Procedure
1. Identify parts whose absence would halt production.
2. Find alternates and check them against the actual circuit requirements, not just the headline spec.
3. Test the alternate in hardware rather than approving on paper.
4. Approve and record the alternate on the BOM.
5. Re-check alternates when the design or the part changes.

## Output contract
`second-source-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Alternates tested in hardware, not approved on paper
- Line-stopping parts identified first
- The output states its confidence grade and names the evidence behind every load-bearing claim.
