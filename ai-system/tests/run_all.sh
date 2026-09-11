#!/usr/bin/env bash
# Run every check. Pass a repeat count to run the whole suite N times.
#   bash ai-system/tests/run_all.sh        # once
#   bash ai-system/tests/run_all.sh 10     # ten times, failing on the first failure
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
N="${1:-1}"

for i in $(seq 1 "$N"); do
  echo "──────────────────────────────────────── pass $i/$N"
  integrity="$(python3 "$ROOT/ai-system/tests/test_system_integrity.py" 2>&1)"
  echo "$integrity" | tail -3
  conformance="$(python3 "$ROOT/ai-system/tests/test_conformance.py" 2>&1)"
  echo "$conformance" | tail -3
  runtime="$(python3 "$ROOT/ai-system/tests/test_runtime.py" 2>&1)"
  echo "$runtime" | tail -3
  bench="$(python3 "$ROOT/ai-system/tests/benchmark.py")"
  echo "$bench" | tail -1
done

echo "──────────────────────────────────────── determinism"
determinism="$(python3 "$ROOT/ai-system/tests/benchmark.py" --repeat 25)"
echo "$determinism" | head -1

echo "──────────────────────────────────────── portability"
python3 "$ROOT/ai-system/tools/eval.py" --dry-run
python3 "$ROOT/ai-system/tools/export.py" --out "$ROOT/ai-system/dist" >/dev/null
echo "export ok (all formats)"
python3 "$ROOT/ai-system/tools/loader.py" assemble --agent director --task smoke >/dev/null
echo "loader ok (assembles within budget)"

echo "──────────────────────────────────────── bootstrap smoke test"
rm -rf "$ROOT/workspace/suite-check"
bash "$ROOT/ai-system/bootstrap/init.sh" suite-check >/dev/null
test -f "$ROOT/workspace/suite-check/venture.yaml"
test -d "$ROOT/workspace/suite-check/telemetry/token-ledger"
if bash "$ROOT/ai-system/bootstrap/init.sh" suite-check >/dev/null 2>&1; then
  echo "FAIL: init.sh overwrote an existing venture"; exit 1
fi
if bash "$ROOT/ai-system/bootstrap/init.sh" "Bad ID" >/dev/null 2>&1; then
  echo "FAIL: init.sh accepted an invalid venture id"; exit 1
fi
rm -rf "$ROOT/workspace/suite-check"
echo "bootstrap ok (scaffolds, refuses overwrite, rejects bad id)"

echo "──────────────────────────────────────── all checks passed"
