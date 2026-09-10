---
name: escalation-criteria
category: orchestration
description: "Define what must go up, to whom, and how fast."
output: "escalation-policy.md"
used_by:
  - escalation-manager
---

# Escalation Criteria

**Category:** `orchestration` · **Output artifact:** `escalation-policy.md`

## What this skill does
Define what must go up, to whom, and how fast.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `escalation-manager`.

## Procedure
1. Define severity levels by consequence, not by emotion.
2. Map each severity to a decision-maker and a response deadline.
3. Specify what must accompany an escalation at each level.
4. Define what explicitly does not escalate, to protect the signal.
5. Review the criteria when escalation volume rises or falls sharply.

## Output contract
Write `escalation-policy.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** escalation-criteria
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
- Severity defined by consequence
- Non-escalating cases defined too
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
