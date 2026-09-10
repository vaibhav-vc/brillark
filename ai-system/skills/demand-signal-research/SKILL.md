---
name: demand-signal-research
category: market
description: "Find evidence that demand exists in behaviour rather than in opinion."
output: "demand-signals.md"
used_by:
  - market-researcher
---

# Demand Signal Research

**Category:** `market` · **Output artifact:** `demand-signals.md`

## What this skill does
Find evidence that demand exists in behaviour rather than in opinion.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `market-researcher`.

## Procedure
1. Look for money already being spent on the problem, including on workarounds.
2. Examine search behaviour, community discussion, and support forums.
3. Count job postings, tooling adoption, and other proxies for organisational spend.
4. Distinguish curiosity signals from purchase signals.
5. Report the strongest three signals and what would falsify them.

## Output contract
Write `demand-signals.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** demand-signal-research
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
- Signals are behavioural, not stated intent
- Falsification condition stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
