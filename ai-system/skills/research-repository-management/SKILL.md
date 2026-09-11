---
name: research-repository-management
category: design
description: "Keep past research findable so the next project does not re-run it."
output: "repository-entry.md"
used_by:
  - design-researcher
---

# Research Repository Management

`design` · produces `repository-entry.md` · used by `design-researcher`

Keep past research findable so the next project does not re-run it.

## Procedure
1. Tag every finding by topic, segment, product area, and date.
2. Store the evidence alongside the conclusion, not just the conclusion.
3. Record the study's method and limits so reuse is judged fairly.
4. Check the repository before commissioning new research.
5. Expire findings whose conditions have changed rather than leaving them to mislead.

## Output contract
`repository-entry.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Evidence stored with each conclusion
- Repository checked before new research is commissioned
- The output states its confidence grade and names the evidence behind every load-bearing claim.
