---
name: qualification-framework
category: gtm
description: "Decide quickly whether a deal is real."
output: "qualification-framework.md"
used_by:
  - sales-playbook-agent
---

# Qualification Framework

**Category:** `gtm` · **Output artifact:** `qualification-framework.md`

## What this skill does
Decide quickly whether a deal is real.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `sales-playbook-agent`.

## Procedure
1. Define the qualification dimensions: need, authority, budget, timing, and fit.
2. Write the question that tests each dimension without interrogating.
3. Set the threshold below which a deal is disqualified.
4. Require evidence, not the seller's impression, per dimension.
5. Track how qualification score predicted actual outcomes and recalibrate.

## Output contract
Write `qualification-framework.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** qualification-framework
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
- Evidence required per dimension
- Predictive accuracy tracked
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
