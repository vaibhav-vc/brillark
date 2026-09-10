---
name: success-signal-definition
category: product
description: "Define in advance what would show a feature worked."
output: "success-signal.md"
used_by:
  - product-requirements-agent
---

# Success Signal Definition

**Category:** `product` · **Output artifact:** `success-signal.md`

## What this skill does
Define in advance what would show a feature worked.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `product-requirements-agent`.

## Procedure
1. Name the single metric that should move if this succeeds.
2. State the baseline and the threshold that counts as success.
3. Set the measurement window and the required sample.
4. Define what would show it failed, and what happens then.
5. Instrument before launch, not after.

## Output contract
Write `success-signal.md` into `workspace/<venture-id>/product/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** success-signal-definition
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
- Threshold and window set in advance
- Failure response defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `product` category
- Writing a requirement that starts with a solution instead of an evidenced problem.
- Shipping without defining, in advance, what would show it worked.
- Treating the roadmap as a promise rather than a current best sequence.
