---
name: invention-disclosure
category: legal
description: "Capture inventions while the detail still exists."
output: "invention-disclosure.md"
used_by:
  - ip-counsel-agent
---

# Invention Disclosure

`legal` · produces `invention-disclosure.md` · used by `ip-counsel-agent`

Capture inventions while the detail still exists.

## Procedure
1. Record what the invention does and the problem it solves.
2. Record what makes it non-obvious compared to existing approaches.
3. Record the date of conception and first reduction to practice.
4. Record the contributors accurately; inventorship is a legal question.
5. Route to counsel for filing or trade-secret decision.

## Output contract
`invention-disclosure.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Non-obviousness articulated
- Contributors recorded accurately
- The output states its confidence grade and names the evidence behind every load-bearing claim.
