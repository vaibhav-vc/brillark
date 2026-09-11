---
name: negative-result-reporting
category: improvement
description: "Report what did not work, as prominently as what did."
output: "negative-results.md"
used_by:
  - ab-test-runner
---

# Negative Result Reporting

`improvement` · produces `negative-results.md` · used by `ab-test-runner`

Report what did not work, as prominently as what did.

## Procedure
1. Report failed variants with the hypothesis they tested.
2. State what the negative result rules out.
3. Record it so the same variant is not retried blindly.
4. Resist reframing a null result as a partial success.
5. Feed the learning into the next round of variants.

## Output contract
`negative-results.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Null results not reframed as partial success
- Ruled-out hypotheses recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.
