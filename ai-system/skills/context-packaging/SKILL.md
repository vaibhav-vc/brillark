---
name: context-packaging
category: orchestration
description: "Assemble everything an agent needs so it never has to rediscover known facts."
output: "context-package.json"
used_by:
  - handoff-coordinator
  - intake-router
  - orchestration-head
---

# Context Packaging

**Category:** `orchestration` · **Output artifact:** `context-package.json`

## What this skill does
Assemble everything an agent needs so it never has to rediscover known facts.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `handoff-coordinator`, `intake-router`, `orchestration-head`.

## Procedure
1. Pull the task brief, its DoD, and its inputs.
2. Retrieve relevant semantic memory, decisions, and prior attempts.
3. Include the constraints in force and the assumptions already accepted.
4. List the open questions being carried forward.
5. Trim anything not needed — an oversized package is as bad as an empty one.

## Output contract
Write `context-package.json` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** context-packaging
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
- Prior attempts included
- Package trimmed to what is needed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
