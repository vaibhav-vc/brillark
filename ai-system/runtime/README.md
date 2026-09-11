# Runtime

Machine-readable configuration a runtime is expected to enforce. These are not documentation — if a
loader ignores them, the organisation stops being affordable and the model tiering stops being safe.

| File | What it controls |
|---|---|
| `context-budget.yaml` | The three loading tiers, per-agent context and return budgets, retrieval caps, cache ordering, and what to do on exceedance |
| `model-routing.yaml` | Which model tier each agent runs on and the observable triggers that make it hand up |
| `loader-spec.md` | How to assemble an agent's context, in order |

## The one rule that matters most

Load in tier order and never skip forward. Loading Tier 2 for six candidate agents in order to
choose between them is exactly what Tier 1 exists to prevent, and it costs more than the naive
approach it was meant to replace.

## Checked by tests

`tests/test_system_integrity.py` verifies that the indexes match the registry, that worst-case
tier-1 discovery fits its budget, that the routing table matches every agent's declared tier, that
return budgets are always below context budgets, and that variable content stays last in the cache
order. `tests/measure_context_cost.py` reports what a run actually costs.
