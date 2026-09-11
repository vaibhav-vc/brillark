---
name: cheapest-test-design
category: council
description: "Find the least expensive way to check a critical assumption."
output: "test-design.md"
used_by:
  - council-assumption-auditor
---

# Cheapest Test Design

`council` · produces `test-design.md` · used by `council-assumption-auditor`

Find the least expensive way to check a critical assumption.

## Procedure
1. State exactly what needs to be known and to what confidence.
2. List possible tests from cheapest to most expensive.
3. Check whether an existing source already answers it.
4. Choose the cheapest test that would actually change the decision.
5. Define the decision rule before running it.

## Output contract
`test-design.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Existing sources checked before new tests
- Decision rule set in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.
