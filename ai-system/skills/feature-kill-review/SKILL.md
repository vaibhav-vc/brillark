---
name: feature-kill-review
category: product
description: "Decide whether a shipped feature earned its place."
output: "feature-review.md"
used_by:
  - cpo-agent
---

# Feature Kill Review

**Category:** `product` · **Output artifact:** `feature-review.md`

## What this skill does
Decide whether a shipped feature earned its place.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cpo-agent`.

## Procedure
1. Compare actual usage and outcome against the success signal set before launch.
2. Check whether failure is due to the feature or to its discovery.
3. Assess the maintenance cost of keeping it.
4. Decide to fix, keep, or remove — default to removal when the signal missed.
5. Record the decision and the evidence for the pattern library.

## Output contract
Write `feature-review.md` into `workspace/<venture-id>/product/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** feature-kill-review
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
- Compared against the pre-set signal
- Removal is the default on a miss
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `product` category
- Writing a requirement that starts with a solution instead of an evidenced problem.
- Shipping without defining, in advance, what would show it worked.
- Treating the roadmap as a promise rather than a current best sequence.
