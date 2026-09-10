---
name: competitive-kill-scenario
category: council
description: "Describe how a competitor could destroy this business."
output: "kill-scenario.md"
used_by:
  - council-red-team
---

# Competitive Kill Scenario

**Category:** `council` · **Output artifact:** `kill-scenario.md`

## What this skill does
Describe how a competitor could destroy this business.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-red-team`.

## Procedure
1. Identify the competitor best positioned to attack, including a large incumbent.
2. Describe the specific move: bundling, pricing, acquisition, or copying.
3. Estimate how long it would take them and what it would cost.
4. Identify what would make it not worth their while.
5. Define the early indicator that the move has started.

## Output contract
Write `kill-scenario.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** competitive-kill-scenario
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
- Move described concretely with cost and timing
- Early indicator defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
