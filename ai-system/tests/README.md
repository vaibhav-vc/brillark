# Tests

```bash
python3 ai-system/tests/test_system_integrity.py       # 41 integrity tests
python3 ai-system/tests/measure_context_cost.py        # what a run actually costs
python3 -m pytest ai-system/tests -q                   # via pytest
```

Only the standard library and PyYAML are needed.

## What is checked

**Agents** — the registry matches the files on disk; ids are unique; the org shape is exactly
50 planning + 14 design + 12 improvement specialists, 10 council, 7 heads, 1 director; every `reports_to` resolves; there are no reporting
cycles; every agent reaches the Director; frontmatter matches the registry; every agent has all the
required sections and declares memory scopes; profiles satisfy `agent-profile.schema.json`.

**Skills** — the library is at least 100 skills; the registry matches the directories on disk; every
skill an agent references exists; every skill file has a procedure of at least five steps, a quality
bar, and an output contract; `used_by` matches what the agent definitions actually claim.

**Workflows** — every step names a real agent and real skills; every step has a completion condition
and produces something; every workflow has a real owner and exit criteria; stage-advancing workflows
route through the Council.

**Model tiering and budgets** — every agent declares a valid model tier, task class, and escalation
target; judgement work (the Director, the heads, the Council, and any judgement-class specialist)
stays on the strongest tier; every agent has context and return budgets, and no agent may return more
than it may receive; every charter carries a return contract.

**Progressive disclosure** — the domain index covers every domain with correct counts; every agent
appears in exactly one domain card file and it matches its registry domain; every skill is indexed
exactly once; worst-case tier-1 discovery fits inside its budget; the model routing table matches the
registry; variable content stays last in the cache order.

**Self-improvement safety** — evaluation criteria, guardrails, schemas, and org shape are nameable
artifact classes requiring human-founder authorisation; proposals require a diagnosis with an
attribution and at least three instances; variants may change only one dimension; agent returns are
capped and must report their token cost; the improvement workflow gates adoption behind measure,
diagnose, trial, sweep, and authorise, in that order.

**Schemas** — all parse; all are self-describing; none requires a property it does not define; memory
records require provenance; council findings require a failure scenario.

## Why these particular tests

These are the failures that happen silently. A skill gets renamed and eleven agents now reference
something that does not exist. An agent is deleted and three others report to a ghost. A workflow is
copied and its steps point at agents from the original. None of that produces an error at authoring
time — it produces an agent that cannot do its job, discovered much later.

If you change the shape of the organisation, `REQUIRED` at the top of the test file is where you say
so — and an org-shape change is not something the improvement domain may make on its own.

## The measurement

`measure_context_cost.py` is not a test; it reports. It compares loading the whole library against
the three-tier strategy and prints the ratio, and it exits non-zero if any agent's tier-1 plus tier-2
load exceeds its own context budget. Token counts are estimates at four characters per token — useful
for comparing strategies, which is what they are for, not for billing.
