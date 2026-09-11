---
name: inter-rater-calibration
category: improvement
description: "Get different scorers to agree."
output: "calibration-report.md"
used_by:
  - eval-designer
---

# Inter Rater Calibration

`improvement` · produces `calibration-report.md` · used by `eval-designer`

Get different scorers to agree.

## Procedure
1. Have multiple scorers rate the same sample independently.
2. Measure agreement per dimension, not just overall.
3. Discuss the disagreements and find the ambiguity in the rubric.
4. Revise the anchors rather than asking scorers to try harder.
5. Re-measure agreement after the revision.

## Output contract
`calibration-report.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Agreement measured per dimension
- Rubric revised rather than exhorting scorers
- The output states its confidence grade and names the evidence behind every load-bearing claim.
