---
name: process-capability-analysis
category: hardware
description: "Design inside what the supplier can actually hold."
output: "capability-report.md"
used_by:
  - dfm-engineer
---

# Process Capability Analysis

`hardware` · produces `capability-report.md` · used by `dfm-engineer`

Design inside what the supplier can actually hold.

## Procedure
1. Request capability data for the specific process and feature type.
2. Compare required tolerances against the demonstrated capability.
3. Identify features requiring capability the supplier does not have.
4. Either relax the tolerance or change supplier — do not hope.
5. Record the capability assumption with the drawing.

## Output contract
`capability-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Requirements compared to demonstrated data
- Unsupportable tolerances resolved, not hoped over
- The output states its confidence grade and names the evidence behind every load-bearing claim.
