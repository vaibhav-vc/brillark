---
name: candidate-trial
category: research
description: "Actually use the thing before recommending it."
output: "trial-report.md"
used_by:
  - technology-evaluator
---

# Candidate Trial

`research` · produces `trial-report.md` · used by `technology-evaluator`

Actually use the thing before recommending it.

## Procedure
1. Define a representative task that exercises the real requirements.
2. Trial the top candidates on the same task under the same conditions.
3. Record friction, failure modes, and what the documentation omitted.
4. Test the unhappy path, not just the tutorial.
5. Report the trial findings separately from the marketing claims.

## Output contract
`trial-report.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Same representative task across candidates
- Unhappy path exercised
- The output states its confidence grade and names the evidence behind every load-bearing claim.
