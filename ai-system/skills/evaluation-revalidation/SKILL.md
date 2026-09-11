---
name: evaluation-revalidation
category: improvement
description: "Re-check the evaluation when the job changes."
output: "revalidation-record.md"
used_by:
  - eval-designer
---

# Evaluation Revalidation

`improvement` · produces `revalidation-record.md` · used by `eval-designer`

Re-check the evaluation when the job changes.

## Procedure
1. Check whether the agent's charter or skills changed since the rubric was written.
2. Check whether the case set still reflects the real task mix.
3. Re-run discrimination analysis.
4. Retire criteria that no longer apply and add ones that now do.
5. Record the revalidation date.

## Output contract
`revalidation-record.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Case set re-checked against the real task mix
- Revalidation date recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.
