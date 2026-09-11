# Skills

505 skills. One directory each, containing a single `SKILL.md`.

A skill is a procedure, not a description. Agents own accountability; skills own method. The same
skill is used by different agents in different contexts and should produce comparable output either way.

## Anatomy of a skill

- **Frontmatter** — `name`, `category`, `description`, `output`, and the agents that use it.
- **Procedure** — five concrete steps. Not principles: steps you can follow and check.
- **Output contract** — the named artifact, written to `workspace/<venture-id>/<category>/` and
  registered as an artifact record so it becomes retrievable memory. Every output carries a summary,
  the body, an evidence table, open questions, and one next action.
- **Quality bar** — two skill-specific checks plus the standing rule that load-bearing claims are graded.
- **Anti-patterns** — the failure modes for the whole category, so related skills fail the same way
  and can be corrected the same way.

## Categories

| Category | Count |
|---|---|
| compliance | 12 |
| council | 44 |
| data | 7 |
| design | 78 |
| efficiency | 9 |
| engineering | 61 |
| finance | 56 |
| gtm | 38 |
| improvement | 55 |
| legal | 15 |
| market | 36 |
| memory | 13 |
| orchestration | 48 |
| people | 5 |
| product | 13 |
| risk | 4 |
| strategy | 11 |
| **total** | **505** |

Browse them in [`SKILL_INDEX.md`](SKILL_INDEX.md).

## Loading skills without paying for all of them

`index/` holds the tier-1 discovery shards: one small TSV per category, each line a skill name, its
output, and one sentence of purpose. Load the shard for the category you need (~400 tokens), pick the
skills, then load only those `SKILL.md` files. Never load the library to choose from it — that is
what the index is for. See `runtime/loader-spec.md`.

## Adding a skill

Create `skills/<name>/SKILL.md` with the same frontmatter and sections, add it to `registry.yaml`,
and reference it from at least one agent. Regenerate the category index shard. The tests check that
the file, the registry, the index shard, and the agents that claim to use it all agree.
