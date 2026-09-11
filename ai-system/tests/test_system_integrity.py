"""Integrity tests for the ai-system agent organisation.

These check the things that silently rot: an agent referencing a skill that was renamed,
a reporting line pointing at a deleted agent, a workflow calling an agent that never existed,
a schema that no longer parses. Run with `python3 -m pytest ai-system/tests -q`
or directly with `python3 ai-system/tests/test_system_integrity.py`.

Only the standard library plus PyYAML is required.
"""
from __future__ import annotations

import json
import pathlib
import re
import unittest

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Counts the organisation is contractually required to have. If you deliberately change the
# shape of the org, change these numbers in the same commit and say why in the message.
REQUIRED = {
    "planning_agents": 50,   # finance + business + engineering + orchestration specialists
    "design_agents": 14,     # the design domain
    "improvement_agents": 12,  # the self-improvement domain
    "hardware_agents": 15,   # 3D/mechanical and PCB/electronics
    "council_agents": 10,    # the critics
    "heads": 8,              # finance, business, engineering, design, hardware, orchestration, improvement, council
    "directors": 1,          # exactly one top-level owner
    "min_skills": 100,       # the floor; the library is far larger
}
PLANNING_DOMAINS = {"finance", "business", "engineering", "orchestration"}
MODEL_TIERS = {"haiku", "sonnet", "opus"}

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def parse_frontmatter(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    assert match, f"{path.relative_to(ROOT)} has no YAML frontmatter"
    return yaml.safe_load(match.group(1))


def load_registry() -> list[dict]:
    return yaml.safe_load((ROOT / "agents" / "registry.yaml").read_text())["agents"]


def load_skill_registry() -> list[dict]:
    return yaml.safe_load((ROOT / "skills" / "registry.yaml").read_text())["skills"]


class TestAgents(unittest.TestCase):
    def setUp(self):
        self.agents = load_registry()
        self.ids = {a["id"] for a in self.agents}

    def test_registry_matches_files_on_disk(self):
        on_disk = {p.stem for p in (ROOT / "agents").rglob("*.md")
                   if p.name not in ("AGENT_INDEX.md", "README.md")}
        self.assertEqual(self.ids, on_disk,
                         "agents/registry.yaml and the files in agents/ have drifted apart")

    def test_ids_are_unique(self):
        self.assertEqual(len(self.ids), len(self.agents), "duplicate agent id in registry")

    def test_required_counts(self):
        tiers = {}
        for a in self.agents:
            tiers[a["tier"]] = tiers.get(a["tier"], 0) + 1
        self.assertEqual(tiers.get("council"), REQUIRED["council_agents"])
        self.assertEqual(tiers.get("head"), REQUIRED["heads"])
        self.assertEqual(tiers.get("director"), REQUIRED["directors"])

        specialists = [a for a in self.agents if a["tier"] == "specialist"]
        by_domain = {}
        for a in specialists:
            by_domain[a["domain"]] = by_domain.get(a["domain"], 0) + 1
        planning = sum(n for d, n in by_domain.items() if d in PLANNING_DOMAINS)
        self.assertEqual(planning, REQUIRED["planning_agents"])
        self.assertEqual(by_domain.get("design"), REQUIRED["design_agents"])
        self.assertEqual(by_domain.get("improvement"), REQUIRED["improvement_agents"])
        self.assertEqual(by_domain.get("hardware"), REQUIRED["hardware_agents"])

    def test_every_agent_has_a_valid_model_tier(self):
        for a in self.agents:
            self.assertIn(a["model"], MODEL_TIERS, f"{a['id']} has model {a['model']}")
            self.assertIn(a["escalates_to_model"], MODEL_TIERS)
            self.assertIn(a["task_class"], {"mechanical", "analytical", "judgement"})

    def test_judgement_work_is_not_on_a_cheap_tier(self):
        """Arbitration and irreversible decisions stay on the strongest tier, whatever it costs."""
        for a in self.agents:
            if a["tier"] in ("director", "head", "council"):
                self.assertEqual(a["model"], "opus",
                                 f"{a['id']} arbitrates but runs on {a['model']}")
            if a["task_class"] == "judgement":
                self.assertEqual(a["model"], "opus")

    def test_every_agent_has_context_and_return_budgets(self):
        for a in self.agents:
            self.assertGreater(a["context_budget_tokens"], 0, f"{a['id']} has no context budget")
            self.assertGreater(a["return_budget_tokens"], 0, f"{a['id']} has no return budget")
            self.assertLess(a["return_budget_tokens"], a["context_budget_tokens"],
                            f"{a['id']} returns more than it may receive")

    def test_reporting_lines_resolve(self):
        for a in self.agents:
            if a["tier"] == "director":
                self.assertEqual(a["reports_to"], "human-founder",
                                 "the Director reports to the human, nobody else")
            else:
                self.assertIn(a["reports_to"], self.ids,
                              f"{a['id']} reports to {a['reports_to']}, which does not exist")

    def test_no_reporting_cycles(self):
        for a in self.agents:
            seen, node = {a["id"]}, a
            while node["tier"] != "director":
                parent = node["reports_to"]
                self.assertNotIn(parent, seen, f"reporting cycle involving {a['id']}")
                seen.add(parent)
                node = next(x for x in self.agents if x["id"] == parent)

    def test_every_agent_reaches_the_director(self):
        for a in self.agents:
            hops, node = 0, a
            while node["tier"] != "director" and hops < 10:
                node = next(x for x in self.agents if x["id"] == node["reports_to"])
                hops += 1
            self.assertEqual(node["tier"], "director",
                             f"{a['id']} does not report up to the director")

    def test_frontmatter_matches_registry(self):
        for a in self.agents:
            fm = parse_frontmatter(ROOT / a["path"])
            self.assertEqual(fm["name"], a["id"])
            self.assertEqual(fm["reports_to"], a["reports_to"])
            self.assertEqual(fm["tier"], a["tier"])
            self.assertEqual(sorted(fm["skills"]), sorted(a["skills"]))

    def test_agents_have_required_sections(self):
        required = ["## Mission", "## Charter", "## Operating procedure",
                    "## Memory & context contract", "## Return contract",
                    "## Escalation & handoffs", "## Guardrails", "## Definition of done"]
        for a in self.agents:
            body = (ROOT / a["path"]).read_text()
            for section in required:
                self.assertIn(section, body, f"{a['id']} is missing {section}")

    def test_shared_boilerplate_is_referenced_not_duplicated(self):
        """Guardrails live once in the base prompt. A charter that restates them has drifted."""
        base = (ROOT / "prompts" / "system" / "00-base-agent.md").read_text()
        self.assertIn("Evidence has a grade", base, "the shared guardrails must live in the base prompt")
        for a in self.agents:
            body = (ROOT / a["path"]).read_text()
            self.assertIn("prompts/system/00-base-agent.md", body,
                          f"{a['id']} does not point at the shared guardrails")

    def test_agents_declare_memory_scopes(self):
        for a in self.agents:
            self.assertTrue(a["memory_scopes"], f"{a['id']} declares no memory scopes")

    def test_agents_declare_a_return_contract(self):
        for a in self.agents:
            body = (ROOT / a["path"]).read_text()
            self.assertIn("## Return contract", body, f"{a['id']} has no return contract")
            self.assertIn("never its working context", body)

    def test_hardware_judgement_work_is_tiered_correctly(self):
        """Tooling, board spins, and certification are one-way doors."""
        for name in ("pcb-schematic-designer", "dfm-engineer", "compliance-emc-engineer"):
            agent = next(a for a in self.agents if a["id"] == name)
            self.assertEqual(agent["task_class"], "judgement",
                             f"{name} makes expensive-to-reverse decisions")
            self.assertEqual(agent["model"], "opus")

    def test_council_reports_to_council_director(self):
        for a in self.agents:
            if a["tier"] == "council" and a["id"] != "council-director":
                self.assertEqual(a["reports_to"], "council-director")

    def test_profiles_satisfy_the_schema(self):
        schema = json.loads((ROOT / "knowledge-schema" / "agent-profile.schema.json").read_text())
        for a in self.agents:
            for field in schema["required"]:
                self.assertIn(field, a, f"{a['id']} is missing required field {field}")
            self.assertIn(a["tier"], schema["properties"]["tier"]["enum"])
            self.assertIn(a["domain"], schema["properties"]["domain"]["enum"])


class TestSkills(unittest.TestCase):
    def setUp(self):
        self.skills = load_skill_registry()
        self.names = {s["name"] for s in self.skills}
        self.agents = load_registry()

    def test_minimum_library_size(self):
        self.assertGreaterEqual(len(self.skills), REQUIRED["min_skills"])

    def test_registry_matches_files_on_disk(self):
        on_disk = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        self.assertEqual(self.names, on_disk,
                         "skills/registry.yaml and the directories in skills/ have drifted apart")

    def test_every_agent_skill_reference_resolves(self):
        for a in self.agents:
            for skill in a["skills"]:
                self.assertIn(skill, self.names,
                              f"{a['id']} references skill '{skill}', which does not exist")

    def test_skill_files_have_a_procedure_and_a_quality_bar(self):
        for s in self.skills:
            body = (ROOT / s["path"]).read_text()
            self.assertIn("## Procedure", body, f"{s['name']} has no procedure")
            self.assertIn("## Quality bar", body, f"{s['name']} has no quality bar")
            self.assertIn("## Output contract", body, f"{s['name']} has no output contract")
            steps = re.findall(r"^\d+\. ", body, re.M)
            self.assertGreaterEqual(len(steps), 5, f"{s['name']} has fewer than five steps")

    def test_skills_point_at_the_shared_output_contract(self):
        """The output format lives once. 590 copies of it is ~100k tokens of duplication."""
        shared = ROOT / "skills" / "OUTPUT_CONTRACT.md"
        self.assertTrue(shared.exists(), "skills/OUTPUT_CONTRACT.md is missing")
        for s in self.skills:
            body = (ROOT / s["path"]).read_text()
            self.assertIn("skills/OUTPUT_CONTRACT.md", body,
                          f"{s['name']} does not point at the shared output contract")

    def test_every_skill_is_referenced_by_an_agent(self):
        """An orphan skill is dead weight: nobody can invoke it and nobody maintains it."""
        referenced = {sk for a in self.agents for sk in a["skills"]}
        orphans = sorted(self.names - referenced)
        self.assertEqual(orphans, [], f"skills referenced by no agent: {orphans}")

    def test_every_category_has_an_antipatterns_file(self):
        categories = {s["category"] for s in self.skills}
        for c in categories:
            path = ROOT / "skills" / "antipatterns" / f"{c}.md"
            self.assertTrue(path.exists(), f"no anti-patterns file for category {c}")

    def test_frontmatter_matches_registry(self):
        for s in self.skills:
            fm = parse_frontmatter(ROOT / s["path"])
            self.assertEqual(fm["name"], s["name"])
            self.assertEqual(fm["category"], s["category"])

    def test_used_by_is_consistent_with_agent_definitions(self):
        actual = {}
        for a in self.agents:
            for skill in a["skills"]:
                actual.setdefault(skill, set()).add(a["id"])
        for s in self.skills:
            self.assertEqual(set(s["used_by"]), actual.get(s["name"], set()),
                             f"used_by for {s['name']} does not match the agent definitions")


class TestWorkflows(unittest.TestCase):
    def setUp(self):
        self.agent_ids = {a["id"] for a in load_registry()}
        self.skill_names = {s["name"] for s in load_skill_registry()}
        self.workflows = {p.name: yaml.safe_load(p.read_text())
                          for p in (ROOT / "workflows").glob("*.yaml")}

    def test_workflows_exist(self):
        self.assertGreaterEqual(len(self.workflows), 10)

    def test_every_step_names_a_real_agent_and_real_skills(self):
        for name, wf in self.workflows.items():
            for step in wf["steps"]:
                self.assertIn(step["agent"], self.agent_ids,
                              f"{name} step '{step['id']}' names unknown agent {step['agent']}")
                for skill in step["skills"]:
                    self.assertIn(skill, self.skill_names,
                                  f"{name} step '{step['id']}' names unknown skill {skill}")

    def test_every_step_has_a_completion_condition(self):
        for name, wf in self.workflows.items():
            for step in wf["steps"]:
                self.assertTrue(step.get("done_when"), f"{name}:{step['id']} has no done_when")
                self.assertTrue(step.get("produces"), f"{name}:{step['id']} produces nothing")

    def test_every_workflow_has_an_owner_and_exit_criteria(self):
        for name, wf in self.workflows.items():
            self.assertIn(wf["owner"], self.agent_ids, f"{name} has an unknown owner")
            self.assertTrue(wf.get("exit_criteria"), f"{name} has no exit criteria")

    def test_material_workflows_include_a_council_review(self):
        """Stage-advancing workflows must route through the Council somewhere."""
        must_review = ["01-business-model-design.yaml", "03-mvp-definition.yaml",
                       "07-upgrade-and-scale.yaml", "12-quarterly-planning.yaml"]
        for name in must_review:
            wf = self.workflows[name]
            agents = {s["agent"] for s in wf["steps"]}
            self.assertTrue(any(a.startswith("council") for a in agents),
                            f"{name} advances a stage without a Council step")


class TestSchemas(unittest.TestCase):
    def test_all_schemas_parse_and_are_self_describing(self):
        files = list((ROOT / "knowledge-schema").glob("*.schema.json"))
        self.assertGreaterEqual(len(files), 10)
        for path in files:
            schema = json.loads(path.read_text())
            self.assertIn("$schema", schema, f"{path.name} declares no $schema")
            self.assertIn("title", schema, f"{path.name} has no title")
            self.assertIn("description", schema, f"{path.name} has no description")
            self.assertEqual(schema["type"], "object")
            for field in schema.get("required", []):
                self.assertIn(field, schema["properties"],
                              f"{path.name} requires '{field}' but never defines it")

    def test_memory_records_require_provenance(self):
        schema = json.loads((ROOT / "knowledge-schema" / "memory-record.schema.json").read_text())
        self.assertIn("provenance", schema["required"],
                      "a memory without provenance cannot be trusted later")

    def test_council_findings_require_a_failure_scenario(self):
        schema = json.loads((ROOT / "knowledge-schema" / "council-verdict.schema.json").read_text())
        finding = schema["properties"]["findings"]["items"]
        self.assertIn("failure_scenario", finding["required"],
                      "a finding without a concrete failure scenario is an adjective, not a finding")


class TestProgressiveDisclosure(unittest.TestCase):
    """The tiered indexes are what make the library affordable. If they drift, the design is gone."""

    def setUp(self):
        self.agents = load_registry()
        self.skills = load_skill_registry()
        self.budget = yaml.safe_load((ROOT / "runtime" / "context-budget.yaml").read_text())

    def _tsv_rows(self, path):
        return [line.split("\t") for line in path.read_text().splitlines()
                if line and not line.startswith("#")]

    def test_domain_index_covers_every_domain(self):
        rows = self._tsv_rows(ROOT / "agents" / "index" / "_domains.tsv")
        indexed = {r[0] for r in rows}
        actual = {a["domain"] for a in self.agents}
        self.assertEqual(indexed, actual, "agents/index/_domains.tsv has drifted from the registry")

    def test_domain_index_counts_are_correct(self):
        counts = {}
        for a in self.agents:
            counts[a["domain"]] = counts.get(a["domain"], 0) + 1
        for row in self._tsv_rows(ROOT / "agents" / "index" / "_domains.tsv"):
            self.assertEqual(int(row[2]), counts[row[0]],
                             f"domain index claims the wrong agent count for {row[0]}")

    def test_every_agent_appears_in_exactly_one_domain_card_file(self):
        seen = {}
        for path in (ROOT / "agents" / "index").glob("*.tsv"):
            if path.stem.startswith("_"):
                continue
            for row in self._tsv_rows(path):
                self.assertNotIn(row[0], seen, f"{row[0]} appears in two domain card files")
                seen[row[0]] = path.stem
        self.assertEqual(set(seen), {a["id"] for a in self.agents})
        for a in self.agents:
            self.assertEqual(seen[a["id"]], a["domain"])

    def test_skill_index_covers_every_skill_exactly_once(self):
        seen = set()
        for path in (ROOT / "skills" / "index").glob("*.tsv"):
            if path.stem.startswith("_"):
                continue
            for row in self._tsv_rows(path):
                self.assertNotIn(row[0], seen, f"{row[0]} indexed twice")
                seen.add(row[0])
        self.assertEqual(seen, {s["name"] for s in self.skills},
                         "skills/index has drifted from skills/registry.yaml")

    def test_tier_one_discovery_fits_its_budget(self):
        """Routing must be affordable, or agents will skip it and load everything instead."""
        limit = self.budget["tiers"]["tier_1_discovery"]["budget"]
        domains = len((ROOT / "agents" / "index" / "_domains.tsv").read_text()) // 4
        worst_agent_shard = max(
            len(p.read_text()) // 4 for p in (ROOT / "agents" / "index").glob("*.tsv")
            if not p.stem.startswith("_"))
        worst_skill_shard = max(
            len(p.read_text()) // 4 for p in (ROOT / "skills" / "index").glob("*.tsv")
            if not p.stem.startswith("_"))
        worst = domains + worst_agent_shard + worst_skill_shard
        self.assertLess(worst, limit,
                        f"worst-case tier-1 discovery is {worst} tokens, over the {limit} budget")

    def test_model_routing_table_matches_the_registry(self):
        routing = yaml.safe_load((ROOT / "runtime" / "model-routing.yaml").read_text())
        table = {r["id"]: r for r in routing["agents"]}
        self.assertEqual(set(table), {a["id"] for a in self.agents})
        for a in self.agents:
            self.assertEqual(table[a["id"]]["model"], a["model"])
            self.assertEqual(table[a["id"]]["escalates_to"], a["escalates_to_model"])

    def test_cache_order_puts_variable_content_last(self):
        order = self.budget["cache_order"]
        self.assertEqual(order[-2:], ["context package", "task"],
                         "variable content must come last or the stable prefix stops being cacheable")


class TestSelfImprovementSafety(unittest.TestCase):
    """The improvement loop may change the system. These are the limits on that."""

    def test_evaluation_criteria_are_not_self_modifiable(self):
        policy = (ROOT / "prompts" / "system" / "06-self-modification.md").read_text()
        self.assertIn("Evaluation criteria", policy)
        self.assertIn("Human founder", policy)
        schema = json.loads(
            (ROOT / "knowledge-schema" / "improvement-proposal.schema.json").read_text())
        levels = schema["properties"]["authorisation_level"]["enum"]
        self.assertIn("human_founder", levels)
        classes = schema["properties"]["target"]["properties"]["artifact_class"]["enum"]
        for protected in ("guardrail", "schema", "org_shape", "evaluation_criteria"):
            self.assertIn(protected, classes,
                          f"{protected} must be a nameable artifact class so it can be gated")

    def test_proposals_require_a_diagnosis_before_a_change(self):
        schema = json.loads(
            (ROOT / "knowledge-schema" / "improvement-proposal.schema.json").read_text())
        self.assertIn("diagnosis", schema["required"])
        diagnosis = schema["properties"]["diagnosis"]
        self.assertIn("attribution", diagnosis["required"],
                      "a proposal must say whether the cause was capability, context, or task definition")
        self.assertGreaterEqual(diagnosis["properties"]["instances"]["minimum"], 3,
                                "three independent instances before calling something a pattern")

    def test_variants_change_one_dimension(self):
        schema = json.loads(
            (ROOT / "knowledge-schema" / "improvement-proposal.schema.json").read_text())
        dims = schema["properties"]["proposed_change"]["properties"]["dimensions_changed"]
        self.assertEqual(dims["maximum"], 1, "one dimension per variant or the effect is unattributable")

    def test_agent_returns_are_budget_capped(self):
        schema = json.loads((ROOT / "knowledge-schema" / "agent-return.schema.json").read_text())
        self.assertIn("tokens_used", schema["required"],
                      "an agent that cannot report its cost cannot be optimised")
        self.assertIn("maxLength", schema["properties"]["summary"])

    def test_improvement_workflow_gates_adoption_on_a_trial(self):
        wf = yaml.safe_load((ROOT / "workflows" / "15-self-improvement.yaml").read_text())
        ids = [s["id"] for s in wf["steps"]]
        for gate in ("measure", "diagnose", "trial", "sweep", "authorise", "adopt", "verify"):
            self.assertIn(gate, ids, f"self-improvement workflow is missing the {gate} gate")
        self.assertLess(ids.index("trial"), ids.index("adopt"), "adoption must follow the trial")
        self.assertLess(ids.index("sweep"), ids.index("adopt"), "adoption must follow the sweep")
        self.assertLess(ids.index("authorise"), ids.index("adopt"),
                        "adoption must follow the authorisation check")


if __name__ == "__main__":
    unittest.main(verbosity=2)
