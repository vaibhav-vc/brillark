---
name: structured-logging
category: engineering
description: "Log so that questions can be answered later."
output: "logging-standard.md"
used_by:
  - backend-implementation-agent
---

# Structured Logging

`engineering` · produces `logging-standard.md` · used by `backend-implementation-agent`

Log so that questions can be answered later.

## Procedure
1. Log events as structured records with consistent field names.
2. Include the correlation identifier on every record.
3. Log the decision and its inputs, not only the outcome.
4. Never log secrets or personal data; define what is redacted.
5. Set levels deliberately so production noise stays readable.

## Output contract
`logging-standard.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Correlation identifier on every record
- Redaction rules defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.
