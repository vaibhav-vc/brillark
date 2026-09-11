---
name: resolution-drafting
category: compliance
description: "Draft a resolution that is unambiguous and effective."
output: "resolution.md"
used_by:
  - corporate-secretary-agent
---

# Resolution Drafting

`compliance` · produces `resolution.md` · used by `corporate-secretary-agent`

Draft a resolution that is unambiguous and effective.

## Procedure
1. State the action being authorised precisely.
2. State the authority under which it is made.
3. Name who is authorised to execute it and within what limits.
4. Include the effective date and any conditions.
5. Check consistency with the governing documents before adoption.

## Output contract
`resolution.md` → `workspace/<venture-id>/compliance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/compliance.tsv`.

## Quality bar
- Execution authority named with limits
- Consistency with governing documents checked
- The output states its confidence grade and names the evidence behind every load-bearing claim.
