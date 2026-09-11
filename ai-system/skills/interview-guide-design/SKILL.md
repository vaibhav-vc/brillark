---
name: interview-guide-design
category: market
description: "Write questions that produce evidence instead of politeness."
output: "interview-guide.md"
used_by:
  - customer-discovery-interviewer
---

# Interview Guide Design

`market` · produces `interview-guide.md` · used by `customer-discovery-interviewer`

Write questions that produce evidence instead of politeness.

## Procedure
1. Start from the hypotheses being tested, riskiest first.
2. Convert each into a behavioural question about a specific past instance.
3. Remove every leading question and every yes/no question.
4. Order from broad context to specific probe.
5. Include the questions that could disconfirm your hypothesis.

## Output contract
`interview-guide.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- No leading questions remain
- Disconfirming questions included
- The output states its confidence grade and names the evidence behind every load-bearing claim.
