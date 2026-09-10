---
name: regulatory-exposure-review
category: legal
description: "Challenge a plan on what regulators would permit."
output: "regulatory-exposure.md"
used_by:
  - council-legal-and-regulatory-critic
---

# Regulatory Exposure Review

**Category:** `legal` · **Output artifact:** `regulatory-exposure.md`

## What this skill does
Challenge a plan on what regulators would permit.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-legal-and-regulatory-critic`.

## Procedure
1. Identify every regulated activity the plan touches, including hidden ones in payments and data.
2. Assess whether a licence or registration is required.
3. Check restrictions on marketing, claims, and target audiences.
4. Assess the consequence of getting it wrong, not just the likelihood.
5. Escalate anything requiring a licensed opinion.

## Output contract
Write `regulatory-exposure.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** regulatory-exposure-review
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
- Hidden regulated activities surfaced
- Consequence assessed, not just likelihood
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
