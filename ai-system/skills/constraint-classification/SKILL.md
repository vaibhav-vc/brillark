---
name: constraint-classification
category: council
description: "Sort real constraints from assumed ones."
output: "constraint-analysis.md"
used_by:
  - council-first-principles
---

# Constraint Classification

**Category:** `council` · **Output artifact:** `constraint-analysis.md`

## What this skill does
Sort real constraints from assumed ones.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-first-principles`.

## Procedure
1. List every constraint the plan treats as fixed.
2. Classify each: physical, legal, contractual, economic, or habitual.
3. For each non-physical constraint, identify who could change it.
4. Test whether anyone has actually tried.
5. Report constraints that are choices nobody owns as findings.

## Output contract
Write `constraint-analysis.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** constraint-classification
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
- Owner identified per changeable constraint
- Unowned assumed constraints flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
