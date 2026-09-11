---
name: comparability-checking
category: research
description: "Check two figures can honestly sit side by side."
output: "comparability-notes.md"
used_by:
  - data-sourcing-analyst
---

# Comparability Checking

`research` · produces `comparability-notes.md` · used by `data-sourcing-analyst`

Check two figures can honestly sit side by side.

## Procedure
1. Compare the definitions behind each figure, not just their labels.
2. Check the time periods align, including partial periods.
3. Check the populations and geographies match.
4. Check for methodology changes between editions of the same series.
5. Refuse the comparison, or state the caveat prominently, when they do not match.

## Output contract
`comparability-notes.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Definitions compared, not labels
- Mismatched comparisons refused or caveated prominently
- The output states its confidence grade and names the evidence behind every load-bearing claim.
