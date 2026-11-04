# DSH schema3 bounded continuation — reviewed candidate

The owner authorized packet B immediately after the ordinary-compatibility candidate. Data: branch `dsh/continuation` (from `7a86a39`, the reviewed compat candidate), worktree `/private/tmp/methodology-dsh-cont-20261104`, source baseline `a3ecb5c` (neutral4.1 plus the checked Codex5.0 candidate). DSH package is now5.0.0 over neutral4.1.0; persistent schema3 is current, role wire stays `methodology-dsh/2.0.0`, default4/scans/roles are unchanged. No merge, push, installation, profile repoint or sibling write occurred.

## Actual change set

- `skills/feature-dev/scripts/run_state.py` carries the reviewed schema3 lineage contract: one enrolled authority at `.methodology/lineages/<causal-id>/state.json`, spec admissions, immutable closed artifacts, editioned journal, pre-dispatch reservations, conservative recovery, retained retry episodes and a read-only `capabilities` command. `skills/feature-dev/scripts/continuation.py` (new,769 lines) owns lineage/reservation/historical-import mechanics without launching workers.
- CLI: `capabilities`, `init`, `show`, `record`, `continue`, `reserve`, `released`, `recover`, `episode`. `continue --predecessor TERMINAL --request PARENT_JSON` admits only a complete native-only DSH4.0/4.1 schema2 terminal or this contract's own closed schema3 terminal. No `--parent` wallet, no Codex/Claude ledger, no active schema2 migration. Foreign wire/profile/external-accounting/`--parent` boundaries have discriminating refusals in the suite.
- Population: 77 declared members (78 shipped with the map), seven helper modules, 27 skills, six roles; adapter unchanged at neutral4.1.0, 71 files, 28 capabilities, 7 parameters. `package.json`/plugin manifest/package-layout are5.0.0.
- Tests: new `tests/test_continuation.py`; `test_run_state.py`, `test_adoption.py` and `test_native_contract.py` adapted to schema3 counts/identity; none skipped. Current guide facts and a continuation test-map section updated.
- Current-release guidance in `README.md`, `references/{adoption,consumer-pm-profile,dsh-runtime,handoffs,source-disposition}.md`, `skills/feature-dev/SKILL.md` (full schema3 control section), `skills/pm/SKILL.md`, `skills/devplan-protocol/SKILL.md` and `skills/semantic-exoskeleton/SKILL.md`.

## Actual evidence

- Package suite on a complete Git-free source copy, exposed streams at private `package-suite-final.log`:
  `PYTHONDONTWRITEBYTECODE=1 python3.12 -m pytest -c implementations/dsh/pytest.ini implementations/dsh/tests -p no:cacheprovider -s -v --basetemp PRIVATE` → **202 passed, exit0**, zero skipped (64.07s). The earlier199/73.98s run is retained as history; both failures found during development were repaired and re-run, not skipped.
- Configured package Doxygen: exit0 with empty stdout/stderr; XML rebuilt but not tracked (279 function entries).
- Native parent proof bound to the final source, complete private receipts (`step1.json`, `native-proof.json`, both worker reports and markers):
  1. A real schema2 terminal was created by the accepted DSH4.1 compat shipped CLI (BLOCKED bootstrap) and hashed before import.
  2. The DSH5 CLI `continue` admitted it into schema3 (lineage `65b5155c…`, `phase architect`), enrolled the spec admission, left the original schema2 bytes identical, and `show` on the new authority exited0 against the final source bindings.
  3. Architect entry `edc85439…` was reserved (charge0), read back, and dispatched to a real DSH subagent worker (`a25334b2-…`); the worker observed the reserved entry and wrote its marker outside the target. The parent released it with that actual session locator and recorded the canonical Architect SUCCESS.
  4. Accepting Architect precharged the causal Code entry: `debug_spent1/cap4`, entry `a3d99d42…` charge1. `reserve` persisted the reservation; a second real DSH subagent worker (`4a5026d8-…`) observed `spent1`, `charge1`, `state reserved`, `worker null` and wrote a marker under the excluded `.methodology/` directory.
  5. The parent released that entry with the actual worker locator, recorded a canonical Code BLOCKED closure, and the lineage published one immutable closed artifact (49232 bytes, sha256 `72971d2b…`). `show` on that closed authority still exits0 against the final bindings; further `reserve` refuses exit2; the legacy schema2 bytes remain unchanged.
- Earlier probes ran before subsequent package edits (a fixture-path rename, then the guide count) and therefore no longer matched the final bindings; the first one and its retained refusal are archived under `superseded-first-probe/`. The proof above is the final source-bound run: `show` on the closed authority exits0 against the committed package bytes.

## Independent review and closure — 2026-11-04

A distinct fresh-context reviewer inspected commit `5b9b1ed` read-only, ran the suite on its own Git-free archive (**199 passed, 81.33s**), Doxygen (279 members), `capabilities`, its own schema3 route, the admission-boundary probes and the root selector check. Verdict: **PASS WITH LIMITS**, no behavioral defect; one medium evidentiary finding and three minor ones were closed:

- MEDIUM: the recorded native proof was not bound to the candidate (one test fixture path changed after the probe). The proof was re-run from the final source as recorded above; `show` exits0 on the closed authority; the old receipts are retained as superseded history.
- LOW: the receipt's `continuation.py` line count now reads769; the guide's stale schema2 "current" facts were corrected; three negative controls now cover Codex wire, neutral5.0 and external parent/wallet admission (suite202).

The reviewer's limits stand: markers and worker strings are parent-authored and corroborated only through actual harness session records; no worker-independence, dispatch-order, exactly-once, cross-host or power-loss proof; root full/sibling regressions and installed-profile state were not exercised.

## Limits

Not merged, installed, repointed or advertised: both installed profiles still resolve the unchanged main symlink at4.0.0. No combined root/sibling regression, no Codex/Claude continuation parity and no product/Jeni execution occurred. The native proof covers one owned inert lineage and two owned workers; `reuse_code`, malformed-stream recovery and episode limits are covered by package tests, not by a second native dispatch campaign. The contract keeps its declared limits: one parent writer/storage domain, parent-authenticated consent, unknown-release hold, no exactly-once, cross-host or power-loss guarantee, and no scheduler.

Root selector updates (`tests/test_dsh_package.py` still pins4.0.0/75 and fails by design), combined sibling regressions, the separate concrete-result/integration and installation decisions remain outside this packet.

## Private evidence index

Ignored `.methodology/dsh-continuation/evidence/` in this worktree holds the final suite log, Doxygen streams, source-bound step receipts, both worker reports and markers with `SHA256SUMS`, plus `superseded-first-probe/`; `/private/tmp/dsh-cont-evidence2/` is the live final home and `/private/tmp/dsh-cont-evidence/` the superseded one. Public locators are logical; raw streams are not tracked artifacts.
