---
name: golden-case-extraction
category: improvement
description: "Turn a real failure into a test that stops it recurring."
output: "golden-case.md"
used_by:
  - failure-miner
---

# Golden Case Extraction

`improvement` · produces `golden-case.md` · used by `failure-miner`

Turn a real failure into a test that stops it recurring.

## Procedure
1. Take the actual inputs and context from the failure.
2. Define what the correct output would have been, and why.
3. Strip anything sensitive while preserving the difficulty.
4. Verify the case fails against the current behaviour.
5. Add it to the suite with its provenance recorded.

## Output contract
`golden-case.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Case verified to fail before the fix
- Provenance recorded with each case
- The output states its confidence grade and names the evidence behind every load-bearing claim.
