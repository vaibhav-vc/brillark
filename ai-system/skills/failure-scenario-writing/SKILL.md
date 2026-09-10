---
name: failure-scenario-writing
category: council
description: "Turn an objection into a specific, checkable failure."
output: "failure-scenario.md"
used_by:
  - council-red-team
---

# Failure Scenario Writing

**Category:** `council` · **Output artifact:** `failure-scenario.md`

## What this skill does
Turn an objection into a specific, checkable failure.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-red-team`.

## Procedure
1. State the precondition under which the failure occurs.
2. Describe the sequence of events step by step.
3. State the observable consequence and who suffers it.
4. Estimate likelihood in our actual context.
5. Drop the objection if the sequence cannot be written concretely.

## Output contract
Write `failure-scenario.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** failure-scenario-writing
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
- Concrete sequence, not an adjective
- Objections without a sequence dropped
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
