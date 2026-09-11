---
name: contract-review
category: legal
description: "Read an agreement for what it actually commits us to."
output: "contract-review.md"
used_by:
  - general-counsel-agent
---

# Contract Review

`legal` · produces `contract-review.md` · used by `general-counsel-agent`

Read an agreement for what it actually commits us to.

## Procedure
1. Identify the obligations we take on and whether we can meet them.
2. Check liability, indemnity, and their caps.
3. Check termination rights, notice periods, and what survives.
4. Check IP ownership and data rights.
5. Flag every clause requiring a licensed attorney's opinion.

## Output contract
`contract-review.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Liability position assessed against our capacity
- Attorney-grade clauses flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.
