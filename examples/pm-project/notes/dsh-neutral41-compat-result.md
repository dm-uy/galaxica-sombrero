# DSH ordinary compatibility against neutral4.1 — reviewed candidate

The owner selected the bounded first packet from the [transfer brief](bounded-continuation-transfer-briefs.md#brief-for-the-dsh-agent): restore ordinary DSH operation against neutral4.1 and the four additive duties, without a continuation port. Data: branch `dsh/neutral41-compat`, worktree `/private/tmp/methodology-dsh-compat-20261104`, source baseline `a3ecb5c` (neutral4.1 plus the checked Codex5.0 candidate). DSH package is now4.1.0 over neutral4.1.0; wire `methodology-dsh/2.0.0`, schema2, default4, the eight named scans and all role payloads are unchanged. No merge, push, installation, profile repoint or sibling write occurred.

## Actual change set

The package diff carries14 files with23 insertions and23 deletions of release-identity literals; this result note and two doc-only relabels accompany them. No algorithm, payload, registry or membership change.

- Identity selectors: `implementations/dsh/package.json`, `.dsh-plugin/plugin.json`, `adapter.json` (`spec_version`), `references/package-layout.json`, `README.md`, and the `METHODOLOGY_VERSION`/package binding in `skills/semantic-exoskeleton/SKILL.md` now name4.1.0.
- Binding literals in `skills/feature-dev/scripts/run_state.py`: declared package version, neutral/adapter version equality and reported `neutral_version` now4.1.0. The `_bindings` algorithm and its75/76,71,28,7 populations are untouched. Its contract line now names the enforced package4.1.0/neutral4.1.0 identities instead of the pre-existing stale2.4.0 text; no behavior changed.
- Current-release statements in `references/adoption.md`, `references/consumer-pm-profile.md`, `references/dsh-runtime.md`, `references/handoffs.md`, `references/source-disposition.md`, and the current-source line of `tests/test_guide.md`; the two surviving M30 checkpoint sentences were relabelled historical rather than current.
- `tests/test_native_contract.py` now asserts package4.1.0 and adapter `spec_version`4.1.0.

The four additive neutral duties (`PREFLIGHT-204`, `PLAN-405`, `TST-1003`, `LIFE-108`) arrive through the existing `adapter.json` file bindings; no new file, member, capability or skill was added, so declared membership stays75 (76 shipped) and the adapter stays71 files/28 capabilities/7 parameters. The DSH-side duty owners already require the full current neutral body and need no reduced restatement.

## Actual evidence

- Package suite, exposed streams at private `package-suite.log`, run in the worktree:
  `PYTHONDONTWRITEBYTECODE=1 python3.12 -m pytest -c implementations/dsh/pytest.ini implementations/dsh/tests -p no:cacheprovider -s -v --basetemp PRIVATE` → **146 passed, exit0**, zero skipped (50.21s). A full-source Git-free copy after the doc correction reproduced **146 passed, exit0**, zero skipped (49.32s, `gitfree-suite-final.log`). Adoption fixtures copy the package and all adapter-referenced neutral owners into a Git-free combined source.
- Ordinary shipped-CLI probe `ordinary_probe.py`, complete receipt at private `ordinary-proof-01.json`: on a fresh private Git-free minimal binding source (package, all adapter-referenced neutral owners, `SPEC_VERSION`; no `.git`) and a real Git target, actual `init` exit0, `show` exit0, accepted `record` exit0 moving `bootstrap`→`architect`, `show` exit0. The initialised bindings report package4.1.0, neutral4.1.0, 76 package rows and71 neutral rows. A duplicate-key control result is refused exit2 with empty stdout; the same-run refused diagnostic is retained while phase `architect` and `debug_spent` stay unchanged. The same probe on a second Git-free full-source tree reproduced every field. This is an ordinary route, not a continuation or native-parent proof.
- Configured package Doxygen: exit0 with empty stdout/stderr, XML rebuilt but not tracked (also reproduced after the doc correction).
- Root `tests/test_dsh_package.py` reports **2 failures, not skipped**: its shared release selector still pins DSH layout/plugin version4.0.0. Because baseline assembly raises, the module's17 refusal controls currently pass vacuously; after the two pins are updated, that module must be re-run and each refusal re-confirmed on its own cause. This is the known root-consumer update that follows an accepted sibling receipt; the DSH packet does not edit root tests or conceal the failure.

## Independent review and doc-only correction — 2026-11-04

A distinct fresh-context reviewer inspected commit `1178220` read-only and independently reran the full package suite on its own basetemp (**146 passed, 51.09s**), its own redirected probe (all summary fields matched), discriminating layout/neutral version refusals, Doxygen on a private copy, and `bin/conform adapter implementations/dsh/adapter.json` (**exit0, 76 pass**). Verdict: **PASS WITH LIMITS** — release-identity-only packet on a working package, no blocking defect.

Five minor findings were closed as doc/receipt corrections, with no behavior or payload change: the two stale "current M30 binding" sentences are now labelled historical; the helper's contract line names4.1.0; the change-set wording distinguishes the14 package files from this note; the probe source is described as a minimal binding source; and the root selector's vacuous-control consequence is disclosed above. The package suite, Git-free suite, probe and Doxygen were re-run after those edits. The reviewer's limits stand: no full root/sibling/combined regression, no loader/installation or native-dispatch verification, and no independent proof that the four duties are new in neutral4.1 versus4.0 (only presence, binding and reachability).

## Limits and next boundary

Not merged, installed, repointed or advertised: the web profile still resolves the unchanged main symlink at4.0.0, and this source change alone is not installation. No native parent/worker dispatch, no continuation capability (`capabilities/continue/reserve/...`), no Claude/Codex change, no combined root regression and no full-flow acceptance is claimed. The historical `tests/test_guide.md` RECON-DEC line that names DSH4.0.0 is retained as history, not rewritten.

The root selector update on the combined source, combined sibling regressions and the separate concrete-result/integration decision remain outside this packet. Packet B (continuation parity) needs its own matching authority.

## Private evidence index

Ignored `.methodology/dsh-neutral41-compat/evidence/` in this worktree holds `package-suite.log`, `gitfree-suite-final.log`, `ordinary-proof-01.json`, `ordinary-proof-01.summary.log`, `ordinary_probe.py`, both Doxygen streams and `SHA256SUMS`; `/private/tmp/dsh-compat-evidence/` is the same live home. Public locators are logical; the streams are not tracked artifacts.
