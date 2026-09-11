# brillark

## `ai-system/`

A multi-agent organisation for planning, building, and upgrading ventures: 130 agents across nine
domains, 590 skills, 18 workflows, 21 schemas, and a test suite that keeps them consistent.

Built to be cheap to run — a routed agent run loads about **3,155 tokens**, not the 278,000 the full
library would cost. About 88x cheaper, verified by a benchmark that runs in CI.

Start at **[`ai-system/README.md`](ai-system/README.md)**.

```bash
python3 ai-system/tests/test_system_integrity.py   # 46 tests: does everything still line up?
python3 ai-system/tests/benchmark.py               # regression gate against a committed baseline
python3 ai-system/tests/measure_context_cost.py    # what does a run actually cost?
bash ai-system/bootstrap/init.sh <venture-id>      # scaffold a venture workspace
```

| Tier | Count | |
|---|---|---|
| Director | 1 | Stage gates, arbitration, budget |
| Domain heads | 8 | Finance, business, engineering, design, hardware, orchestration, improvement, council |
| Executive officers | 20 | Including Chief Design, Chief Hardware, Chief Learning Officer, legal, privacy, IP, risk |
| Council | 10 | Critics who attack every material plan before it is funded |
| Specialists | 91 | 50 planning · 15 hardware (3D + PCB) · 14 design · 12 improvement |

Key reading: [org chart](ai-system/docs/org-chart.md) ·
[token efficiency](ai-system/docs/token-efficiency.md) ·
[self-improvement](ai-system/docs/self-improvement.md) ·
[design practice](ai-system/docs/design-practice.md) ·
[hardware practice](ai-system/docs/hardware-practice.md) ·
[memory model](ai-system/docs/memory-model.md)
