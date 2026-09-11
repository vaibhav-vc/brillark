# ai-system — a multi-agent organisation for building ventures

113 agents, 505 skills, 17 workflows, 19 schemas, and a test suite that keeps them consistent.

The system takes a founder's intent and runs it through the path a competent company would: design a
business model, validate it against real customers, design the experience, scope an MVP to the
smallest thing that tests the riskiest belief, build it, launch it, learn from it, upgrade it — with
every material plan attacked by a standing Council before money is spent on it, and a self-improvement
loop that makes the next cycle better than the last.

**It is built to be cheap to run.** A single agent run loads about **4,700 tokens**, not the 373,000
the full library would cost, because nothing loads what it does not need. See
[`docs/token-efficiency.md`](docs/token-efficiency.md) — and run the measurement yourself.

## The organisation

```
                              human founder
                                    |
                                director                    <- 1, single accountable owner
                                    |
    +---------+---------+-----------+-----------+---------+---------+
    |         |         |           |           |         |         |
 finance  business  engineering  design   orchestration improvement council
   (13)     (15)       (15)       (15)        (11)         (13)      (11)

    executive officers (19): CEO CFO CMO CTO COO CPO CSO CRO CDO CISO CHRO
    Chief Design Officer, Chief Learning Officer, General Counsel,
    Chief Compliance, Chief Risk, DPO, IP Counsel, Corporate Secretary
```

Full chart and decision rights: **[`docs/org-chart.md`](docs/org-chart.md)**.

| Tier | Count | For |
|---|---|---|
| Director | 1 | Stage gates, arbitration, budget. The only agent reporting to the human. |
| Domain heads | 7 | Finance, business, engineering, design, orchestration, improvement, council. |
| Executive officers | 19 | Company-wide functions, including design, learning, legal, privacy, IP, risk. |
| Council | 10 | Structured critics. Attack every material plan before it is funded. |
| Specialists | 76 | 50 planning · 14 design · 12 improvement. |

## What makes it work

**Progressive disclosure.** Three tiers: discovery (a domain index, then one domain's agent cards,
then one skill category index — about 1,100 tokens), activation (the one charter and the skills
actually chosen), execution (context fetched just-in-time). The org grew 36% from v1 and the cost of
a run *fell* 39%.

**Context isolation.** Every agent runs in its own context and returns at most its
`return_budget_tokens` — the decision, the artifact paths, a confidence grade. Never its working
context.

**Model tiering.** 3 agents on `haiku` for mechanical work, 65 on
`sonnet` for analysis, 45 on `opus` for judgement. Every assignment needs quality
evidence; judgement work is never demoted to save money.

**Structural rules.** A memory record cannot exist without provenance. A decision cannot omit its
accepted costs. A Council finding cannot be an adjective. A design spec cannot omit its error state.
These are enforced by schema, not by convention.

**It improves itself, within limits.** The improvement domain measures, diagnoses, trials against
held-out cases, sweeps for regressions, adopts one change at a time, and verifies the next cycle. It
may edit prompts and skill steps automatically. It may **never** change guardrails, schemas, the org
shape, or its own evaluation criteria — those need the human founder. See
[`docs/self-improvement.md`](docs/self-improvement.md).

## Layout

| Directory | Contents |
|---|---|
| `agents/` | 113 charters, `registry.yaml`, and the tier-1 `index/` used for routing |
| `skills/` | 505 skills, one directory each, plus the sharded tier-1 `index/` |
| `runtime/` | Context budgets, model routing, and the loader specification |
| `prompts/` | Layered system prompts and the artifact templates that move between agents |
| `workflows/` | 17 workflow definitions, from intake to self-improvement |
| `knowledge-schema/` | 20 JSON Schemas: memory, decisions, verdicts, returns, proposals, design specs |
| `integrations/` | Contracts for the external systems the organisation reads and writes |
| `tests/` | Integrity tests, plus the context-cost measurement |
| `bootstrap/` | Scaffold a venture and verify the wiring |
| `docs/` | Org chart, memory model, token efficiency, self-improvement, design practice |

## Start here

```bash
python3 ai-system/tests/test_system_integrity.py    # 41 tests: does everything still line up?
python3 ai-system/tests/measure_context_cost.py     # what does a run actually cost?
bash ai-system/bootstrap/init.sh acme-corp          # scaffold a venture workspace
```

1. **[`docs/getting-started.md`](docs/getting-started.md)** — run your first venture through it.
2. **[`docs/org-chart.md`](docs/org-chart.md)** — who reports to whom, who decides what.
3. **[`docs/token-efficiency.md`](docs/token-efficiency.md)** — why it is cheap, and how to keep it cheap.
4. **[`docs/memory-model.md`](docs/memory-model.md)** — how context and memory actually work.
5. **[`docs/self-improvement.md`](docs/self-improvement.md)** — the loop, and its boundary.

## Deliberate constraints

- **One owner** per task, artifact, risk, and metric. Two owners means none.
- **Evidence carries a grade** — `measured`, `sourced`, `benchmarked`, `estimated`, `guessed`. A
  guess may never be load-bearing at a stage gate.
- **The Council attacks but never decides.** The Director decides, and overruling a blocker must be
  written down.
- **Accessibility is a build requirement.** A surface that fails its conformance target is a defect.
- **Legal advice stops at the boundary.** Anything needing a licensed attorney is escalated out of
  the system, never answered inside it.
- **Efficiency never buys quality.** No saving ships without a quality check on the golden cases.
