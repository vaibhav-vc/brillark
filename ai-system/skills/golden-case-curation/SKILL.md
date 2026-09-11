---
name: golden-case-curation
category: orchestration
description: "Maintain the reference examples that define good output."
output: "golden-cases.md"
used_by:
  - benchmark-curator
  - evaluation-harness-agent
---

# Golden Case Curation

`orchestration` · produces `golden-cases.md` · used by `benchmark-curator`, `evaluation-harness-agent`

Maintain the reference examples that define good output.

## Procedure
1. Choose cases that discriminate — a case everything passes teaches nothing.
2. Include at least one historical failure per agent.
3. Record why each case's expected output is correct.
4. Review annually and retire cases that no longer discriminate.
5. Keep the set small enough to run on every change.

## Output contract
`golden-cases.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Every case discriminates
- Historical failures represented
- The output states its confidence grade and names the evidence behind every load-bearing claim.
