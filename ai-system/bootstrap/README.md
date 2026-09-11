# Bootstrap

## `init.sh <venture-id>`

Scaffolds `workspace/<venture-id>/` with a directory per skill category, the six memory stores, a
verdict archive, an artifact register, and a `venture.yaml` from the template.

```bash
bash ai-system/bootstrap/init.sh acme-corp
```

It refuses to overwrite an existing venture and validates the id format. Nothing in `ai-system/` is
venture-specific — the system is the constant, the workspace is the variable.

## `venture.template.yaml`

The intent brief. Two sections matter more than the rest:

**`what_we_do_not_know`** — this becomes the hypothesis backlog. A brief with an empty list here is a
brief that has not been thought about, and the Council will say so.

**`kill_criteria`** — written now, while judgement is still uncommitted. A kill criterion written
after the evidence arrives is a rationalisation. Each needs a numeric threshold and a deadline.

## Verifying the system

```bash
python3 ai-system/tests/test_system_integrity.py
```

Run this after any change to agents, skills, workflows, or schemas. It catches the failures that are
otherwise silent: a renamed skill leaving eleven dangling references, a deleted agent leaving three
others reporting to a ghost, a copied workflow pointing at the original's agents.
