---
name: minute-taking
category: compliance
description: "Record decisions so the corporate record is accurate."
output: "minutes.md"
used_by:
  - corporate-secretary-agent
---

# Minute Taking

`compliance` · produces `minutes.md` · used by `corporate-secretary-agent`

Record decisions so the corporate record is accurate.

## Procedure
1. Record attendance, quorum, and the time.
2. Record the decision made, not the discussion around it.
3. Record any conflict of interest declared and how it was handled.
4. Record dissent and abstention where they occurred.
5. Circulate promptly for approval while memories are accurate.

## Output contract
`minutes.md` → `workspace/<venture-id>/compliance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/compliance.tsv`.

## Quality bar
- Decisions recorded, not discussion narrative
- Conflicts and dissent recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.
