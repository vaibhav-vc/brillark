---
name: behaviour-preserving-refactor
category: engineering
description: "Change structure without changing behaviour."
output: "refactor-record.md"
used_by:
  - tech-debt-refactor-agent
---

# Behaviour Preserving Refactor

`engineering` · produces `refactor-record.md` · used by `tech-debt-refactor-agent`

Change structure without changing behaviour.

## Procedure
1. Establish characterisation tests for the current behaviour first.
2. Make one structural change at a time.
3. Never mix behaviour changes into a refactoring commit.
4. Run the full suite after each step.
5. If behaviour must change, do it as a separate, reviewed change.

## Output contract
`refactor-record.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Behaviour changes kept in separate commits
- Characterisation tests established first
- The output states its confidence grade and names the evidence behind every load-bearing claim.
