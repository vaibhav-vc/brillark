"""A working memory store for the organisation.

Until now `docs/memory-model.md` described a memory system and nothing implemented one. This does:
schema-validated writes with mandatory provenance, scope-filtered retrieval, contradiction detection
at write time, consolidation of repeated episodes into semantic memory, and decay.

    python3 ai-system/tools/memory.py write   --venture acme --file record.json
    python3 ai-system/tools/memory.py recall  --venture acme --scope "venture.acme.finance" --limit 5
    python3 ai-system/tools/memory.py consolidate --venture acme
    python3 ai-system/tools/memory.py stale   --venture acme
    python3 ai-system/tools/memory.py stats   --venture acme

Storage is JSON files under workspace/<venture>/memory/. Deliberately boring: the contract matters,
the backend does not, and a file per record stays diffable and inspectable.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKSPACE = ROOT.parent / "workspace"
GRADES = ["guessed", "estimated", "benchmarked", "sourced", "measured"]
TYPES = ["episodic", "semantic", "procedural", "decision"]
# Shelf life by type. Market facts rot; decisions do not.
SHELF_LIFE = {"episodic": 90, "semantic": 180, "procedural": 365, "decision": 3650}
PROMOTION_THRESHOLD = 3  # independent episodes before a fact becomes semantic


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def mem_dir(venture: str) -> pathlib.Path:
    return WORKSPACE / venture / "memory"


def record_id(claim: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", claim.lower())[:40].strip("-")
    digest = hashlib.sha256(claim.encode()).hexdigest()[:6]
    return f"mem_{slug}-{digest}"


def load_all(venture: str) -> list[dict]:
    out = []
    for path in sorted(mem_dir(venture).rglob("*.json")):
        try:
            out.append(json.loads(path.read_text()))
        except json.JSONDecodeError:
            print(f"warning: {path} is not valid JSON, skipping", file=sys.stderr)
    return out


def validate(record: dict) -> list[str]:
    """Enforce the contract. A record that cannot be trusted later must not be written now."""
    problems = []
    for field in ("type", "claim", "scope", "provenance"):
        if field not in record:
            problems.append(f"missing required field '{field}'")
    if record.get("type") not in TYPES:
        problems.append(f"type must be one of {TYPES}")
    claim = record.get("claim", "")
    if len(claim) < 10:
        problems.append("claim must be a standalone statement, not a fragment")
    for pronoun in (" it ", " this ", " they "):
        if claim.lower().startswith(pronoun.strip()) or claim.lower()[:12].find(pronoun) == 0:
            problems.append("claim appears to depend on surrounding context; make it standalone")
    prov = record.get("provenance", {})
    for field in ("author_agent", "evidence_grade"):
        if field not in prov:
            problems.append(f"provenance missing '{field}' — an untraceable claim cannot be trusted")
    grade = prov.get("evidence_grade")
    if grade not in GRADES:
        problems.append(f"evidence_grade must be one of {GRADES}")
    # Anything above 'estimated' asserts an external source exists. Make it name one.
    if grade in ("sourced", "measured", "benchmarked") and not prov.get("source_artifacts"):
        problems.append(f"grade '{grade}' requires source_artifacts naming where it came from")
    return problems


def find_contradictions(record: dict, existing: list[dict]) -> list[dict]:
    """Catch a conflicting claim at write time. Two contradicting facts must never both be stored.

    Heuristic and deliberately conservative: same scope, same subject fingerprint, different claim.
    It will miss subtle conflicts; it catches the common case of a number being silently replaced.
    """
    def fingerprint(text: str) -> set[str]:
        words = re.findall(r"[a-z]{4,}", text.lower())
        stop = {"that", "this", "with", "from", "have", "will", "been", "were", "they", "their",
                "about", "would", "which", "there", "than", "then", "when", "what"}
        return {w for w in words if w not in stop}

    conflicts = []
    new_fp = fingerprint(record["claim"])
    numbers_new = set(re.findall(r"\d+(?:[.,]\d+)?", record["claim"]))
    for other in existing:
        if other.get("status") in ("superseded", "archived"):
            continue
        if other.get("scope") != record.get("scope"):
            continue
        if other.get("claim") == record.get("claim"):
            continue
        overlap = new_fp & fingerprint(other["claim"])
        if len(overlap) < 3:
            continue
        numbers_old = set(re.findall(r"\d+(?:[.,]\d+)?", other["claim"]))
        # Strong signal: same subject words, different numbers.
        if numbers_new and numbers_old and numbers_new != numbers_old:
            conflicts.append(other)
        elif len(overlap) >= 5 and not numbers_new and not numbers_old:
            conflicts.append(other)
    return conflicts


def _attribution(claim: str) -> str | None:
    """Who is making this claim? 'AirDNA reported X' is attributed; 'X is true' is not.

    Attribution is what separates two sources disagreeing from memory contradicting itself.
    """
    match = re.match(r"([A-Z][A-Za-z0-9&.\- ]{1,30}?)\s+(?:reported|reports|states|found|claims|"
                     r"estimated|estimates|published)\b", claim)
    return match.group(1).strip() if match else None


def contest(venture: str, record: dict, other_id: str, note: str) -> int:
    """Store both claims, mutually marked as contested. Disagreement preserved, not averaged."""
    if not note:
        print("--contest needs --note explaining why the sources differ", file=sys.stderr)
        return 1
    record.setdefault("id", record_id(record["claim"]))
    record["status"] = "contested"
    record["contested_with"] = [other_id]
    record["contest_note"] = note
    record["provenance"].setdefault("created_at", now())
    record.setdefault("shelf_life_days", SHELF_LIFE[record["type"]])
    target = mem_dir(venture) / record["type"] / f"{record['id']}.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(record, indent=2, sort_keys=True))

    for path in mem_dir(venture).rglob(f"{other_id}.json"):
        other = json.loads(path.read_text())
        other["status"] = "contested"
        other.setdefault("contested_with", []).append(record["id"])
        other["contest_note"] = note
        path.write_text(json.dumps(other, indent=2, sort_keys=True))

    print(f"recorded as contested: {record['id']} <-> {other_id}")
    print(f"  note: {note}")
    print("  Both remain retrievable. Any agent recalling either sees the disagreement.")
    return 0


def write(venture: str, record: dict, force: bool = False) -> int:
    problems = validate(record)
    if problems:
        print("REJECTED — the write contract was not met:")
        for p in problems:
            print(f"  - {p}")
        return 1

    record.setdefault("id", record_id(record["claim"]))
    record.setdefault("status", "active")
    record["provenance"].setdefault("created_at", now())
    record.setdefault("shelf_life_days", SHELF_LIFE[record["type"]])

    existing = load_all(venture)
    conflicts = find_contradictions(record, existing)
    if conflicts and not force:
        print(f"CONTRADICTION — this write conflicts with {len(conflicts)} stored claim(s):")
        for c in conflicts:
            print(f"  stored : {c['claim']}")
            print(f"           ({c['id']}, grade {c['provenance']['evidence_grade']}, "
                  f"{c['provenance'].get('created_at', 'undated')})")
        print(f"  new    : {record['claim']}")
        # Two sources disagreeing is NOT the same as memory contradicting itself. The research
        # doctrine says preserve disagreement; the memory doctrine says never store both. Both are
        # right about different situations, so name which one this is.
        attributed = _attribution(record["claim"])
        others = {_attribution(c["claim"]) for c in conflicts} - {None}
        if attributed and others and attributed not in others:
            print(f"\nThese look like ATTRIBUTED DISAGREEMENT, not contradiction:")
            print(f"  '{attributed}' vs {sorted(o for o in others if o)}")
            print("  Different sources disagreeing is a finding to preserve, not a conflict to resolve.")
            print("  Record it as contested so both survive and the disagreement stays visible:")
            print(f"    --contest {conflicts[0]['id']} --note '<why they differ>'")
            print("\n  If this really is memory contradicting itself, use --supersede instead.")
        else:
            print("\nMemory never stores two contradicting facts. Resolve by supersession:")
            print("  re-run with --supersede <id> to mark the loser superseded, or --force to override.")
        return 2

    target = mem_dir(venture) / record["type"] / f"{record['id']}.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(record, indent=2, sort_keys=True))
    print(f"wrote {target.relative_to(WORKSPACE)}")
    return 0


def supersede(venture: str, loser_id: str, winner_id: str) -> int:
    for path in mem_dir(venture).rglob(f"{loser_id}.json"):
        record = json.loads(path.read_text())
        record["status"] = "superseded"
        record["superseded_by"] = winner_id
        record["superseded_at"] = now()
        path.write_text(json.dumps(record, indent=2, sort_keys=True))
        print(f"{loser_id} superseded by {winner_id} (kept, not deleted — history stays auditable)")
        return 0
    print(f"no record {loser_id}", file=sys.stderr)
    return 1


def recall(venture: str, scope: str | None, limit: int, min_grade: str | None) -> int:
    records = [r for r in load_all(venture) if r.get("status") in ("active", "contested")]
    if scope:
        pattern = scope.replace(".", r"\.").replace("*", ".*")
        records = [r for r in records if re.fullmatch(pattern, r.get("scope", ""))]
    if min_grade:
        floor = GRADES.index(min_grade)
        records = [r for r in records
                   if GRADES.index(r["provenance"]["evidence_grade"]) >= floor]
    # Strongest evidence first, then most recent. Digest-first: claim only, fetch detail on demand.
    records.sort(key=lambda r: (GRADES.index(r["provenance"]["evidence_grade"]),
                                r["provenance"].get("created_at", "")), reverse=True)
    stale_count = 0
    for record in records[:limit]:
        marker = ""
        if record.get("status") == "contested":
            marker = f"  [CONTESTED with {len(record.get('contested_with', []))} other claim(s)]"
        if is_stale(record):
            marker += "  [STALE — re-verify before using in a decision]"
            stale_count += 1
        print(f"[{record['provenance']['evidence_grade']:<11}] {record['claim']}{marker}")
        print(f"    {record['id']}  {record['type']}  {record['scope']}  "
              f"by {record['provenance']['author_agent']}")
        if record.get("contest_note"):
            print(f"    disagreement: {record['contest_note']}")
    print(f"\n{len(records)} active records matched, showing {min(limit, len(records))}"
          + (f", {stale_count} stale" if stale_count else ""))
    return 0


def is_stale(record: dict) -> bool:
    created = record["provenance"].get("created_at")
    if not created:
        return True
    age = (dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(created)).days
    return age > record.get("shelf_life_days", 90)


def consolidate(venture: str) -> int:
    """Promote repeated episodic facts into semantic memory. Three independent episodes, per
    the memory model — fewer is a streak, not a fact."""
    records = load_all(venture)
    episodes = [r for r in records if r["type"] == "episodic" and r.get("status") == "active"]
    semantic_claims = {r["claim"] for r in records if r["type"] == "semantic"}

    groups: dict[str, list[dict]] = {}
    for record in episodes:
        key = record.get("consolidates_to") or record["claim"]
        groups.setdefault(key, []).append(record)

    promoted = 0
    for key, members in groups.items():
        authors = {m["provenance"]["author_agent"] for m in members}
        if len(members) < PROMOTION_THRESHOLD or key in semantic_claims:
            continue
        if len(authors) < 2:
            # Three observations from one agent is one perspective repeated.
            continue
        best = max(members, key=lambda m: GRADES.index(m["provenance"]["evidence_grade"]))
        new = {
            "id": record_id("semantic:" + key),
            "type": "semantic",
            "claim": key,
            "scope": best["scope"],
            "status": "active",
            "promoted_from": [m["id"] for m in members],
            "shelf_life_days": SHELF_LIFE["semantic"],
            "provenance": {
                "author_agent": "context-memory-curator",
                "skill": "memory-consolidation",
                "created_at": now(),
                "evidence_grade": best["provenance"]["evidence_grade"],
                "source_artifacts": sorted({a for m in members
                                            for a in m["provenance"].get("source_artifacts", [])}),
            },
        }
        path = mem_dir(venture) / "semantic" / f"{new['id']}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(new, indent=2, sort_keys=True))
        print(f"promoted: {key}")
        print(f"          from {len(members)} episodes by {len(authors)} agents")
        promoted += 1

    near = sum(1 for m in groups.values() if len(m) == PROMOTION_THRESHOLD - 1)
    print(f"\n{promoted} promoted to semantic memory; {near} group(s) one episode short")
    return 0


def stats(venture: str) -> int:
    records = load_all(venture)
    if not records:
        print(f"no memory for venture '{venture}'")
        return 0
    by_type: dict[str, int] = {}
    by_grade: dict[str, int] = {}
    stale = 0
    for r in records:
        by_type[r["type"]] = by_type.get(r["type"], 0) + 1
        g = r["provenance"]["evidence_grade"]
        by_grade[g] = by_grade.get(g, 0) + 1
        if r.get("status") == "active" and is_stale(r):
            stale += 1
    superseded = sum(1 for r in records if r.get("status") == "superseded")
    print(f"venture: {venture}")
    print(f"  records      {len(records)}")
    for t in TYPES:
        if by_type.get(t):
            print(f"    {t:<11} {by_type[t]}")
    print("  by grade")
    for g in reversed(GRADES):
        if by_grade.get(g):
            print(f"    {g:<11} {by_grade[g]}")
    print(f"  superseded   {superseded}")
    print(f"  stale        {stale}")
    guessed = by_grade.get("guessed", 0)
    if guessed:
        print(f"\n  {guessed} claim(s) graded 'guessed' — none may be load-bearing at a stage gate")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["write", "recall", "consolidate", "stats", "stale",
                                        "supersede"])
    ap.add_argument("--venture", required=True)
    ap.add_argument("--file", help="JSON record to write")
    ap.add_argument("--scope")
    ap.add_argument("--limit", type=int, default=12)
    ap.add_argument("--min-grade", choices=GRADES)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--supersede", dest="loser")
    ap.add_argument("--contest")
    ap.add_argument("--note")
    ap.add_argument("--winner")
    args = ap.parse_args()

    if args.command == "write":
        if not args.file:
            raise SystemExit("write needs --file")
        record = json.loads(pathlib.Path(args.file).read_text())
        if args.contest:
            return contest(args.venture, record, args.contest, args.note or "")
        if args.loser:
            supersede(args.venture, args.loser, record.get("id", record_id(record["claim"])))
            args.force = True
        return write(args.venture, record, force=args.force)
    if args.command == "recall":
        return recall(args.venture, args.scope, args.limit, args.min_grade)
    if args.command == "consolidate":
        return consolidate(args.venture)
    if args.command == "supersede":
        return supersede(args.venture, args.loser, args.winner or "manual")
    if args.command == "stale":
        stale = [r for r in load_all(args.venture) if r.get("status") == "active" and is_stale(r)]
        for r in stale:
            print(f"[stale] {r['id']}  {r['claim'][:80]}")
        print(f"\n{len(stale)} stale record(s); re-verify before any decision relies on them")
        return 0
    return stats(args.venture)


if __name__ == "__main__":
    raise SystemExit(main())
