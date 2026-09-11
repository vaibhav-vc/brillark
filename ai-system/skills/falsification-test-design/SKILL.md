---
name: falsification-test-design
category: council
description: "Define what would prove the plan wrong."
output: "falsification-test.md"
used_by:
  - council-devils-advocate
---

# Falsification Test Design

`council` · produces `falsification-test.md` · used by `council-devils-advocate`

Define what would prove the plan wrong.

## Procedure
1. State the claim precisely enough to be tested.
2. Define the observation that would disprove it.
3. Set the threshold and the timeframe.
4. Check the test is affordable and would actually be run.
5. If no falsifying observation exists, report that as the finding.

## Output contract
`falsification-test.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Threshold and timeframe both defined
- Unfalsifiable claims reported as findings
- The output states its confidence grade and names the evidence behind every load-bearing claim.
