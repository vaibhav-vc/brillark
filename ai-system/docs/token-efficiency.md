# Token efficiency

The organisation grew from 83 agents to 113 and from 363 skills to 505, and the cost of a single
agent run **fell by about 39%**. That is not a paradox: cost is driven by what gets loaded, not by
what exists. This page is how that works, and how to keep it true.

Run the measurement yourself:

```bash
python3 ai-system/tests/measure_context_cost.py
```

## The measured position

| | Tokens |
|---|---|
| Everything — all charters and all skills | ~373,000 |
| Tier 1: domain index + one domain's agent cards + one skill category index | ~1,100 |
| Tier 2: the selected charter + that agent's declared skills | ~3,600 |
| **Median single-agent run (tier 1 + tier 2)** | **~4,700** |
| Worst case single-agent run | ~5,600 |

**The "80x cheaper" framing was a strawman and has been retired.** Loading all 629 skills is not
something any sane runtime would do, so beating it proves nothing.

The honest comparison is against a single well-written general-purpose system prompt of ~5,000
tokens. Against that, a routed run costs **about the same — roughly 1.6x cheaper, not 80x**.

What tiering actually buys is not raw savings. It is that **138 specialised agents, each with its
own charter, skills and guardrails, stay affordable at roughly the cost of one generalist prompt**.
That is capability per token, and it is a much smaller and much more defensible claim.

Counts are estimates at four characters per token — good for comparing revisions of this repository
against each other, which is what the regression gate needs, and not a substitute for a tokeniser
or a bill.

## The seven mechanisms

### 1. Three-tier progressive disclosure
The single biggest lever, and the one the rest depend on.

- **Tier 1 — discovery.** `agents/index/_domains.tsv` (8 lines) picks the domain. That domain's
  card file (~440 tokens) picks the agent. One `skills/index/<category>.tsv` shard picks the skills.
- **Tier 2 — activation.** Load the one charter and the selected `SKILL.md` files. Nothing else.
- **Tier 3 — execution.** Context package, memory, and artifacts fetched just-in-time.

The two-level agent index matters more than it looks. A flat card file for 113 agents costs ~3,800
tokens at Tier 1; splitting it by domain costs ~720. That single change is why the org could grow
36% while per-run cost fell.

### 2. Sub-agent context isolation
Every agent runs in its own context and returns at most `return_budget_tokens` — the decision, the
artifact paths, a confidence grade, open questions. Never its working context. A specialist may burn
15,000 tokens internally and hand back 800. The parent reads the artifact if it needs detail.

Schema: `knowledge-schema/agent-return.schema.json`.

### 3. Model tiering
Work is classified mechanical, analytical, or judgement, and routed accordingly.

| Tier | Agents | Used for |
|---|---|---|
| `haiku` | 3 | Extraction, formatting, validation, tracking |
| `sonnet` | 65 | Synthesis, comparison, modelling, diagnosis, building |
| `opus` | 45 | Arbitration, strategy, ethics, irreversible decisions, the whole Council |

Every assignment needs quality evidence on the golden cases, and every demotion needs an escalation
rule with an **observable** trigger. Judgement work is never demoted to save money. Owned by
`model-router-tuner`; the table lives in `runtime/model-routing.yaml`.

### 4. Cache-stable prompt ordering
Base prompt → tier prompt → charter → skills → context package → task. Everything before the
context package is stable for the session. Interleaving one variable value into that prefix loses
cache reuse for all of it, which is a large and completely avoidable cost.

### 5. Just-in-time retrieval, digest-first
Carry pointers, not payloads. Read the memory digest; fetch the full record only when the digest is
insufficient. Retrieval is capped at 12 records by default.

### 6. Output discipline
Lead with the answer. No preamble, no restating the question, no closing paragraph that repeats the
opening. Artifacts carry a capped summary and the detail lives in the body, so a reader — human or
agent — can stop early. See `prompts/system/05-token-discipline.md`.

### 7. Measurement, so none of this is a story
`knowledge-schema/token-ledger.schema.json` records what every run actually cost, including the
runs that failed. `token-efficiency-analyst` computes cost **per completed task** — a cheap call
that fails twice is expensive — and finds context that was loaded and never referenced, then fixes
the packaging rule rather than trimming by hand.

## The rule that keeps it honest

**No efficiency change ships without a quality check on the golden cases.** A saving that pushes an
agent below its rubric floor is not a saving; it moves the cost from tokens to rework and hides it.
`efficiency-quality-tradeoff` is the gate, and it accounts for retry cost.

## Budgets

`runtime/context-budget.yaml` is machine-readable and a runtime is expected to enforce it.

| Agent tier | Context | Return |
|---|---|---|
| Director, head | 25,000 | 1,500 |
| Executive, council | 20,000 | 1,200 |
| Specialist | 15,000 | 800 |
| Mechanical | 6,000 | 400 |

On exceedance: compact, then escalate to the head. Repeated exceedance is a bloat defect routed to
`token-efficiency-analyst` — not an agent failing, a packaging rule failing.

## Sources

The design follows published practice on context engineering rather than invention:

- [Effective context engineering for AI agents — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Progressive Disclosure in AI Agents — MindStudio](https://www.mindstudio.ai/blog/progressive-disclosure-ai-agents-context-management)
- [Less Context, Better Agents: Efficient Context Engineering for Long-Horizon Tool-Using LLM Agents](https://arxiv.org/pdf/2606.10209)
- [Context Engineering: Why More Tokens Makes Agents Worse — Morph](https://www.morphllm.com/context-engineering)
