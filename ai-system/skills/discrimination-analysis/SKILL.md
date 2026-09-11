---
name: discrimination-analysis
category: improvement
description: "Check the evaluation actually separates good from bad."
output: "discrimination-report.md"
used_by:
  - eval-designer
---

# Discrimination Analysis

`improvement` · produces `discrimination-report.md` · used by `eval-designer`

Check the evaluation actually separates good from bad.

## Procedure
1. Score a known-good and a known-bad example with the rubric.
2. Check the scores differ meaningfully.
3. Check the case set produces a spread rather than clustering at one score.
4. Identify cases everything passes and everything fails; both teach little.
5. Revise or retire non-discriminating cases and dimensions.

## Output contract
`discrimination-report.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Known-good and known-bad verified to separate
- Non-discriminating cases retired
- The output states its confidence grade and names the evidence behind every load-bearing claim.
