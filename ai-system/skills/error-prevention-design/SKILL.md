---
name: error-prevention-design
category: design
description: "Stop the error happening rather than reporting it afterwards."
output: "error-prevention-spec.md"
used_by:
  - interaction-designer
---

# Error Prevention Design

`design` · produces `error-prevention-spec.md` · used by `interaction-designer`

Stop the error happening rather than reporting it afterwards.

## Procedure
1. Identify the errors users actually make, from testing and support data.
2. Constrain the input so the invalid value cannot be entered.
3. Use good defaults so the common case needs no decision.
4. Confirm only destructive and irreversible actions; confirmation fatigue defeats itself.
5. Make every non-destructive action undoable rather than confirmed.

## Output contract
`error-prevention-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Constraints preferred over post-hoc validation
- Confirmation reserved for irreversible actions
- The output states its confidence grade and names the evidence behind every load-bearing claim.
