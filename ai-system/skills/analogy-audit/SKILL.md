---
name: analogy-audit
category: council
description: "Find reasoning that rests on imitation rather than evidence."
output: "analogy-audit.md"
used_by:
  - council-first-principles
---

# Analogy Audit

**Category:** `council` · **Output artifact:** `analogy-audit.md`

## What this skill does
Find reasoning that rests on imitation rather than evidence.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-first-principles`.

## Procedure
1. Identify every justification of the form 'X does this'.
2. Check whether X's circumstances match ours in the relevant respects.
3. Check whether X actually succeeded because of that choice.
4. Replace the analogy with direct reasoning or evidence.
5. Report justifications that cannot be replaced.

## Output contract
Write `analogy-audit.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** analogy-audit
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
- Circumstance match tested per analogy
- Unreplaceable analogies reported
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
