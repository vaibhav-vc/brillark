---
name: claims-substantiation-review
category: legal
description: "Check that public claims can be backed up."
output: "substantiation-file.md"
used_by:
  - council-legal-and-regulatory-critic
  - general-counsel-agent
---

# Claims Substantiation Review

**Category:** `legal` · **Output artifact:** `substantiation-file.md`

## What this skill does
Check that public claims can be backed up.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-legal-and-regulatory-critic`, `general-counsel-agent`.

## Procedure
1. Collect every external claim, including implied and comparative ones.
2. Identify the evidence that supports each.
3. Assess whether the evidence supports the exact claim made.
4. Reject or soften claims that outrun the evidence.
5. Keep the substantiation file for as long as the claim is live.

## Output contract
Write `substantiation-file.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** claims-substantiation-review
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
- Implied and comparative claims included
- Substantiation retained while the claim is live
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
