---
name: model-recomputation
category: council
description: "Independently recompute a model's headline numbers before critiquing them."
output: "recomputation-report.md"
used_by:
  - council-economics-skeptic
---

# Model Recomputation

**Category:** `council` · **Output artifact:** `recomputation-report.md`

## What this skill does
Independently recompute a model's headline numbers before critiquing them.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-economics-skeptic`.

## Procedure
1. Rebuild the top three outputs from the stated inputs without looking at the original formulas.
2. Compare your result to the model's; investigate any difference.
3. Check the arithmetic of every percentage, ratio, and growth rate.
4. Verify that units and time periods are consistent throughout.
5. Report discrepancies with the corrected figure, not just the objection.

## Output contract
Write `recomputation-report.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** model-recomputation
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
- Rebuilt independently of the original formulas
- Discrepancies reported with corrected figures
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
