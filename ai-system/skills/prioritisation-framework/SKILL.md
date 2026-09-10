---
name: prioritisation-framework
category: product
description: "Apply one consistent method to decide what gets built next."
output: "prioritisation.md"
used_by:
  - cpo-agent
---

# Prioritisation Framework

**Category:** `product` · **Output artifact:** `prioritisation.md`

## What this skill does
Apply one consistent method to decide what gets built next.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cpo-agent`.

## Procedure
1. Score each candidate on evidence of pain, reach, and strategic fit.
2. Divide by cost to learn, not cost to build fully.
3. Apply the same method to every candidate, including the CEO's.
4. Publish the scores so the ranking can be argued with facts.
5. Recalibrate when a shipped item's outcome contradicts its score.

## Output contract
Write `prioritisation.md` into `workspace/<venture-id>/product/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** prioritisation-framework
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
- Same method applied to every candidate
- Scores published and challengeable
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `product` category
- Writing a requirement that starts with a solution instead of an evidenced problem.
- Shipping without defining, in advance, what would show it worked.
- Treating the roadmap as a promise rather than a current best sequence.
