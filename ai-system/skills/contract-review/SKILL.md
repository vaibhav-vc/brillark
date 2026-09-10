---
name: contract-review
category: legal
description: "Read an agreement for what it actually commits us to."
output: "contract-review.md"
used_by:
  - general-counsel-agent
---

# Contract Review

**Category:** `legal` · **Output artifact:** `contract-review.md`

## What this skill does
Read an agreement for what it actually commits us to.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `general-counsel-agent`.

## Procedure
1. Identify the obligations we take on and whether we can meet them.
2. Check liability, indemnity, and their caps.
3. Check termination rights, notice periods, and what survives.
4. Check IP ownership and data rights.
5. Flag every clause requiring a licensed attorney's opinion.

## Output contract
Write `contract-review.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** contract-review
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
- Liability position assessed against our capacity
- Attorney-grade clauses flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
