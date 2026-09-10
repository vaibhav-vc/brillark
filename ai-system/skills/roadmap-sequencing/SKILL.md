---
name: roadmap-sequencing
category: product
description: "Order the roadmap for learning value rather than for tidiness."
output: "roadmap.md"
used_by:
  - cpo-agent
---

# Roadmap Sequencing

**Category:** `product` · **Output artifact:** `roadmap.md`

## What this skill does
Order the roadmap for learning value rather than for tidiness.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cpo-agent`.

## Procedure
1. Identify what each item would teach us, not just what it would deliver.
2. Sequence the highest-uncertainty, highest-dependency items early.
3. Check capacity honestly against the sequence.
4. Group items that share technical foundations.
5. State what each quarter's sequence assumes and what would reorder it.

## Output contract
Write `roadmap.md` into `workspace/<venture-id>/product/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** roadmap-sequencing
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
- Sequenced by learning value
- Capacity checked against the sequence
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `product` category
- Writing a requirement that starts with a solution instead of an evidenced problem.
- Shipping without defining, in advance, what would show it worked.
- Treating the roadmap as a promise rather than a current best sequence.
