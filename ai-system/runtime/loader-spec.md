# Loader specification

How to assemble an agent's context. Order matters twice: for correctness, and for cache reuse.

## Assembly order

```
1. prompts/system/00-base-agent.md          stable   ┐
2. prompts/system/05-token-discipline.md    stable   │
3. prompts/system/<tier>.md                 stable   ├─ cacheable prefix
4. agents/<domain>/<id>.md                  stable   │
5. skills/<selected>/SKILL.md               stable   ┘
6. context package                          variable ┐
7. the task                                 variable ┘
```

Everything through step 5 is stable for the session. **Never interleave a variable value into it** —
a single timestamp in step 1 loses cache reuse for all five.

## Selection, in tier order

**Tier 1 — discovery (~1,100 tokens).** Load `agents/index/_domains.tsv`. Pick the domain. Load that
domain's `agents/index/<domain>.tsv`. Pick exactly one agent. Load the relevant
`skills/index/<category>.tsv`. Pick the skills.

**Tier 2 — activation (~3,600 tokens).** Load the selected charter and the selected `SKILL.md` files.
Nothing else. An agent's `skills:` frontmatter is its declared toolkit; a skill outside it is a
signal to re-route, not to load more.

**Tier 3 — execution.** Build the context package (`knowledge-schema/context-package.schema.json`).
Retrieve memory digests first, capped at the retrieval limit. Fetch artifacts by path, only the parts
needed.

## Enforcement

- Refuse to exceed `context_budget_tokens`. Compact first; escalate to the head if still over.
- Truncate returns to `return_budget_tokens` — keep the decision and the artifact pointers, drop the
  narrative.
- Record a `token-ledger` entry for every run, including failed ones. Cost is per *completed task*.
- Record `context_referenced` so `context-bloat-analysis` can find what was loaded and never used.

## Model selection

Read `runtime/model-routing.yaml`. Escalate a tier when the task is irreversible, the Council raised
a blocker, two attempts failed the definition of done, or the agent's own confidence on a
load-bearing claim would be `guessed`.

Never demote judgement work — arbitration, strategy, ethics, one-way doors — to save money. The test
suite enforces this.
