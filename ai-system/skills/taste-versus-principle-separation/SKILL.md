---
name: taste-versus-principle-separation
category: design
description: "Tell apart a real problem and a personal preference."
output: "objection-triage.md"
used_by:
  - design-critic
---

# Taste Versus Principle Separation

`design` · produces `objection-triage.md` · used by `design-critic`

Tell apart a real problem and a personal preference.

## Procedure
1. Ask what evidence or principle supports the objection.
2. Check whether it would fail for a user or only differ from your choice.
3. Test the objection against the design system and research findings.
4. Drop preferences that do not affect the goal.
5. Record genuine principles so they become shared rather than repeated.

## Output contract
`objection-triage.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Preferences dropped when they do not affect the goal
- Principles recorded to become shared
- The output states its confidence grade and names the evidence behind every load-bearing claim.
