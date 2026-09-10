---
name: severity-normalisation
category: council
description: "Make severity consistent across different critics."
output: "normalised-severities.md"
used_by:
  - council-synthesis-arbiter
---

# Severity Normalisation

**Category:** `council` · **Output artifact:** `normalised-severities.md`

## What this skill does
Make severity consistent across different critics.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-synthesis-arbiter`.

## Procedure
1. Collect the ratings from every critic.
2. Compare findings of similar consequence rated differently.
3. Re-anchor against the scale definitions and prior verdicts.
4. Adjust outliers and record the adjustment.
5. Report persistent disagreement rather than averaging it away.

## Output contract
Write `normalised-severities.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** severity-normalisation
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
- Outliers re-anchored to the scale
- Persistent disagreement reported, not averaged
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
