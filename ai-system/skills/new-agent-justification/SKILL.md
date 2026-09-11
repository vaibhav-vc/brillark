---
name: new-agent-justification
category: improvement
description: "Justify a new agent by the accountability nobody currently holds."
output: "agent-proposal.md"
used_by:
  - capability-gap-scout
---

# New Agent Justification

**Category:** `improvement` · **Output artifact:** `agent-proposal.md`

## What this skill does
Justify a new agent by the accountability nobody currently holds.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `capability-gap-scout`.

## Procedure
1. Name the outcome the new agent would own that no agent owns today.
2. Show why it cannot sit with an existing agent without overloading it.
3. Define its charter, escalation, and definition of done.
4. State the coordination cost it adds.
5. Submit for director approval; the org shape is not self-modifiable.

## Output contract
Write `agent-proposal.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** new-agent-justification
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
- Unowned outcome named explicitly
- Coordination cost stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
