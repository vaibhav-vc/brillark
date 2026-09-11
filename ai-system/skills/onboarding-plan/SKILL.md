---
name: onboarding-plan
category: people
description: "Make a new team member productive in their first week."
output: "onboarding-plan.md"
used_by:
  - chro-agent
---

# Onboarding Plan

`people` · produces `onboarding-plan.md` · used by `chro-agent`

Make a new team member productive in their first week.

## Procedure
1. Define the contribution they should make in week one.
2. Sequence context: mission, customers, system, then codebase or process.
3. Assign an owner responsible for their first two weeks.
4. Give them a real, small piece of work immediately.
5. Collect their questions and fix the documentation they exposed.

## Output contract
`onboarding-plan.md` → `workspace/<venture-id>/people/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/people.tsv`.

## Quality bar
- Week-one contribution defined
- Documentation improved from their questions
- The output states its confidence grade and names the evidence behind every load-bearing claim.
