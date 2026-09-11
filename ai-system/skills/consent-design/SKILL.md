---
name: consent-design
category: compliance
description: "Design consent that is genuine rather than assumed."
output: "consent-design.md"
used_by:
  - data-protection-officer-agent
---

# Consent Design

`compliance` · produces `consent-design.md` · used by `data-protection-officer-agent`

Design consent that is genuine rather than assumed.

## Procedure
1. Make consent specific to each purpose, not bundled.
2. Ensure it is freely given — service must not be conditional on unnecessary consent.
3. Make withdrawal as easy as giving it.
4. Record what was consented to, when, and in what wording.
5. Re-obtain consent when the purpose changes.

## Output contract
`consent-design.md` → `workspace/<venture-id>/compliance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/compliance.tsv`.

## Quality bar
- Consent unbundled per purpose
- Withdrawal as easy as granting
- The output states its confidence grade and names the evidence behind every load-bearing claim.
