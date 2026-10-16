# Evaluation — distinct evaluator (verbatim)

Actor: fresh Claude Code subagent (general-purpose, model opus requested), session-local id a4a92d4e17838c66f, authored none of the proposals; dispatched 2026-10-16 by the root only after both HOLD files were saved and hashed. Its recommendation confers no authority; the owner decides at the specification gate.

---

## Hash check
`shasum -a 256` (all match the dispatch):
- brief.md 01838020ce941442ccc6660c820b578c903dd63660aa7fef3ad4fa92ef0d71c7
- hold-generator-a.md 25cdfb784d42e979ea4e188860abc707e5f74b1df005a23bc9e97e45b7cdbde8
- hold-generator-b.md 269976cffafe26da8b1e3fcb912f28bac6f120d3b86644ff240d19ded40e58e6

I wrote nothing. Worktree at start: 28 ` M` plus the untracked decision dir. During my run `CHANGELOG.md` became modified and `examples/pm-project/notes/m37-claude-parity.md` appeared untracked; neither is mine (another writer). Not reverted.

## Merged population
- **M1 = A.A + B.ALT-2** Byte-locked Claude mirror of 4 helpers + 13 seeds (B: also the 4 Codex tests), root SHA parity oracle, Codex canonical, Claude `bin/` launchers.
- **M2 = B.ALT-1** Adapted independent Claude copy; sync by policy only.
- **M3 = A.B** Claude-native fork: cwd default, `--hook session-start` second SessionStart entry, legacy 1.4.0 assessment, bare names.
- **M4 = A.C** Helper code moved to neutral root `tools/consumer_pm/` + root `bin/`; Codex scripts become shims; seeds mirrored.
- **M5 = A.D + B.ALT-4** Third typed sibling `implementations/consumer-pm/`; Codex 73→~52 members.
- **M6 = A.E + B.ALT-3** No code port: Claude thin delta carrier + routing referencing `${CLAUDE_PLUGIN_ROOT}/../codex/skills/pm/{scripts,templates}`; SHA tripwire on the 17 Codex files. B variant adds `bin/` launchers that BLOCK (exit 2) if the Codex file is missing; A variant retires bare names and offers a grant-gated per-project `.claude/settings.json` SessionStart hook at adoption.
- **M7 = B.ALT-5** Vendor helpers into each consumer + project hook, per-project grants.
- **M8 = B.ALT-6** External bridge plugin (bin + hook) dispatching to the checkout via `METHODOLOGY_ROOT`; repo side as M6 without `bin/`.
- **H (hybrid of evaluated mechanisms)** = M6 with B's launchers + tripwire, plus A.E's adoption-time project SessionStart hook, separately granted per project.

## Fact verification
1. **C2 orient cannot assess the five today — VERIFIED.**
   - `consumer_files.py:384-397`: profile must equal `methodology-consumer-pm/1.0.0` (`:67`). Otherwise AGENTS.md containing "Project Conventions 1.4.0" yields a legacy Layout. Anything else hits `fail(...,'undeclared-or-unsupported-profile')`.
   - Projects: no CONVENTIONS has a `profile:` key. Versions: consumer-A 1.0.0, consumer-B 1.4.0, consumer-C 1.0.0, consumer-D 1.3.0, consumer-E 1.1.0.
   - consumer-B is legacy: `orient.py:199-200`, then all 22 rows UNAVAILABLE (`:301-302`), exit 2. The other four raise ConsumerInputError, giving "orient: unavailable", exit 2 (`:505-508`).
   - Bare no-argument `orient` is refused by `orient.py:569`.
   - Generator A's assumption "all five declare 1.4.0" is **REFUTED**. B's F2 is verified.
   - Also verified:
     - The three CLAUDE.md "plugin injects" lines (<owner-org>, consumer-C, consumer-D).
     - <owner-org> `CLAUDE.md:42` calls the old orient by absolute path.
     - consumer-D `AGENTS.md:38` uses `codemap <project> <file or symbol>`.
   - Extra: `codemap.py` never calls `resolve_layout`, but map answers need `.methodology/maps/current.json` (`:149`). None of the five has one, so only the attributed "source fallback" path is available (code read, not executed). Whether each legacy Doxyfile parses under C2 `parse_doxyfile` is unverified.
2. **Single-SessionStart and AST pins — VERIFIED** (in the dirty 2.0.2 tree).
   - `test_session_start.py:586-588`: one entry, one hook.
   - `test_package_contract.py:286`: `len(start) == 1`.
   - `test_guard.py:1612,1617`: hook keys exactly {PreToolUse, SessionStart}.
   - `tests/test_c1_review_and_routing.py:414-441`: whole-AST SHA `4ee9d7d1…`; only `PACKAGE_VERSION` "2.0.2" normalizes.
3. **Oracle refusals — VERIFIED.**
   - `test_claude_package.py`:
     - `:59` `DECLARED_PACKAGES={"codex","claude"}`
     - `:125-128` symlinked package and unknown sibling refused
     - `:156-157,167` linked or uncontained members refused
     - `:215` the sibling set is exact
   - `test_codex_package.py:46,78-80` does the same.
   - Codex `run_state.py:445` hard-codes `== 73`. `test_c1:199-204` requires that exact site ("exact C2 member site mismatch").
   - Claude `run_state` takes its count from the layout and has no literal.
4. **FORMAT admits a non-harness typed member — UNVERIFIABLE (ambiguous, leaning against).**
   - FMT-1 exempts "the typed implementation-package namespace" and is silent on harness-ness.
   - FMT-26/27 and `runtime/adapters.md:109` ("A declared package under `implementations/` owns its adapter…", and an adapter holds `harness`) frame every package as a harness package.
   - So M5 needs an owner interpretation. Neutral bodies may not change.
5. **Harness strings and template lookup — VERIFIED.**
   - No "codex" string in the 4 helpers or 13 seeds. "CLAUDE" appears only as the consumer's `CLAUDE.md` file (`orient.py:205,305`).
   - `orient.py:53` imports its sibling `consumer_files`.
   - `markup_migrate.py:445` locates the template at `Path(__file__).parent.parent/'templates/Doxyfile'`, with no package-identity binding.
   - The carrier, by contrast, names Codex (`consumer-pm-profile.md:3`, "Wire methodology-codex/2.0.0"). Lines 15/25 exclude hook/PATH registration ("no old --all/--hook/PATH/installed-source fallback").
   - The drift precedent is verified: `visual_gate_lint.py` differs between the packages (`cmp` differs at line 3).
6. **In-place `bin/` on PATH — UNVERIFIABLE from files.**
   - The Claude package has no `bin/` today.
   - The only plugin `bin/` on PATH is `<owner-agent-skills-checkout>/plugins/product-methodology/bin`. That is the directory-marketplace source of a plugin whose `installPath` is the cache. This is the marketplace case, not `CLAUDE_CODE_PLUGIN_DIRS`.
   - `CLAUDE_PLUGIN_ROOT` is unset in Bash (verified).
   - The old plugin's README cites docs for enabled plugins generally.
   - A one-session probe is required.

## Scores
Criteria (brief): C1 single source 0.25; C2 compatibility 0.25; C3 consumer continuity 0.20; C4 cost (higher score = cheaper) 0.15; C5 reversibility and extensibility 0.15. F = feasibility, I = impact (10 best), R = risk (10 = riskiest).

| Cand | C1 | C2 | C3 | C4 | C5 | **Total** | F | I | R |
|---|---|---|---|---|---|---|---|---|---|
| M1 mirror+oracle | 7 | 8 | 3 | 5 | 6 | **6.00** | 7 | 6 | 4 |
| M2 adapted copy | 3 | 8 | 3 | 5 | 4 | **4.70** | 8 | 5 | 6 |
| M3 native fork | 2 | 3 | 6 | 3 | 3 | **3.35** | 4 | 6 | 8 |
| M4 neutral-root tool | 7 | 4 | 3 | 3 | 6 | **4.70** | 4 | 6 | 7 |
| M5 third package | 10 | 2 | 3 | 2 | 5 | **4.65** | 3 | 7 | 8 |
| M6 reference Codex | 9 | 7 | 4 | 9 | 7 | **7.20** | 9 | 6 | 3 |
| M7 vendor to consumers | 5 | 7 | 6 | 4 | 6 | **5.70** | 5 | 6 | 6 |
| M8 external bridge | 9 | 6 | 7 | 7 | 6 | **7.10** | 6 | 7 | 5 |
| **H** M6 + project hook | 9 | 7 | 5 | 8 | 7 | **7.25** | 8 | 7 | 3 |

Reasons:
- **M1:**
  - Equality is enforced by hash, but two paths per file.
  - Codex is untouched. Membership edits travel together, as the constraint allows.
  - Fixtures say `codex:test` inside Claude.
  - Every Codex fix becomes a coupled two-place edit.
  - Rollback is a revert. It converts to M5 mechanically.
- **M2:** about 2450 duplicated lines with no check. F5 shows drift happens. Maintenance is the highest of the copy options.
- **M3:**
  - Amending the single-hook assertions is not a membership change, so it violates "preserve existing assertions".
  - It departs from the C2 contract ("no --hook"; C3 hooks not shipped).
  - The legacy reader covers only 1.4.0 (one project) and needs its own spec and QA.
- **M4:**
  - Changes accepted C2 files (shims, a parameterized template path in `markup_migrate`).
  - Codex QA must be repeated.
  - Package-profile code lands at the neutral root (REPO-102 spirit).
  - Seeds stay duplicated.
- **M5:**
  - The best structure, but it breaks the Codex `== 73` literal and the test_c1 selector.
  - `DECLARED_PACKAGES` changes in both oracles.
  - FORMAT is ambiguous (fact 4).
  - Rollback spans packages, and the tie-breaker penalizes it.
- **M6:**
  - One copy and roughly +1 to +5 Claude members. Codex untouched.
  - The complete checkout always contains `codex/`, because the oracle pins the sibling set.
  - Negatives:
    - first runtime cross-package dependency;
    - the SessionStart binding cannot check the sibling (its AST is pinned), so the launchers BLOCK at call time;
    - Claude users read Codex-worded owner text through a Claude delta.
  - The tripwire forces review on any upstream change.
  - Revert is trivial, and promotion to M5 stays possible later.
- **M7:**
  - Five copies plus a new stale-copy check, which is new orient behaviour.
  - Vendored code falls under consumer Doxyfile coverage and CHECK-15.
  - Needs two grants per project.
- **M8:**
  - Continuity rests on the only observed PATH mechanism (fact 6), and no pins change.
  - But exposure lives outside this repo's QA and oracles, needs an owner-level env setting, keeps an in-house plugin alive against the goal, and invites a "fallback to installed copy" reading.
- **H:** M6 plus the grant-gated project hook. It restores session-start orientation after adoption without touching package pins or relying on in-place PATH. The hook needs a separate explicit grant per project, consistent with profile line 15. Cost rises slightly (a bootstrap step and test).

Uncertainty is about ±0.5 per total, and these are reasoned judgments, not measurements. H, M6 and M8 sit inside one band. Unknowns:
- **U1:** whether an in-place `bin/` reaches PATH.
- **U3:** how a project-level hook locates the checkout. A tracked absolute home path is a portability and privacy problem; prefer `settings.local.json` or an env var.
- Whether legacy Doxyfiles parse.

The tie-breaker (Codex risk) does not separate H, M6 and M8, since all leave Codex untouched. I separate them by verifiability inside this repository's QA and by the goal of retiring in-house plugins, which favours H/M6 over M8.

## Recommendation
**H**, with M6 as its mandatory core:
- the thin Claude carrier;
- routing in pm and the four lifecycle skills;
- three regular-file `bin/` launchers (kind `helper`) that exec the real Codex files and return exit 2 BLOCKED if they are missing;
- a root tripwire test pinning the SHA-256 of the 17 Codex files;
- layout, independent oracle and contract counts updated together.

The adoption-time project SessionStart hook is a separable, per-project, explicitly granted step. If the owner declines it, plain M6 remains.

Cost and reversibility:
- Lowest file and QA cost of all candidates. Codex QA is not repeated.
- Revert is a single PR.
- Maintenance: each Codex change trips the tripwire and gets a one-line review.

The spec must include the U1 probe before bare names are promised. Explicit `python3 -B …/codex/skills/pm/scripts/<cmd>.py PROJECT` stays the guaranteed form.

The runner-up, if a self-contained Claude package is preferred, is M1.

## Reopen conditions
- The U1 probe shows an in-place `bin/` is not on PATH. M8, or project hooks with explicit paths, gain C3, so re-score.
- The owner rules that a package must not depend at runtime on a sibling harness package. Choose M1.
- An approved third harness, or a need to version the helpers independently. Move to M5, after an owner reading of FMT-26 and `runtime/adapters.md:109`.
- The tripwire fires often, meaning C2 helpers churn. Reconsider M1 or M5.
- The owner authorizes amending the single-SessionStart pins. A package-level hook becomes admissible.
- The owner wants continuity before adoption. Only a separately specified legacy reader (M3-like) or keeping the old plugins enabled meets it.

## Consumer-continuity finding
No candidate restores bare `orient` assessment for any of the five projects without a per-project adoption grant:
- C2 accepts only `methodology-consumer-pm/1.0.0`.
- 1.4.0 (consumer-B) is read-only legacy with all 22 rows UNAVAILABLE.
- 1.0.0, 1.1.0 and 1.3.0 (the other four) are refused outright.
- Bare no-argument `orient`, as written in four AGENTS.md files, is refused by design.

M3's legacy reader would reach one project at most, as unspecified new behaviour. M8 runs the same C2 helpers, so it does not help either.

`codemap PROJECT TARGET` is the only command usable before adoption, in attributed source-fallback mode. That is subject to the unverified Doxyfile parse and to U1 for the bare name.

Implications for the spec:
- Retiring `product-methodology` and `prompting-methodology` cannot be a single switch. Each project needs a sequenced, owner-granted pm-bootstrap migration: CONVENTIONS profile, AGENTS.md `orient .` or the explicit form, and the three false "plugin injects" CLAUDE.md lines (<owner-org>'s absolute-path call too).
- The old plugins should stay enabled for each project until its migration is accepted, or the owner explicitly accepts the gap.

## Files read
- `/private/tmp/methodology-m37-claude-parity/examples/pm-project/notes/m37-decision-c2-port/{brief,hold-generator-a,hold-generator-b}.md` (full)
- `/private/tmp/methodology-m37-claude-parity/prompting/brainstorm.md` (lines 9-82); `prompting/verification.md` (rule index)
- `/private/tmp/methodology-m37-claude-parity/FORMAT.md` (FMT-1, FMT-26..37); `runtime/adapters.md` (grep 109-111); `README.md` (grep); `tools/conformlib/markdown.py` (grep)
- `/private/tmp/methodology-m37-claude-parity/implementations/codex/`:
  - `skills/pm/scripts/{consumer_files,orient,codemap,markup_migrate}.py` (targeted sections)
  - `references/{consumer-pm-profile.md,package-layout.json}`
  - `README.md:99`
  - `tests/test_{consumer_pm,codemap,consumer_files,markup_migrate}.py` (grep)
  - `skills/feature-dev/scripts/run_state.py` (grep)
  - `skills/devplan-protocol/scripts/visual_gate_lint.py` (diff)
- `/private/tmp/methodology-m37-claude-parity/implementations/claude/`:
  - `references/package-layout.json`
  - `skills/feature-dev/scripts/run_state.py` (grep)
  - `tests/{test_session_start,test_package_contract,test_guard}.py` (grep)
  - README and references (grep)
- `/private/tmp/methodology-m37-claude-parity/tests/{test_claude_package,test_codex_package,test_c1_review_and_routing,test_skeleton,test_cli}.py` (targeted)
- `<five-consumer-projects>/{AGENTS,CLAUDE,CONVENTIONS}.md` (front matter and grep, read-only); existence checks for Doxyfile and `.methodology/maps/current.json`
- `<owner-agent-skills-checkout>/plugins/product-methodology/{hooks/hooks.json,bin/codemap,README.md}`
- `<home>/.claude/settings.json` (grep); `<home>/.claude/plugins/{installed_plugins,known_marketplaces}.json` (read); session `$PATH`
