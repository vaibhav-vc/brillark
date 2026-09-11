---
name: library-overlap-analysis
category: improvement
description: "Find skills that have blurred into each other, and gaps between them."
output: "overlap-report.md"
used_by:
  - skill-refiner
---

# Library Overlap Analysis

`improvement` · produces `overlap-report.md` · used by `skill-refiner`

Find skills that have blurred into each other, and gaps between them.

## Procedure
1. Compare skills within a category for overlapping procedures.
2. Check whether agents actually distinguish them in practice.
3. Identify decisions no skill currently covers.
4. Recommend merge, split, or leave alone — most should be left alone.
5. Check every reference before recommending a merge.

## Output contract
`overlap-report.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Practical distinguishability tested, not just textual similarity
- References checked before merge
- The output states its confidence grade and names the evidence behind every load-bearing claim.
