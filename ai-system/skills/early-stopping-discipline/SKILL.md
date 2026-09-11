---
name: early-stopping-discipline
category: improvement
description: "Do not stop the trial when it starts looking good."
output: "trial-log.md"
used_by:
  - ab-test-runner
---

# Early Stopping Discipline

`improvement` · produces `trial-log.md` · used by `ab-test-runner`

Do not stop the trial when it starts looking good.

## Procedure
1. Commit to the planned sample before starting.
2. Do not inspect interim results unless a stopping rule was defined in advance.
3. If you must stop early, record it and treat the result as provisional.
4. Re-run to the full sample before adopting anything.
5. Record any deviation from the plan alongside the result.

## Output contract
`trial-log.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Interim inspection only under a pre-defined rule
- Early stops recorded and treated as provisional
- The output states its confidence grade and names the evidence behind every load-bearing claim.
