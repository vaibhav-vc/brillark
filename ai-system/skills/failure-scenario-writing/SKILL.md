---
name: failure-scenario-writing
category: council
description: "Turn an objection into a specific, checkable failure."
output: "failure-scenario.md"
used_by:
  - council-red-team
---

# Failure Scenario Writing

`council` · produces `failure-scenario.md` · used by `council-red-team`

Turn an objection into a specific, checkable failure.

## Procedure
1. State the precondition under which the failure occurs.
2. Describe the sequence of events step by step.
3. State the observable consequence and who suffers it.
4. Estimate likelihood in our actual context.
5. Drop the objection if the sequence cannot be written concretely.

## Output contract
`failure-scenario.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Concrete sequence, not an adjective
- Objections without a sequence dropped
- The output states its confidence grade and names the evidence behind every load-bearing claim.
