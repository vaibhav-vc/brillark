# brillark

## `ai-system/`

A multi-agent organisation for planning, building, and upgrading ventures: 113 agents across eight
domains, 505 skills, 17 workflows, 19 schemas, and a test suite that keeps them consistent.

Built to be cheap to run — a single agent run loads about **4,700 tokens**, not the 373,000 the full
library would cost, because nothing loads what it does not need.

Start at **[`ai-system/README.md`](ai-system/README.md)**.

```bash
python3 ai-system/tests/test_system_integrity.py   # 41 tests: does everything still line up?
python3 ai-system/tests/measure_context_cost.py    # what does a run actually cost?
bash ai-system/bootstrap/init.sh <venture-id>      # scaffold a venture workspace
```

| Tier | Count | |
|---|---|---|
| Director | 1 | Stage gates, arbitration, budget |
| Domain heads | 7 | Finance, business, engineering, design, orchestration, improvement, council |
| Executive officers | 19 | Including Chief Design Officer, Chief Learning Officer, legal, privacy, IP, risk |
| Council | 10 | Critics who attack every material plan before it is funded |
| Specialists | 76 | 50 planning · 14 design · 12 improvement |

Key reading: [org chart](ai-system/docs/org-chart.md) ·
[token efficiency](ai-system/docs/token-efficiency.md) ·
[self-improvement](ai-system/docs/self-improvement.md) ·
[design practice](ai-system/docs/design-practice.md) ·
[memory model](ai-system/docs/memory-model.md)
