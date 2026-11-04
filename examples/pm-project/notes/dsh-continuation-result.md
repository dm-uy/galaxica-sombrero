# DSH schema3 bounded continuation — candidate in independent review

The owner authorized packet B immediately after the ordinary-compatibility candidate. Data: branch `dsh/continuation` (from `7a86a39`, the reviewed compat candidate), worktree `/private/tmp/methodology-dsh-cont-20261104`, source baseline `a3ecb5c` (neutral4.1 plus the checked Codex5.0 candidate). DSH package is now5.0.0 over neutral4.1.0; persistent schema3 is current, role wire stays `methodology-dsh/2.0.0`, default4/scans/roles are unchanged. No merge, push, installation, profile repoint or sibling write occurred.

## Actual change set

- `skills/feature-dev/scripts/run_state.py` carries the reviewed schema3 lineage contract: one enrolled authority at `.methodology/lineages/<causal-id>/state.json`, spec admissions, immutable closed artifacts, editioned journal, pre-dispatch reservations, conservative recovery, retained retry episodes and a read-only `capabilities` command. `skills/feature-dev/scripts/continuation.py` (new,782 lines) owns lineage/reservation/historical-import mechanics without launching workers.
- CLI: `capabilities`, `init`, `show`, `record`, `continue`, `reserve`, `released`, `recover`, `episode`. `continue --predecessor TERMINAL --request PARENT_JSON` admits only a complete native-only DSH4.0/4.1 schema2 terminal or this contract's own closed schema3 terminal. No `--parent` wallet, no Codex/Claude ledger, no active schema2 migration.
- Population: 77 declared members (78 shipped with the map), seven helper modules, 27 skills, six roles; adapter unchanged at neutral4.1.0, 71 files, 28 capabilities, 7 parameters. `package.json`/plugin manifest/package-layout are5.0.0.
- Tests: new `tests/test_continuation.py`; `test_run_state.py`, `test_adoption.py` and `test_native_contract.py` adapted to schema3 counts/identity; none skipped. Current guide line and a continuation test-map section added.
- Current-release guidance in `README.md`, `references/{adoption,consumer-pm-profile,dsh-runtime,handoffs,source-disposition}.md`, `skills/feature-dev/SKILL.md` (full schema3 control section), `skills/pm/SKILL.md`, `skills/devplan-protocol/SKILL.md` and `skills/semantic-exoskeleton/SKILL.md`.

## Actual evidence

- Package suite on a complete Git-free source copy, exposed streams at private `package-suite-final.log`: `PYTHONDONTWRITEBYTECODE=1 python3.12 -m pytest -c implementations/dsh/pytest.ini implementations/dsh/tests -p no:cacheprovider -s -v --basetemp PRIVATE` → **199 passed, exit0**, zero skipped (73.98s). An earlier worktree run gave the same199 before the doc-only guide edits.
- Configured package Doxygen: exit0 with empty stdout/stderr; XML rebuilt but not tracked (279 function entries).
- Native parent proof, complete private receipts (`step1.json`, `native-proof.json`, both worker reports and markers):
  1. A real schema2 terminal was created by the accepted DSH4.1 compat shipped CLI (BLOCKED bootstrap) and hashed before import.
  2. The DSH5 CLI `continue` admitted it into schema3 (`phase architect`), left the original schema2 bytes identical, and enrolled the spec admission.
  3. Architect entry `d3a9a424…` was reserved (charge0), read back, and dispatched to a real DSH subagent worker (`01872701-…`); the worker observed the reserved entry and wrote `architect-marker.txt`. The parent released it with that actual session locator and recorded the canonical Architect SUCCESS.
  4. Accepting Architect precharged the causal Code entry: `debug_spent1/cap4`, entry `72bd04b1…` charge1. `reserve` persisted the reservation; a second real DSH subagent worker (`5c91ebfc-…`) observed `spent1`, `charge1`, `state reserved`, `worker null` and wrote a marker under the excluded `.methodology/` directory.
  5. The parent released that entry with the actual worker locator, recorded a canonical Code BLOCKED closure, and the lineage published one immutable closed artifact. Further `reserve` on the closed authority refuses exit2; the legacy schema2 bytes remain unchanged.
- One real refusal is retained in the same history: the first Architect record attempt was refused because the worker marker had changed the target candidate; the marker was moved out of the inventory, the same reserved entry was recorded, and the refused event remains in `history` rather than being erased.
- Not a finding: the earlier compat root selector `tests/test_dsh_package.py` still pins DSH4.0.0/75 and therefore fails until the accepted receipt updates it; this packet does not edit root tests or conceal that.

## Limits

Not merged, installed, repointed or advertised: both installed profiles still resolve the unchanged main symlink at4.0.0. No combined root/sibling regression, no Codex/Claude continuation parity and no product/Jeni execution occurred. The native proof covers one owned inert lineage and two owned workers; `reuse_code`, malformed-stream recovery and episode limits are covered by package tests, not by a second native dispatch campaign. The contract keeps its declared limits: one parent writer/storage domain, parent-authenticated consent, unknown-release hold, no exactly-once, cross-host or power-loss guarantee, and no scheduler.

Independent cumulative review of this exact candidate is pending. Root selector updates, combined sibling regressions, the separate concrete-result/integration and installation decisions remain outside this packet.

## Private evidence index

Ignored `.methodology/dsh-continuation/evidence/` in this worktree holds the suite log, Doxygen streams, native step receipts, worker reports and markers plus `SHA256SUMS`; `/private/tmp/dsh-cont-evidence/` is the live home. Public locators are logical; raw streams are not tracked artifacts.
