---
name: jurisdiction-risk-review
category: legal
description: "Treat each new market as a new risk surface."
output: "jurisdiction-review.md"
used_by:
  - council-legal-and-regulatory-critic
---

# Jurisdiction Risk Review

**Category:** `legal` · **Output artifact:** `jurisdiction-review.md`

## What this skill does
Treat each new market as a new risk surface.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-legal-and-regulatory-critic`.

## Procedure
1. Identify what changes legally when entering this jurisdiction.
2. Check data localisation, consumer protection, and tax obligations.
3. Check whether the product or content is restricted there.
4. Assess enforcement reality, not just the written rule.
5. Decide entry, deferral, or geo-blocking explicitly.

## Output contract
Write `jurisdiction-review.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** jurisdiction-risk-review
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
- Enforcement reality assessed
- Explicit entry decision recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
