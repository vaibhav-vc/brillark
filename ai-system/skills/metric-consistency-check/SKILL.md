---
name: metric-consistency-check
category: compliance
description: "Verify a reported metric means the same thing it did last period."
output: "consistency-check.md"
used_by:
  - investor-reporting-agent
---

# Metric Consistency Check

`compliance` · produces `consistency-check.md` · used by `investor-reporting-agent`

Verify a reported metric means the same thing it did last period.

## Procedure
1. Compare the current definition to the one used previously.
2. Check the source data and the filters have not changed.
3. Identify any restatement and disclose it explicitly.
4. Verify the same number appears identically across documents.
5. Block publication until inconsistencies are resolved.

## Output contract
`consistency-check.md` → `workspace/<venture-id>/compliance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/compliance.tsv`.

## Quality bar
- Restatements disclosed explicitly
- Cross-document consistency verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
