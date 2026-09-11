---
name: state-handling-review
category: engineering
description: "Check the interface handles every state a user can encounter."
output: "state-review.md"
used_by:
  - frontend-implementation-agent
---

# State Handling Review

`engineering` · produces `state-review.md` · used by `frontend-implementation-agent`

Check the interface handles every state a user can encounter.

## Procedure
1. Enumerate the states: empty, loading, partial, error, and success.
2. Check each has a designed, implemented treatment.
3. Verify errors are recoverable and explain what to do.
4. Check behaviour on slow networks and interrupted requests.
5. Test the states directly rather than assuming they occur.

## Output contract
`state-review.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- All five states implemented
- Recovery path present for errors
- The output states its confidence grade and names the evidence behind every load-bearing claim.
