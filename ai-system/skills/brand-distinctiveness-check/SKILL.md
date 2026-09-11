---
name: brand-distinctiveness-check
category: design
description: "Verify the identity is actually distinguishable from the competition."
output: "distinctiveness-report.md"
used_by:
  - brand-identity-designer
---

# Brand Distinctiveness Check

**Category:** `design` · **Output artifact:** `distinctiveness-report.md`

## What this skill does
Verify the identity is actually distinguishable from the competition.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `brand-identity-designer`.

## Procedure
1. Collect the identities of the real competitive set.
2. Place ours among them and check whether it is identifiable without the name.
3. Check for convergence on the category's default colours and forms.
4. Verify no confusing similarity to an existing mark.
5. Adjust for distinctiveness without sacrificing legibility.

## Output contract
Write `distinctiveness-report.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** brand-distinctiveness-check
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
- Identifiable without the name alongside competitors
- Category-default convergence checked
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
