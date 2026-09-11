---
name: fix-verification
category: design
description: "Confirm the fix actually fixed it."
output: "retest-report.md"
used_by:
  - usability-tester
---

# Fix Verification

`design` · produces `retest-report.md` · used by `usability-tester`

Confirm the fix actually fixed it.

## Procedure
1. Retest the same task with fresh participants from the same segment.
2. Compare against the prior round's success rate and error count.
3. Check whether the fix created a new problem elsewhere in the flow.
4. Close the finding only when the retest passes.
5. Record the before and after so the change's value is visible.

## Output contract
`retest-report.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Retested with fresh participants
- Closure requires a passing retest
- The output states its confidence grade and names the evidence behind every load-bearing claim.
