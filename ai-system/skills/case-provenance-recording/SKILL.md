---
name: case-provenance-recording
category: improvement
description: "Record where each case came from and why its answer is right."
output: "case-provenance.md"
used_by:
  - benchmark-curator
---

# Case Provenance Recording

`improvement` · produces `case-provenance.md` · used by `benchmark-curator`

Record where each case came from and why its answer is right.

## Procedure
1. Record the source: a real task, a real failure, or a constructed edge case.
2. Record why the expected output is correct, in enough detail to be challenged.
3. Record who decided and when.
4. Note anything sanitised and whether difficulty was preserved.
5. Link the case to the failure it came from, where applicable.

## Output contract
`case-provenance.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Correctness justified, not just asserted
- Sanitisation noted with difficulty preserved
- The output states its confidence grade and names the evidence behind every load-bearing claim.
