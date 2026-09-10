---
name: deal-structuring
category: gtm
description: "Structure an agreement that is testable before it is binding."
output: "deal-structure.md"
used_by:
  - partnership-bd-agent
---

# Deal Structuring

**Category:** `gtm` · **Output artifact:** `deal-structure.md`

## What this skill does
Structure an agreement that is testable before it is binding.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `partnership-bd-agent`.

## Procedure
1. Start with the smallest structure that tests the thesis.
2. Define the commitments on both sides concretely.
3. Avoid exclusivity before evidence exists.
4. Set success metrics and a review date inside the agreement.
5. Define the exit and what happens to customers if it ends.

## Output contract
Write `deal-structure.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** deal-structuring
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
- No exclusivity before evidence
- Exit terms defined up front
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
