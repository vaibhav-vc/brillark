---
name: input-validation-review
category: engineering
description: "Check that untrusted input cannot get through unchecked."
output: "validation-review.md"
used_by:
  - backend-implementation-agent
---

# Input Validation Review

`engineering` · produces `validation-review.md` · used by `backend-implementation-agent`

Check that untrusted input cannot get through unchecked.

## Procedure
1. Identify every entry point where external data arrives.
2. Verify validation happens at the boundary, before use.
3. Check type, range, length, format, and encoding.
4. Verify rejection is explicit and does not leak internals.
5. Test with malformed, oversized, and hostile input.

## Output contract
`validation-review.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Validation at the boundary, not deep inside
- Hostile input tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.
