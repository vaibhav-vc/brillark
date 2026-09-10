---
name: counsel-escalation
category: legal
description: "Mark clearly what needs a licensed professional."
output: "counsel-request.md"
used_by:
  - council-legal-and-regulatory-critic
---

# Counsel Escalation

**Category:** `legal` · **Output artifact:** `counsel-request.md`

## What this skill does
Mark clearly what needs a licensed professional.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-legal-and-regulatory-critic`.

## Procedure
1. Identify the question that exceeds issue-spotting.
2. State what has already been established and what remains open.
3. Frame the specific question for counsel, not the whole situation.
4. Note the deadline and the decision waiting on it.
5. Never paper over the gap with a confident-sounding internal answer.

## Output contract
Write `counsel-request.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** counsel-escalation
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
- Specific question framed for counsel
- Internal answer never substituted for advice
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
