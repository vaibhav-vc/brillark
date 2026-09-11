---
name: design-strategy-alignment
category: design
description: "Check the design direction actually serves the strategy."
output: "alignment-review.md"
used_by:
  - chief-design-officer-agent
---

# Design Strategy Alignment

**Category:** `design` · **Output artifact:** `alignment-review.md`

## What this skill does
Check the design direction actually serves the strategy.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-design-officer-agent`.

## Procedure
1. Restate the strategy and the customer it serves.
2. Check the design direction supports that customer's judgement criteria.
3. Identify where design is optimising something the strategy does not need.
4. Identify where the strategy requires an experience we cannot yet deliver.
5. Recommend the realignment explicitly.

## Output contract
Write `alignment-review.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** design-strategy-alignment
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
- Misaligned optimisation identified
- Undeliverable strategy requirements surfaced
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
