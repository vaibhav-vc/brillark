---
name: alternative-model-generation
category: market
description: "Generate genuinely different business models before committing to one."
output: "model-alternatives.md"
used_by:
  - business-model-canvas-agent
---

# Alternative Model Generation

**Category:** `market` · **Output artifact:** `model-alternatives.md`

## What this skill does
Generate genuinely different business models before committing to one.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `business-model-canvas-agent`.

## Procedure
1. Vary the revenue mechanism: subscription, usage, transaction, marketplace, licence.
2. Vary the customer: who else has this problem and more budget?
3. Vary the channel: direct, partner, embedded, self-serve.
4. Build at least two complete alternatives, not variations of one.
5. Compare on unit economics, speed to evidence, and defensibility.

## Output contract
Write `model-alternatives.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** alternative-model-generation
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
- Alternatives structurally different, not variants
- Compared on speed to evidence
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
