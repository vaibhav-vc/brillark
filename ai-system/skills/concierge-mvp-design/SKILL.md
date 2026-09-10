---
name: concierge-mvp-design
category: product
description: "Deliver the outcome manually before building the machine."
output: "concierge-design.md"
used_by:
  - mvp-scoper
---

# Concierge Mvp Design

**Category:** `product` · **Output artifact:** `concierge-design.md`

## What this skill does
Deliver the outcome manually before building the machine.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `mvp-scoper`.

## Procedure
1. Identify the outcome the customer wants, separate from the interface.
2. Design a manual process that delivers it end to end.
3. Set the volume ceiling at which manual becomes untenable.
4. Instrument what you learn from doing it by hand.
5. Automate only the steps the manual run proves are needed.

## Output contract
Write `concierge-design.md` into `workspace/<venture-id>/product/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** concierge-mvp-design
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
- Outcome delivered before automation
- Manual run instrumented for learning
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `product` category
- Writing a requirement that starts with a solution instead of an evidenced problem.
- Shipping without defining, in advance, what would show it worked.
- Treating the roadmap as a promise rather than a current best sequence.
