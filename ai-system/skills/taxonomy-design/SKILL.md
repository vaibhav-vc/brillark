---
name: taxonomy-design
category: design
description: "Build the controlled vocabulary the whole organisation uses."
output: "taxonomy.md"
used_by:
  - information-architect
---

# Taxonomy Design

**Category:** `design` · **Output artifact:** `taxonomy.md`

## What this skill does
Build the controlled vocabulary the whole organisation uses.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `information-architect`.

## Procedure
1. Derive terms from user language in research, not from internal shorthand.
2. Define one term per concept and record the rejected synonyms.
3. Check each term for ambiguity across the product's contexts.
4. Define the rules for adding a term and who approves it.
5. Publish it where product, design, content, and engineering will all see it.

## Output contract
Write `taxonomy.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** taxonomy-design
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
- One term per concept with rejected synonyms recorded
- Terms drawn from user language
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
