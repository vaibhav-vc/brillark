---
name: cascade-analysis
category: council
description: "Find failures that trigger other failures."
output: "cascade-analysis.md"
used_by:
  - council-risk-and-failure-modes
---

# Cascade Analysis

**Category:** `council` · **Output artifact:** `cascade-analysis.md`

## What this skill does
Find failures that trigger other failures.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-risk-and-failure-modes`.

## Procedure
1. Map the dependencies between failure modes.
2. Identify single failures that would trigger three or more others.
3. Estimate the combined impact of each cascade.
4. Identify the circuit breaker that would stop the chain.
5. Prioritise mitigations at the cascade origin.

## Output contract
Write `cascade-analysis.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** cascade-analysis
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
- Cascade chains explicitly mapped
- Circuit breakers identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
