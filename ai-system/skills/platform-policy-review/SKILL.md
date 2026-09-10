---
name: platform-policy-review
category: legal
description: "Check the plan against the rules of the platforms it depends on."
output: "platform-policy-review.md"
used_by:
  - council-legal-and-regulatory-critic
---

# Platform Policy Review

**Category:** `legal` · **Output artifact:** `platform-policy-review.md`

## What this skill does
Check the plan against the rules of the platforms it depends on.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-legal-and-regulatory-critic`.

## Procedure
1. Identify every platform the business depends on for distribution or payment.
2. Review the policies that apply to our model, especially around payments and data.
3. Check for policy changes since the last review.
4. Assess the consequence of removal, which is usually immediate.
5. Reduce single-platform dependency where the risk is material.

## Output contract
Write `platform-policy-review.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** platform-policy-review
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
- Payment and data policies specifically checked
- Removal consequence assessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
