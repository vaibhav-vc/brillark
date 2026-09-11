---
name: structural-analysis
category: hardware
description: "Check the part survives the loads it will actually see."
output: "analysis-report.md"
used_by:
  - mechanical-engineer
---

# Structural Analysis

`hardware` · produces `analysis-report.md` · used by `mechanical-engineer`

Check the part survives the loads it will actually see.

## Procedure
1. Define load cases from real use, transport, and abuse.
2. Apply realistic constraints; over-constrained models give reassuring wrong answers.
3. Report margin against yield and against fatigue where cyclic.
4. Check the mesh and assumptions before trusting a result.
5. State the margin numerically rather than pass or fail.

## Output contract
`analysis-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Load cases drawn from real use and abuse
- Margins stated numerically
- The output states its confidence grade and names the evidence behind every load-bearing claim.
