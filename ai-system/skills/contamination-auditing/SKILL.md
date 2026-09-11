---
name: contamination-auditing
category: improvement
description: "Check the measurement set has not leaked into development."
output: "contamination-audit.md"
used_by:
  - benchmark-curator
---

# Contamination Auditing

`improvement` · produces `contamination-audit.md` · used by `benchmark-curator`

Check the measurement set has not leaked into development.

## Procedure
1. Compare tuning and held-out sets for overlapping or near-duplicate cases.
2. Check whether held-out cases appear in any prompt or example.
3. Check whether results improved suspiciously fast after a variant round.
4. Quarantine any contaminated case and rebuild the split.
5. Record the audit and its outcome.

## Output contract
`contamination-audit.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Near-duplicates checked, not just exact matches
- Contaminated cases quarantined and split rebuilt
- The output states its confidence grade and names the evidence behind every load-bearing claim.
