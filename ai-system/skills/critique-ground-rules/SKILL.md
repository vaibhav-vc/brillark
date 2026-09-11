---
name: critique-ground-rules
category: design
description: "Set the rules that make critique safe and useful."
output: "ground-rules.md"
used_by:
  - design-critic
---

# Critique Ground Rules

`design` · produces `ground-rules.md` · used by `design-critic`

Set the rules that make critique safe and useful.

## Procedure
1. State that the work is being critiqued, not the designer.
2. Require the goal before the feedback.
3. Ban solutioning over the designer and rank-based override.
4. Give quieter participants a structured turn.
5. Time-box and close with recorded decisions.

## Output contract
`ground-rules.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Rank-based override explicitly banned
- Structured turn for quieter participants
- The output states its confidence grade and names the evidence behind every load-bearing claim.
