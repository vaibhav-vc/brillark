---
name: regulatory-applicability-mapping
category: legal
description: "Determine which rules actually apply to this business."
output: "applicability-map.md"
used_by:
  - chief-compliance-officer-agent
---

# Regulatory Applicability Mapping

**Category:** `legal` · **Output artifact:** `applicability-map.md`

## What this skill does
Determine which rules actually apply to this business.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-compliance-officer-agent`.

## Procedure
1. List activities, data types, markets, and customer types.
2. Identify candidate regimes for each and test applicability rather than assuming.
3. Record why each regime applies or does not.
4. Map applicable requirements to owners.
5. Re-run when entering a market or launching a new capability.

## Output contract
Write `applicability-map.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** regulatory-applicability-mapping
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
- Non-applicability recorded with a reason
- Re-run on market or product change
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
