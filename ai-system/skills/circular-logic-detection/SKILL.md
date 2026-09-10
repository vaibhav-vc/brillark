---
name: circular-logic-detection
category: council
description: "Find reasoning that assumes what it is trying to prove."
output: "circularity-report.md"
used_by:
  - council-economics-skeptic
---

# Circular Logic Detection

**Category:** `council` · **Output artifact:** `circularity-report.md`

## What this skill does
Find reasoning that assumes what it is trying to prove.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-economics-skeptic`.

## Procedure
1. Trace each key output back through its inputs to their origins.
2. Look for inputs that depend on the output — revenue funding the spend that creates the revenue.
3. Check whether growth assumptions are justified by the growth plan itself.
4. Identify metrics defined in terms of each other.
5. Report the loop explicitly and propose an independent anchor.

## Output contract
Write `circularity-report.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** circular-logic-detection
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
- Loops traced to their origin
- Independent anchor proposed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
