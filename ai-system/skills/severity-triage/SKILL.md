---
name: severity-triage
category: council
description: "Assign a severity that means the same thing to everyone."
output: "severity-ratings.md"
used_by:
  - council-director
  - council-red-team
  - escalation-manager
---

# Severity Triage

**Category:** `council` · **Output artifact:** `severity-ratings.md`

## What this skill does
Assign a severity that means the same thing to everyone.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-director`, `council-red-team`, `escalation-manager`.

## Procedure
1. Apply the fixed scale: blocker, major, minor, note.
2. Require a concrete failure scenario for anything rated blocker or major.
3. Rate on consequence, not on how strongly it was argued.
4. Check the rating against how similar findings were rated before.
5. Drop findings that cannot be made concrete.

## Output contract
Write `severity-ratings.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** severity-triage
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
- Blockers carry a concrete failure scenario
- Consistency with prior ratings checked
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
