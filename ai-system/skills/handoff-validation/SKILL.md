---
name: handoff-validation
category: orchestration
description: "Check that arriving work is complete before accepting it."
output: "handoff-record.md"
used_by:
  - handoff-coordinator
---

# Handoff Validation

`orchestration` · produces `handoff-record.md` · used by `handoff-coordinator`

Check that arriving work is complete before accepting it.

## Procedure
1. Check the artifact exists and matches the agreed format.
2. Verify the definition of done was met, item by item.
3. Confirm assumptions and open questions are stated.
4. Reject immediately with the specific gap if anything is missing.
5. Record acceptance, so responsibility transfers cleanly.

## Output contract
`handoff-record.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Rejection names the specific gap
- Acceptance recorded explicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.
