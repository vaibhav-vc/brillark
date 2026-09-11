---
name: origin-story-development
category: gtm
description: "Capture why the founders started this, credibly."
output: "origin-story.md"
used_by:
  - brand-narrative-agent
---

# Origin Story Development

`gtm` · produces `origin-story.md` · used by `brand-narrative-agent`

Capture why the founders started this, credibly.

## Procedure
1. Establish the founder's direct experience of the problem.
2. Describe the specific moment the decision was made.
3. Explain the insight others missed and why the founder saw it.
4. Keep it true — investors and journalists verify these.
5. Compress to a version that survives being retold by others.

## Output contract
`origin-story.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Verifiably true in every detail
- Compressed to a retellable form
- The output states its confidence grade and names the evidence behind every load-bearing claim.
