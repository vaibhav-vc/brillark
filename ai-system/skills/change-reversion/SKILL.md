---
name: change-reversion
category: improvement
description: "Undo a change that did not hold."
output: "reversion-record.md"
used_by:
  - improvement-head
---

# Change Reversion

`improvement` · produces `reversion-record.md` · used by `improvement-head`

Undo a change that did not hold.

## Procedure
1. Check the following cycle whether the measured gain persisted.
2. Compare against the recorded baseline, not against impression.
3. Revert cleanly to the logged previous version.
4. Record why it was reverted so it is not retried identically.
5. Re-open the underlying problem in the improvement queue.

## Output contract
`reversion-record.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Persistence checked in the following cycle
- Underlying problem reopened, not closed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
