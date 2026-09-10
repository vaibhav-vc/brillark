---
name: handoff-contract-definition
category: orchestration
description: "Define what must accompany work passed between two specific roles."
output: "handoff-contract.md"
used_by:
  - handoff-coordinator
---

# Handoff Contract Definition

**Category:** `orchestration` · **Output artifact:** `handoff-contract.md`

## What this skill does
Define what must accompany work passed between two specific roles.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `handoff-coordinator`.

## Procedure
1. Ask the receiving role what inputs it actually needs to start.
2. Specify the artifact, its format, and its completeness conditions.
3. Require stated assumptions and open questions as part of the handoff.
4. Define what the receiver may reject for, and how.
5. Version the contract; roles evolve and stale contracts cause silent gaps.

## Output contract
Write `handoff-contract.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** handoff-contract-definition
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
- Receiver defined the requirements
- Rejection grounds specified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
