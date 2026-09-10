---
name: network-effect-analysis
category: council
description: "Test whether a claimed network effect is real."
output: "network-effect-analysis.md"
used_by:
  - council-expansion-scout
---

# Network Effect Analysis

**Category:** `council` · **Output artifact:** `network-effect-analysis.md`

## What this skill does
Test whether a claimed network effect is real.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-expansion-scout`.

## Procedure
1. Specify who gains value when who else joins — direct, indirect, or local.
2. Check whether the effect is actually present at current scale or merely hoped for.
3. Identify the critical mass required for it to matter.
4. Assess whether it is local or global; local effects are weaker but reachable.
5. Identify what could disintermediate it.

## Output contract
Write `network-effect-analysis.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** network-effect-analysis
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
- Effect verified at current scale
- Critical mass quantified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
