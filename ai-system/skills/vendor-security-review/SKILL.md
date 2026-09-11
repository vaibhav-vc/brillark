---
name: vendor-security-review
category: engineering
description: "Assess a third party before trusting them with data or access."
output: "vendor-security-review.md"
used_by:
  - ciso-agent
---

# Vendor Security Review

`engineering` · produces `vendor-security-review.md` · used by `ciso-agent`

Assess a third party before trusting them with data or access.

## Procedure
1. Determine what data and access the vendor would receive.
2. Review their security posture, certifications, and breach history.
3. Check contractual security and breach notification terms.
4. Assess the blast radius of their compromise.
5. Define monitoring and the exit path if their posture degrades.

## Output contract
`vendor-security-review.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Blast radius of compromise assessed
- Breach notification terms verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
