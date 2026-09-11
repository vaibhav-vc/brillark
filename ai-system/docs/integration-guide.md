# Integration guide — running this on any model

The organisation is definitions plus an executable contract. Nothing in it is specific to a vendor,
a framework, or an agent SDK. This is how you wire it to whatever you have.

## The 60-second version

```bash
python3 ai-system/tools/loader.py domains                     # what exists
python3 ai-system/tools/loader.py agents --domain hardware    # who is in a domain
python3 ai-system/tools/loader.py assemble --agent pcb-layout-designer --task "Route the sensor board"
```

That last command prints the exact context a real run sends, its token cost, and the model the
active profile resolves to. If your runtime produces something different, the difference is the bug.

## 1. Point it at your models

Every agent declares a `task_class` — `mechanical`, `analytical`, or `judgement` — and never a model
name. `runtime/model-profiles.yaml` maps those onto concrete models. That file is the only place a
vendor name appears in the whole system.

```yaml
active_profile: custom
profiles:
  custom:
    mechanical: your-fast-model
    analytical: your-workhorse-model
    judgement: your-strongest-model
```

A null tier is a hard error, not a silent upgrade to a stronger model — silent upgrades hide
misconfiguration and inflate cost invisibly.

**Before trusting an assignment, measure it.** An unmeasured tier assignment is a guess with a
config file around it:

```bash
python3 ai-system/tools/eval.py --runner yourmodule:call --profile custom
```

### What your model must support

| Required | Why |
|---|---|
| Structured output validating against a supplied JSON Schema | Returns, memory records, and proposals are schema-enforced |
| ≥32k context | Routed activation is ~3.2k; the rest is task context |
| Instruction-following across a multi-thousand-token system prompt | The contract lives there |
| Willingness to return `guessed` rather than confabulate | This is the behaviour the whole evidence-grading system rests on |

Strongly recommended: prompt caching (or the cache-ordering discipline buys nothing) and tool
calling (for just-in-time retrieval). Not required: any specific vendor, tokeniser, or native
"agent"/"skill" feature — the organisation supplies its own.

## 2. Choose how to consume it

```bash
python3 ai-system/tools/export.py
```

| Format | File | Use when |
|---|---|---|
| `json` | `agents.json`, `skills.json` | You are building your own orchestrator |
| `tools` | `tool-definitions.json` | Your model has function calling — one tool per agent, plain JSON Schema |
| `claude` | `claude-agents/` | Drop into `.claude/agents/`; each file is self-contained |
| `mcp` | `mcp-manifest.json` | You expose agents through an MCP server |
| `prompts` | `system-prefix.txt` | You just want the cacheable prefix to send once |

`dist/` is generated, never edited, and not committed — regenerate it in one command. The markdown
in `ai-system/` is the source of truth.

## 3. Assemble context correctly

Order matters twice: for correctness, and for cache reuse.

```
prompts/system/00-base-agent.md        ┐
prompts/system/05-token-discipline.md  │
skills/OUTPUT_CONTRACT.md              ├─ stable across the session: cache this
prompts/system/<tier>.md               │
agents/<domain>/<id>.md                │
skills/<each declared skill>/SKILL.md  ┘
context package                        ┐ variable
the task                               ┘
```

One variable value inside the stable block loses cache reuse for all of it.
`test_conformance.py::TestLoadingOrder` checks this, including that the prefix is byte-identical
across two different tasks.

**Do not load the skill index on a routed run.** The charter already names its toolkit. The index
exists for composing a task that no single agent's toolkit covers.

## 4. Enforce the budgets

Every agent carries `context_budget_tokens` and `return_budget_tokens`. The loader raises rather
than truncating silently:

```
BUDGET EXCEEDED
progress-tracker: 51,203 tokens exceeds its 6,000 budget by 45,203.
Compact the context package, then escalate to orchestration-head if still over.
Repeated exceedance is a bloat defect for token-efficiency-analyst, not a reason to raise the limit.
```

Returns are capped too. An agent hands back the decision, artifact **paths**, a confidence grade,
and open questions — never its working context. Validate with:

```bash
python3 ai-system/tools/loader.py validate-return --file return.json
```

## 5. Port the loader, port the tests

`tools/loader.py` is a reference implementation, not a dependency. Rewrite it in your language if
you like — but port `tests/test_conformance.py` with it. Those 33 tests *are* the definition of
correct: model resolution, loading order, cache stability, budget enforcement, return validation,
and export fidelity.

## What this does not do

- **It does not execute.** There is no scheduler, no retry loop, no persistence layer. It tells you
  what to send and what to expect back; running it is your orchestrator's job.
- **It does not score itself.** `eval.py` assembles, runs, and records. Scoring is against
  `evals/rubric.yaml` by a human or a separate judge — a model scoring its own output measures
  agreement, not quality.
- **It does not guarantee output quality on a model it has never been measured on.** The tier
  assignments in the `anthropic` profile were measured. Yours have not been. Run the evals.

## Common mistakes

| Mistake | What happens |
|---|---|
| Loading all 130 charters to "give the model full context" | ~280k tokens, worse output, and the routing tiers exist precisely to avoid it |
| Putting a timestamp or session id in the system prompt | Cache reuse lost for the entire prefix |
| Raising a budget because an agent keeps exceeding it | Hides a context-packaging defect that will recur everywhere |
| Returning the full analysis as the summary | The parent's context fills with what artifacts are for |
| Demoting a judgement-class agent to save money | The failures are the irreversible ones; the test suite blocks this |
| Using a holdout eval case while tuning | It stops being a measurement, permanently |
