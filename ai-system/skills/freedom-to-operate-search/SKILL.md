---
name: freedom-to-operate-search
category: legal
description: "Check whether building this could infringe someone else's rights."
output: "fto-memo.md"
used_by:
  - ip-counsel-agent
---

# Freedom To Operate Search

**Category:** `legal` · **Output artifact:** `fto-memo.md`

## What this skill does
Check whether building this could infringe someone else's rights.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ip-counsel-agent`.

## Procedure
1. Define the technical features to be cleared.
2. Search patents and applications in the relevant jurisdictions.
3. Assess claim scope, not just titles and abstracts.
4. Identify design-arounds where risk is found.
5. Escalate to qualified counsel for any credible risk.

## Output contract
Write `fto-memo.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** freedom-to-operate-search
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
- Claim scope assessed, not titles
- Design-arounds identified where risk exists
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
