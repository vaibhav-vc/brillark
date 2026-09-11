---
name: policy-authoring
category: compliance
description: "Write a policy people can actually follow."
output: "policy.md"
used_by:
  - chief-compliance-officer-agent
---

# Policy Authoring

`compliance` · produces `policy.md` · used by `chief-compliance-officer-agent`

Write a policy people can actually follow.

## Procedure
1. State the scope, who it applies to, and what it requires.
2. Write requirements as observable behaviours, not aspirations.
3. Define exceptions and how they are approved.
4. Assign an owner and a review date.
5. Test comprehension with someone who must follow it.

## Output contract
`policy.md` → `workspace/<venture-id>/compliance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/compliance.tsv`.

## Quality bar
- Requirements are observable behaviours
- Comprehension tested with an actual user
- The output states its confidence grade and names the evidence behind every load-bearing claim.
