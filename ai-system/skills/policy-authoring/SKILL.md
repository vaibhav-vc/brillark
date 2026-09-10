---
name: policy-authoring
category: compliance
description: "Write a policy people can actually follow."
output: "policy.md"
used_by:
  - chief-compliance-officer-agent
---

# Policy Authoring

**Category:** `compliance` · **Output artifact:** `policy.md`

## What this skill does
Write a policy people can actually follow.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-compliance-officer-agent`.

## Procedure
1. State the scope, who it applies to, and what it requires.
2. Write requirements as observable behaviours, not aspirations.
3. Define exceptions and how they are approved.
4. Assign an owner and a review date.
5. Test comprehension with someone who must follow it.

## Output contract
Write `policy.md` into `workspace/<venture-id>/compliance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** policy-authoring
- **Author agent:** <agent-id>
- **Date:** <ISO-8601>
- **Confidence:** measured | sourced | benchmarked | estimated | guessed

## Summary
<the answer in three sentences or fewer>

## Body
<the substance produced by the procedure above>

## Evidence
| Claim | Source | Grade |
|---|---|---|

## Open questions
<what remains unknown, and who could answer it>

## Next action
<the single next step and its owner>
```

## Quality bar
- Requirements are observable behaviours
- Comprehension tested with an actual user
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `compliance` category
- Writing a policy nobody can follow and treating publication as compliance.
- Collecting evidence at audit time rather than as the control operates.
- Building controls for a framework that was never shown to apply.
