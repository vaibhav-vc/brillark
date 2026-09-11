---
name: capability-mapping
category: improvement
description: "Know what the organisation can and cannot currently do."
output: "capability-map.md"
used_by:
  - capability-gap-scout
---

# Capability Mapping

`improvement` · produces `capability-map.md` · used by `capability-gap-scout`

Know what the organisation can and cannot currently do.

## Procedure
1. List the capabilities the current workflows require.
2. Map each to the agent and skills that provide it.
3. Mark capabilities with no owner and those with only one.
4. Mark capabilities provided but never exercised.
5. Publish the map so gaps are visible before they cause failures.

## Output contract
`capability-map.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Unowned and single-owner capabilities marked
- Unexercised capabilities identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
