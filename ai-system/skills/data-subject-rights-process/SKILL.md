---
name: data-subject-rights-process
category: compliance
description: "Build a rights request process that actually works."
output: "rights-process.md"
used_by:
  - data-protection-officer-agent
---

# Data Subject Rights Process

`compliance` · produces `rights-process.md` · used by `data-protection-officer-agent`

Build a rights request process that actually works.

## Procedure
1. Define the intake channel and how requests are identified.
2. Define identity verification proportionate to the request.
3. Map where personal data lives so a request can be fulfilled completely.
4. Set the internal deadline ahead of the statutory one.
5. Test the process end to end with a real request.

## Output contract
`rights-process.md` → `workspace/<venture-id>/compliance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/compliance.tsv`.

## Quality bar
- Complete data map enables full fulfilment
- Process tested end to end
- The output states its confidence grade and names the evidence behind every load-bearing claim.
