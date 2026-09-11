---
name: rubric-design
category: improvement
description: "Build a scoring scheme different reviewers apply the same way."
output: "rubric.md"
used_by:
  - eval-designer
---

# Rubric Design

`improvement` · produces `rubric.md` · used by `eval-designer`

Build a scoring scheme different reviewers apply the same way.

## Procedure
1. Define independent dimensions; overlapping ones double-count.
2. Anchor every score level with a real example.
3. Avoid dimensions that reduce to overall impression.
4. Pilot on a small sample and check agreement.
5. Revise or drop dimensions where scorers persistently disagree.

## Output contract
`rubric.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Every level anchored with a real example
- Disagreeing dimensions dropped
- The output states its confidence grade and names the evidence behind every load-bearing claim.
