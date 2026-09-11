# Token discipline — every agent

You do not get the whole organisation in your context, and you should not want it. Loading more is
not the same as knowing more: past a point it reliably makes output worse, not better.

## Loading

1. **Three tiers, in order.** Tier 1 is discovery — `agents/index/_domains.tsv`, one domain's card
   file, one skill category index. Tier 2 is activation — the one charter and the skills you
   actually selected. Tier 3 is execution — context, retrieved memory, input artifacts, fetched
   just-in-time. Never skip forward: loading Tier 2 for six candidate agents to decide between them
   is what Tier 1 exists to prevent.
2. **Pointers, not payloads.** Carry file paths, artifact ids, and query templates. Fetch the
   content when you need it, and only the part you need.
3. **Retrieve digests first.** Read the memory digest; fetch the full record only when the digest is
   insufficient. Cap retrieval at the limit in `runtime/context-budget.yaml`.
4. **Never reorder the stable prefix.** Base prompt, tier prompt, charter, skills — in that order,
   every time. Variable content goes after it. Interleaving anything variable into that prefix
   destroys cache reuse for everything that follows.

## Returning

You run in your own context. What you hand back to your parent is capped by your
`return_budget_tokens`: the decision or finding, the artifact paths, your confidence grade, and any
open question. **Never return your working context.** If the parent needs the detail, it reads the
artifact — that is what artifacts are for.

If you cannot fit the answer in the budget, the answer is too long, not the budget too small.
Summarise and point.

## Writing

- Lead with the answer. The reasoning goes after it, and often in the artifact rather than the reply.
- Say the number, name the source, stop. Do not restate the question or narrate what you are about to do.
- No preamble, no summary of your own summary, no closing paragraph that repeats the opening.
- A table beats a paragraph when the content is a table.
- Say "I don't know" in four words rather than three hedged sentences.

## Spending

- Cost is measured per **completed task**, not per call. A cheap call that fails twice is expensive,
  so do not under-resource work that will simply come back.
- If your context budget is exhausted, compact and continue; if still over, escalate to your head.
  Do not silently drop context and carry on.
- Repeated budget exceedance is a defect: route it to `token-efficiency-analyst` as context bloat,
  not as your personal failing.
