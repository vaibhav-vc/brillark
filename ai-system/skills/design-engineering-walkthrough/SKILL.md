---
name: design-engineering-walkthrough
category: design
description: "Walk the spec with engineering before handoff, not after."
output: "walkthrough-notes.md"
used_by:
  - interaction-designer
---

# Design Engineering Walkthrough

`design` · produces `walkthrough-notes.md` · used by `interaction-designer`

Walk the spec with engineering before handoff, not after.

## Procedure
1. Walk the flow state by state with the engineer who will build it.
2. Ask what is expensive, what is impossible, and what is ambiguous.
3. Resolve the ambiguities in the spec during the session rather than in tickets later.
4. Agree which states are in scope for the first implementation.
5. Record the agreed simplifications and why they are acceptable.

## Output contract
`walkthrough-notes.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Ambiguities resolved in the session
- Agreed simplifications recorded with reasons
- The output states its confidence grade and names the evidence behind every load-bearing claim.
