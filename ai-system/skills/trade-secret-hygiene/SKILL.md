---
name: trade-secret-hygiene
category: legal
description: "Protect what is not worth patenting."
output: "trade-secret-policy.md"
used_by:
  - ip-counsel-agent
---

# Trade Secret Hygiene

**Category:** `legal` · **Output artifact:** `trade-secret-policy.md`

## What this skill does
Protect what is not worth patenting.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ip-counsel-agent`.

## Procedure
1. Identify the information whose value depends on secrecy.
2. Restrict access to those who genuinely need it.
3. Ensure confidentiality obligations cover everyone with access.
4. Mark and handle the material consistently with its status.
5. Review when people leave or partnerships end.

## Output contract
Write `trade-secret-policy.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** trade-secret-hygiene
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
- Access restricted to genuine need
- Handling consistent with claimed status
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
