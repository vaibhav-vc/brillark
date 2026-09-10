---
name: time-to-user-estimation
category: product
description: "Estimate honestly when a real user will touch this."
output: "time-to-user.md"
used_by:
  - mvp-scoper
---

# Time To User Estimation

**Category:** `product` · **Output artifact:** `time-to-user.md`

## What this skill does
Estimate honestly when a real user will touch this.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `mvp-scoper`.

## Procedure
1. Break the path to first user into its required steps.
2. Estimate each from historical throughput, not optimism.
3. Include the non-build steps: review, deploy, and access.
4. State the estimate as a range with the assumptions behind each end.
5. Track the actual against the estimate to calibrate the next one.

## Output contract
Write `time-to-user.md` into `workspace/<venture-id>/product/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** time-to-user-estimation
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
- Non-build steps included
- Estimate calibrated against past actuals
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `product` category
- Writing a requirement that starts with a solution instead of an evidenced problem.
- Shipping without defining, in advance, what would show it worked.
- Treating the roadmap as a promise rather than a current best sequence.
