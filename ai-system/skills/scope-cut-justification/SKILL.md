---
name: scope-cut-justification
category: product
description: "Record why something was cut so the decision survives argument."
output: "scope-cuts.md"
used_by:
  - mvp-scoper
---

# Scope Cut Justification

**Category:** `product` · **Output artifact:** `scope-cuts.md`

## What this skill does
Record why something was cut so the decision survives argument.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `mvp-scoper`.

## Procedure
1. State what was cut and who asked for it.
2. State the criterion applied: does it change what we learn now?
3. Record the trigger that would bring it back.
4. Record the risk accepted by cutting it.
5. Publish so the cut does not have to be re-argued weekly.

## Output contract
Write `scope-cuts.md` into `workspace/<venture-id>/product/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** scope-cut-justification
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
- Revisit trigger recorded per cut
- Accepted risk stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `product` category
- Writing a requirement that starts with a solution instead of an evidenced problem.
- Shipping without defining, in advance, what would show it worked.
- Treating the roadmap as a promise rather than a current best sequence.
