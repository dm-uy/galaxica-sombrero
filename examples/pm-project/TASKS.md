# Current maintainer tasks

## CONT-BOUND — bounded continuation and earlier verification

Owner request, 2026-11-03: «Давай подготовим спецификацию доработок методологии: А и Б — одним ограниченным изменением, В–Д — уточнениями существующих правил. Сначала проведи необходимый recon, без реализации.» Preparation only. The later owner clarification selects Codex executable work and explanatory transfer instructions for separate Claude/DSH agents; it does not authorize implementation, consumer repair, main merge, push or installation.

| Task | State | Finish / next action |
|---|---|---|
| CONT-BOUND-T1 — source/data/decision reconnaissance | Complete locally | [RECON](notes/RECON_2026-11-03_bounded-continuation.md), independent source lanes and fresh completeness check; all four findings reconciled and bounded delta verified. Source unchanged. |
| CONT-BOUND-T2 — resolve spec-affecting questions and draft specification | Complete; owner approved2026-11-04 | ONE authorized Q-REPRESENTATION/Q-ROLLOUT packet, preserved originals/HOLD/evaluation and root A choice; [approved specification](specs/bounded-continuation.md) passed original independent document review. Later authentic approval and lighter procedure supersede its preparation-only stage; implementation/result is recorded below. |

### Implementation approval — 2026-11-04

Owner approved the exact specification and then the lighter procedure: short plan, root Codex implementation, checks and one independent review. Merge/installation remain separate; sibling code belongs to other agents. Earlier pending statements above are historical preparation receipts.

| Task | State | Finish / next action |
|---|---|---|
| CONT-BOUND-T3 — Codex candidate | Checked locally | [Result](notes/bounded-continuation-result.md): schema3/helper/callers/rules, full Codex200 passed, root614+2 known held/baseline failures, maps and real CLI/native proofs. |
| CONT-BOUND-T4 — independent review and owner result | Review complete; owner result pending | Same reviewer closed F1–F6; [final judgment](notes/bounded-continuation-review-final.md). Shared rollout/merge/install held for exact external compatibility and combined validation; no overall acceptance claimed. |

### Claude ordinary compatibility — 2026-11-04

Owner: «надо доработать наш плагин с методологией», pointing at the transfer briefs, then «Сначала совместимость». Ordinary compatibility only, on a lighter procedure with one independent reviewer. Merge, push and installation remain separate.

| Task | State | Finish / next action |
|---|---|---|
| CONT-BOUND-T5 — Claude 3.1.0 ordinary compatibility | Checked locally; owner result pending | [Result](notes/bounded-continuation-claude-compat.md) on `claude/cont-bound-compat`: Claude 548, root 616 and Codex 201 passed; live native session and real helper route observed; review findings dispositioned, with the notes left open stated in the result. |
| CONT-BOUND-T6 — DSH ordinary compatibility | Not started; needs a separately assigned DSH agent | Its package suite fails 83 of 146 on the version pin. Blocks shared integration. |
| CONT-BOUND-T7 — findings outside the Claude package | Open | Stale Codex stamps corrected and guarded at the owner's word on 2026-11-04. Still open: Codex carrier wording, the missing `continuation.py` disposition row and the smoke specification's admissions path; the same stamp guard for DSH; neutral homes for the ledger rule and for counting a successor's Code repair; stranding of in-flight runs by in-place releases. [Details](notes/bounded-continuation-claude-compat.md#findings-for-other-owners). |
| CONT-BOUND-T8 — continuation port to Claude | Not selected | Separate owner decision; the motivating Jeni ledger is Codex's, so this port would not serve it. |

## RECON-DEC — reviewed RECON forks and owner-authorized brainstorm

Owner request, 2026-11-03: prepare a specification for explicit forks in RECON, independent completeness verification, and owner agreement before launching brainstorm so downstream project specifications contain worked-through decisions. Initial grant: preparation only. On 2026-11-03 the owner approved removing the full feature-dev procedure and implementing the bounded change with affected checks, independent review and a small behavioral probe. Merge, push and installation remain separate.

| Task | State | Finish / next action |
|---|---|---|
| RECON-DEC-T1 — measured reconnaissance and specification | Complete locally | [Draft specification](specs/spec-recon-decision-checkpoint.md) and [RECON / verification](notes/RECON_2026-11-03_spec-recon-decision-checkpoint.md); independent document review found no blockers, bounded document/adapter checks pass. |
| RECON-DEC-T2 — owner specification decision | Approved with lighter procedure | Exact owner quote is retained in the specification metadata; no full feature-dev run. |
| RECON-DEC-T3 — targeted implementation | Checked locally | [Changes, affected checks, independent review and bounded native probe](notes/spec-recon-decision-checkpoint-result.md); no full feature-dev flow. |
| RECON-DEC-T4 — local main integration and installed updates | Complete locally | Owner grant executed: canonical main integrated; Codex4.0.0, Claude3.0.0, DSH4.0.0 updated and bounded load/integrity checks pass. [Receipt / desktop runtime limit](notes/spec-recon-decision-checkpoint-result.md#accepted-merge-and-installed-updates--2026-11-03). Later owner-authorized [remote main delivery](notes/spec-recon-decision-checkpoint-result.md#remote-main-delivery--2026-11-03) completed. |

## PM-INVOKE — model-invocable lifecycle commands (Claude 2.4.0, branch in review)

Owner request, 2026-10-28, in the interview workspace session: «Так не годится. Надо сделать так, чтобы ты мог запускать сам автономно эти вещи. Это запрещено на уровне плагина, потому что плагин-то, собственно говоря, наш, и мы можем внести в него изменения для твоей имплементации, если он тебя блокирует.» Scope: the five Claude `pm-*` lifecycle skills become model-invocable while their consent semantics stay as they are; Codex is unchanged.

| Task | State | Finish / next action |
|---|---|---|
| PM-INVOKE-T1 — skills, runtime, test, version | Done on branch `claude/pm-model-invocation`, review corrections applied | Flags removed, consent sentence in each command, runtime sections 4 and 5, contract test inverted, package 2.4.0, CHANGELOG. Independent Review (Opus) of `7859d1a` requested changes: five blockers and remarks, corrected in the follow-up commit (root README identity, restored M38 history line, RUNREV-101 request for `pm-review-run`, M37-T9 row, live-probe status). Suites on Python 3.12 in a Git-free copy are recorded in each commit message. |
| PM-INVOKE-T3 — live probe | Unverified | No live Claude Code session loaded the candidate: a child session would load the settings' in-place plugin of the same name beside it. The first fresh session after the merge is the probe: the root's Skill call to `methodology-claude:pm-run-batch` on an approved packet; `pm-run-batch` refusing a packet without a recorded batch decision; `pm-review-run`, invoked by the model with no recorded request, asking instead of reading transcripts; and the Russian trigger overlaps (`pm-handoff` against `durable-layer` on «зафиксируй состояние», `pm-review-run` against `analyzer` on «разбери прогон») showing which skill fires. A failure returns to this task. |
| PM-INVOKE-T2 — merge and in-place update | Merged locally into `main` by fast-forward; not pushed | Owner decision 2026-10-28T17:20:41Z through a structured question (AskUserQuestion), answer «Слить в main локально (Recommended)». It covers a fast-forward of this branch into the canonical checkout's `main` without push, plus the consumer workspace's instruction and memory update. The in-place plugin reads `main`, so a fresh Claude session loads 2.4.0. Push or PR need the owner's word. |

## BF-SOURCE — brownfield source-obligation correspondence (PR19 merged and installed)

Owner-selected correction, 2026-10-27: remove the account name from current text while retaining history; introduce SP-205 with MINOR. [Scope, earlier failed rationale and corrections](notes/brownfield-source-correspondence.md).

| Task | State | Finish / next action |
|---|---|---|
| BF-SOURCE-T1 — existing-receipt correspondence | Superseded by T3 | Initial patch candidate and review missed source-transfer authority, semver and receipt/example issues; history retained. |
| BF-SOURCE-T2 — initial validation and delivery | Historical; not revised-candidate proof | Original suites passed and draft PR19 was delivered at997adbf; owner review returned it for correction. |
| BF-SOURCE-T3 — owner-selected norm and review corrections | Accepted; PR19 merged | All13 items have dispositions; SP-205/MINOR, dedicated field, traceable exclusions, form/example, source identities and records corrected. Full suites plus bounded strengthened-test follow-up and independent re-review pass. History preserved; corrected result accepted and PR19 merged at17574b8. |
| BF-SOURCE-T4 — accepted merge and installed-version update | Complete | Explicit owner grant fulfilled: Codex/DSH3.2.0, Claude2.3.0. Fresh Codex discovery/integrity, Claude binding and DSH web probes pass; desktop runtime discovery remains unverified. [Receipt](notes/brownfield-source-correspondence.md#merge-and-installed-version-update--2026-10-27). |


## QA-REFLECT — QA boundaries and critical reflection (PR17 merged and installed)

[Owner scope, critique and validation](notes/qa-reflection-clarification.md). Documentation clarification on an isolated branch; no new software flow, status or helper.

| Task | State | Finish / next action |
|---|---|---|
| QA-REFLECT-T1 — neutral wording and native carriers | Done; PR17 merged | Strict QA gate, scenario effects, prerequisite refusal, bounded reflection and honest reuse; original guarantees retained. |
| QA-REFLECT-T2 — consistency and independent review | Done; PR17 merged | Initial failures and corrections retained; bounded root/native/adapter checks and independent document review completed. Checked source f72798d delivered to origin branch; owner-directed gh account switch resolved API access. PR17 subsequently merged under explicit owner grant; installed activation is recorded below. |
| QA-REFLECT-T3 — owner-supplied PR17 review corrections | Done; PR17 merged | Five current-version comment lines, historical provenance, one current HANDOFF and neutral-owner QA references; bounded contracts/maps/adapters and independent rereview pass. Owner granted merge/install; completed at a321003 with the bounded checks below. |

## GRACE-Q2 — minimal QA evidence package (integrated and delivered)

[Owner grant, scope and checks](notes/grace-qa-evidence-minimal.md). Documentation clarification, neutral first then Codex/Claude/DSH; no new roles, experiments or contract/test reduction.

| Task | State | Finish / next action |
|---|---|---|
| GRACE-Q2-T1 — neutral clarification and carrier sync | Done; main/origin | Existing QA evidence view, LDD outcome correlation and agent-operable test guide; preserve all required guarantees. |
| GRACE-Q2-T2 — bounded checks and project records | Done; main/origin | Wording, patch bindings and preserved interfaces checked; independent document review clear after history-comment correction. Owner approved integration/origin delivery; package448e575 was pushed and remotely confirmed. Working-profile installation withheld. |

PR17 follow-up at reviewed snapshot dc25ea4: two independent reviews confirm substantive correctness and full-suite green results; five annotation lines, record provenance/HANDOFF and duplicate QA summary are corrected. Bounded follow-up verification completed; [evidence and disposition](notes/qa-reflection-clarification.md#pr17-independent-review-follow-up). PR17 merged at a321003; Codex3.1.0 is enabled with fresh27-skill discovery, Claude2.2.0 binds to neutral3.1.0, and both registered DSH profiles resolve3.1.0. Web composition passes; desktop CLI composition is host-refused and fresh desktop discovery remains unverified. [Installation receipt](notes/qa-reflection-clarification.md#merge-and-installation-2026-10-21).

## M38 — DSH native implementation package (merged through PR10)

Owner request: implement the methodology for the DeepSeek Harness under `implementations/`, reconcile it against current source and connect it as a DSH plugin. Scope, evidence and limits: [result note](notes/m38-dsh-package.md). Because this adds a shipped public package and not only documentation, the change keeps the software flow's separation between an implementation artifact and the owner's matching concrete-result decision.

| Task | State | Finish / next action |
|---|---|---|
| M38-T1 — third typed package and DSH bundle | Done; merged through PR10 | Adapter, runtime, 27 skills, six roles, six helpers, bundle and a root contract test. Pre-rebase checks: `bin/conform adapter` and `bin/conform self` exit 0; package suite 146 passed; root DSH test 2 passed; sibling package tests 11 passed. A scratch-profile `dsh plugin add` proved the layer and the resolved skill root. |
| M38-T2 — `main` merge and live installation | Done | Owner approved both. The first local fast-forward of `af7eab7` never reached `origin/main` and is superseded by M38-T5. `dsh plugin --profile web add ./implementations/dsh` installed the bundle from the canonical checkout. Composed layer and 27-entry skill root verified with `--dump-config`. Previous profile files saved as `.bak-m38`. A packaged release stays separate and untaken. |
| M38-T3 — first real run, probe 1 | Done on the live profile | The bundle is installed in the `desktop` profile this GUI actually runs. All 27 methodology skills appeared in the running session and `pm` loaded with `Base directory for this skill: <checkout>/implementations/dsh/skills/pm`. Recorded correction: the first installation had gone to the `web` profile, which is why the plugin was absent after the owner's restart. |
| M38-T4 — smoke and a bounded real task | Probe 2 executed; full flow remains unproved | [Run evidence and limits](notes/m38-run-01.md). Bounded smoke executed on the granted disposable target; full Bootstrap-to-Finalize, checkpoint/resume and role isolation remain unproved. Probe 3 needs matching scope. |
| M38-T5 — rebase and merge | Done; merged through PR10 (merge `1ff633c`, 2026-10-19) | Rebased onto M37 merge `380dd00` under the owner's grant; HANDOFF/TASKS/C1 conflicts resolved with M37 records and Claude 2.1.0 assertions retained. Python 3.12 root 605/DSH 146 passed; adapter 76 passed; independent resolution verification and whitespace check passed. Private self scan not rerun without its deny list. [Delivery state](notes/m38-dsh-package.md#delivery-state). |

Records were synchronized after both merges at the owner's request on 2026-10-19.

## M37 — Claude package actualization (merged through PR11)

Owner scope of 2026-10-16 (structured answers retained verbatim in the [record](notes/m37-claude-parity.md)): patch the Claude package now; port the C2 consumer PM profile through specification → owner approval → feature-dev; keep the name `methodology-claude`; lift the M30 Claude deferral and run the live proof; keep the in-house plugins until orient is ported. Developed on an isolated branch from `b8696a2` with root as the only writer; merged into `origin/main` through PR11 (merge `380dd00`, 2026-10-17).

| Task | State | Finish / next action |
|---|---|---|
| M37-T1 — reconcile Claude with Codex, neutral owners and in-house plugins | Done | Two read-only lanes plus root re-check; findings in the record. |
| M37-T2 — patch Claude 2.0.2 | Done; merged through PR11 | Carrier parity (prompting route, RUNREV-301, lifecycle owner sets), install-claim correction, M31 root-oracle regression repair. Superseded by 2.1.0 in the same delivery. |
| M37-T3 — live Claude M30 AC4/Claude AC5 | Observed | Three fresh headless runs on candidate 2.0.2: important case ran two generators → persisted HOLD → distinct evaluator → DEC; trivial and settled controls stayed bounded. M30 renewed QA/Review/Finalize still owed. |
| M37-T4 — C2-port decision packet | Collapsed to H by the owner's specification approval | Two generators, persisted HOLD, distinct evaluator ([packet](notes/m37-decision-c2-port/README.md)); recommendation H, runner-up M1; U1 verified after evaluation. |
| M37-T5 — C2-port specification | Approved 2026-10-16 | Owner: «Да, утверждаем H.» — collapses the decision packet to H and authorizes the feature-dev run; recorded in the [specification](specs/m37-claude-consumer-profile.md) front matter. The owner also asked to deliver the result to the public repository through a PR afterwards, with no owner-local references. |
| M37-T6 — feature-dev run for the C2 port | Result accepted by the owner; PR11 merged into origin/main | Run `m37-c2-20261016` ended BLOCKED at Finalize on one owner decision (AC5 literal bare call); Debug 1/4 fixed three Review defects; renewed QA and Review SUCCESS. Owner: «Принять» (AC5 met by the absolute-path launcher call, probe deviations accepted), «Push + PR, слияние после вас», «Да» to the `.methodology/` ignore rule. [Record](notes/m37-claude-parity.md). |
| M37-T7 — consumer migrations and plugin retirement | Plugins disabled 2026-10-19; migrations await per-project grants | The owner disabled `product-methodology` and `prompting-methodology` at user scope ahead of the migrations ([record](notes/m37-claude-parity.md#in-house-plugin-retirement-2026-10-19)). Five consumer projects still migrate to `methodology-consumer-pm/1.0.0` one by one (CONVENTIONS profile, AGENTS orient line, CLAUDE.md lines that claim plugin injection); until then C2 `orient` is expected to refuse their current profile. |
| M37-T8 — sandbox check after the plugin retirement | Done 2026-10-19 | Six live probes in the Claude-only sandbox copy `011-claude-tasklight`: wiring, PM orientation, profile adoption, trivial brainstorm and a Russian contract request passed; a Russian fact-check request missed `prompting-verify`. Parity check listed seven losses. [Results](notes/m37-claude-parity.md#sandbox-check-after-the-retirement-2026-10-19). |
| M37-T9 — close the losses after the retirement | Russian triggers: PR15 awaits the owner's review; the rest awaits owner decisions | Port or drop `run_review.py` and `pm-ingest-candidates`; restore a typed brainstorm generator or not; extend the neutral quotation rule (research-wide ellipsis ban, verifier's exact-string step) or not. Russian triggers: PR15 leads the 23 model-invoked skill descriptions with Russian labels and phrases; live probes fired every Russian request ([record](notes/m37-claude-parity.md#follow-up)). Loss 6 (owner-only `pm-*` commands) is closed by [PM-INVOKE](#pm-invoke--model-invocable-lifecycle-commands-claude-240-branch-in-review) on branch `claude/pm-model-invocation`, pending the owner's merge decision. |

## M36 — canonical session handoff synchronization (completed)

Owner explicitly requested synchronizing Sombrero meta-documents and retaining important conclusions from this chat, history and real limitations. [Scope, provenance, carryover and delivery state](notes/m36-session-handoff.md). Documentation only; no framework code, installation, donor adoption or proof-deferral change.

| Task | State | Finish / next action |
|---|---|---|
| M36-T1 — current records and self-contained carryover | Integrated and pushed | Owner explicitly approved main integration/push. Checked source5ad7961 was fast-forwarded into canonical main and delivered; remote readback matched. This factual record closure follows under the same grant. Links, history preservation, source/fresh-reader review, whitespace and bounded conform checks passed; [receipt](notes/m36-session-handoff.md). |
| M36-T2 — choose the next bounded framework task | Awaiting owner-selected scope | In the next session read AGENTS and current records, then the M36 note. Resume a matching approved scope or ask only for the next genuinely missing scope; no automatic C3 Code, Claude retry or donor implementation. |

## M35 — new-machine Codex installation instructions (completed)

Owner reported that a fresh-machine agent did not infer personal plugin installation until prompted. Root prepared a bounded documentation correction in `codex/m35-install-docs`; [result and checks](notes/m35-install-docs.md). No new installer or package profile, live user configuration change or consumer onboarding.

| Task | State | Finish / next action |
|---|---|---|
| M35-T1 — explicit personal plugin entry | Integrated and pushed | README/AGENTS installation route, reproducible snapshot and native installation instructions independently exercised in an isolated temporary Codex profile. Owner-requested fast-forward merge and origin/main push completed; remote HEAD matched. Record closure follows under the same grant. |

## M34 — README presentation (completed)

Owner-requested reader-oriented README and diagrams; [result, review history and limits](notes/m34-readme.md). Root owns README/current records only; no installation or publication.

| Task | State | Finish / next action |
|---|---|---|
| M34-T1 — concise entry and diagrams | Checked locally | Purpose/quick start/document roles and two Mermaid diagrams; original Local use and responsibility boundaries retained. Relevant tests and local rendering pass. |
| M34-T2 — retain reviewed result | Complete locally | Owner “сливай” implemented: reviewed README3a6858b integrated into local main. Owner-requested canonical push completed and remote HEAD matched; closure receipt follows in the same delivery. No public release or installed update. |

## M33 — PM entry continuity (completed)

Owner-authorized template/bootstrap source update; [scope, actual routes and evidence](notes/m33-pm-entry.md). Root owns the isolated source/record amendment; no bulk consumer mutation, release or installation.

| Task | State | Finish / next action |
|---|---|---|
| M33-T1 — early entry duties and additive bootstrap | Checked locally | Both seeds/routes agree; five synthetic forward cases, source/preservation checks and independent review support the scoped amendment. Existing rules and actual homes retained. |
| M33-T2 — checked result and continuation | Local integration/install and canonical delivery complete | Owner “Сливай и устанавливай.” implemented at local main471c02f; Codex3.0.1 snapshot and Claude2.0.1 in-place checks retained. The later owner-authorized canonical direct push completed delivery; no consumer sweep. Historical receipts remain in the linked result. |

## M32 — incremental adoption of book-derived findings (retained results)

Owner-selected on 2026-10-15: retain all findings and progress step by step, checking and adopting useful results. [Authority, complete findings and acceptance policy](notes/m32-book-findings.md). This is bounded research/document work under M31; implementation, integration and activation keep their applicable boundaries.

| Task | State and dependency | Observable finish / next action |
|---|---|---|
| M32-T0 — retain findings and route | Accepted; integrated into local main | Findings and route saved; independent source/link/readback and whitespace checks pass. Source/readback/whitespace checks pass; final privacy results and retained earlier failures are in the note. Canonical record delivery is complete; separate prompting-source delivery remains limited. |
| M32-T1 — reconcile prompting carriers | Accepted; integrated into local source main | Candidate commit53b62f0, version0.6.0; independent review, structural checks and actual authoring proof complete. No target eval; local0.6.0 installation subsequently authorized and completed; source no-push rule retained. [Result](notes/m32-book-findings.md#current-result). |
| M32-T2 — verify document extraction | Checked locally; retained as optional | Recipe exercised on seven synthetic sources, simulated truncation/staleness and actual book ranges. No persistent parser or mandatory skill. [Result](notes/m32-book-findings.md#t2-and-t3--bounded-reading-checks). |
| M32-T3 — verify fresh-reader usefulness | Checked locally; retained within demonstrated scope | Fresh reader recovered current authority/holds, detected a synthetic contract contradiction and stale M31 wording; records corrected. No broad efficacy or full consumer trial. |
| M32-T4 — integrate accepted results | Local integration and canonical delivery complete | Owner “Разрешаю.” retained; source main53b62f0 and canonical records14191a0 integrated. Prompting0.6.0 installation completed in both clients. Later direct push completed canonical delivery without a PR; the separate prompting-source upstream/release remains undelivered. |

Historical M32 ownership: root was the sole writer of findings/recipe, TASKS, ROADMAP, HANDOFF and the narrow M31 note clarification in isolated `codex/m32-book-findings`. The present M36 custodian owns only its named record synchronization; the original M32 source grant is not reopened. The separately granted T1 source edits are committed in `codex/m32-prompting-carriers`; local source main now includes T1; book, workflow helpers/registries and VISION are unchanged; installed prompting copies were updated under the subsequent explicit grant. Stop on ownership conflict, unresolved consequential effects, scope expansion or a required failed/unavailable check. Inspect the actual candidate before deciding adoption; preserve negative findings and held work. The later explicit result decision authorizes the completed local merges; the subsequent explicit installation grant covers only the prompting update; remote release remains separate.

Retained older tasks below keep their original states and dispositions. M32 does not restart C3, waive M30 Claude proof or activate the broad deferred learning/measurement program.

## M28-C3 safeguards — terminal escalation

This retained C3 action is closed as an exhausted bounded run; no C3 Code continues here. Actual A3 state is ESCALATED/review at source candidatec5110484; prior spend2 plus A3spend2 exhaust Debug4/global4. Historical correction1 and every earlier failure remain retained. [Full result/history](notes/m28-c3-result.md), [specification](specs/m28-c3-safeguards.md), [approved plan](plans/m28-c3-safeguards.md).

Completed within the grant: exact46b7ccc private draft PR5 delivery; linked Bootstrap/Architect/Code diagnosis; counted Debug3 comment/control-provenance repair; QA1; Review1 CR finding; counted Debug4 blank-boundary repair; fresh full QA2; whole Review2. Current QA2 passed597/158/526, both private self checks and three adapters. Whole Review2 found the unresolved symlink-plus-parent protected-read bypass. Review SUCCESS, Finalize and result acceptance are not complete.

A3 source changes stay within guard_destructive.py/test_guard.py. The local branch contains unaccepted source2.3/77members/27skills/sevenhelpers/sixroles; at that C3 checkpoint main was accepted C2/source2.2; current main includes M30 source via PR6. C3 remains unmerged. Neutral1.1/wire2.0/schema2/Claude/root Local use are protected. Native AC7 is HELD/UNFULFILLED; no install/activation/main merge/publicity.

Next proposed activity needs a matching decision: read-only reconnaissance and a revised bounded safeguard specification, evaluating a smaller exact-recipe/structured-tool surface. No fifth repair, counter reset or silently relinked continuation. Retain the current source, raw evidence and limitations. Root-only five-record closure is verified separately from the judged319-file source.

## Accepted foundation

- M28-C2: implementation/current independent QA3/whole Review/assigned Finalize owner-accepted and integrated through PR4; [result](notes/m28-c2-result.md), [integration](notes/m28-c2-integration.md). Source2.2/73members/27skills/sixhelpers/sixroles; its597/146/526 and original cumulative4/4 history are distinct from C3.
- M28-C1: integrated through PR3; [result](notes/m28-c1-result.md). Required owners/native prompt routing and compatible neutral1.1/source2.1 bridge, unchanged wire/schema/algorithms.
- M27/M26: [coverage contract](specs/m27-self-contained-coverage.md) preparation and canonical onboarding integrated. Whole behavioral coverage remains owed; preparation repositories are archival.

## Route after an accepted minimal safeguard

Prepare a bounded single-stream Python API/database consumer trial. Then revisit separately scoped C4 SDK/import/candidate processing, C5 autonomous development/resume/isolation and C6 actual loader handover. Frontend/Telegram/MCP, installation/native activation and concurrent feature writers remain separate decisions. Repository visibility is already public; future releases are separately scoped. Lightweight error recording stays selected; systematic learning and comparative measurement remain deferred.

Preserve historical20evidence overwrites, qualified earlier Claude temporary-resource effects, host failure and foreign archival work. No blanket original-byte restoration or hard OS isolation claim.

## New owner observations — proposed follow-up only

These observations do not change C3's terminal escalation, approve a design, authorize Code/installation or activate deferred C5/C6 work.

### INTAKE-01 — actual task-ledger and entry-map adoption

The owner supplied a screenshot where an agent treated TASKS as optional and then added it. Canonical C2 PM/durable-layer already require the actual tasks home, with TASKS/AGENTS seeds and a document-home map. The installed1.0 PM/durable entrypoints omit TASKS. The screenshot's actual engine/version/project root is unknown; stale loading is a plausible explanation, not an established cause. Current orient's entry row does not verify actual AGENTS document links.

Status: proposed reconnaissance/acceptance follow-up. Done when a fresh consumer session proves which canonical source it loads, creates or locates the sole current task ledger, links actual key document homes from AGENTS, maintains task status/evidence and resumes from that ledger. Preserve established equivalent filenames; no duplicate register or automatic installation. Route this evidence into the existing onboarding/loader obligations.

### INTAKE-02 — independent exploration before consequential open decisions

The second screenshot requests independent subagent alternatives, superposition and scoring before important decisions. Canonical and installed brainstorm already provide proposal/hold/evaluation/collapse and reasoned scoring. The canonical protocol also permits one participant to perform phases sequentially; independently delegated generation/evaluation is not a universal mandatory trigger in the inspected brainstorm/PM entries.

Status: selected into the approved M30 contract below; this earlier observation is historical. M30 defines which consequential unresolved product/architecture choices require authorized independent generators and separate evaluation; retain alternatives before preference, explicit criteria/score reasons, actual decision authority and rejected/reopening reasons. Preserve settled decisions and routine delegated choices; disclose unavailable independence and respect host limits. Demonstrate actual role separation when required rather than declaring the presence of a skill sufficient. No brainstorm dispatch or methodology change is inferred from the screenshots alone.

## M30 — independent exploration contract (current)

- Existing approval “Давай так сделаем.” retained; later live Claude deferral is not a proof waiver.
- Delivered: one full neutral owner; actual PM/Architect trigger/load; both carriers/entry pointers; saved HOLD/evaluation/decision links; no new engine/role/phase/schema.
- Verified: independent QA2 on320-file45ef0b47/input10eea56c;600/146/526ordinary tests without skips, original private checks/three adapters/three maps,42own XML contracts; bounded actual Codex important/trivial/settled cases with true e350 identities and operative byte equivalence.
- Retained: original BLOCKED/code, I2 failed wave, QA1 BUG_REPORT and actual counted Debug1 fixing historical label/positive trace visibility; no current actionable source defect. M30Debug1/4 is distinct from exhausted C3.
- **Held/UNFULFILLED:** actual native Claude AC4/ClaudeAC5 under explicit deferral. Terminal BLOCKED/qa; whole Review/assigned Finalize/full checkpoint acceptance incomplete. Owner-approved source integration through PR6 is complete; [record](notes/m30-integration.md). No Claude auth/engine retry now.
- [Result/history](notes/m30-result.md), [approved spec](specs/m30-independent-decisions.md), [operative plan](plans/m30-independent-decisions-i2.md), [input correction](notes/m30-input-correction.md). Four current records plus result note are a separate closure after judged source.
- Next: required Claude proof only after owner changes deferral, then independent acceptance/Review/Finalize. INTAKE-01 remains separately proposed; C4–C6/trial route/C3 history retained. M30 source merge is complete; no installation/public visibility change or C3 merge.

## M31 — owner-directed lightweight PM (current)

Direction and merge/reissue/installation accepted by the owner; [decision/scope](notes/pm-lightweight-direction.md). Shared and both native carriers reflect the lightweight boundary. Release identities: neutral3.0.0, Codex3.0.0, Claude2.0.0; only exact executable binding constants/current-version assertions change, original algorithm pins/wire/schema/inventories remain.

Bounded release checks and actual installation readback apply; no feature-dev/QA role or new run ledger for this documentation release. Codex uses a complete repository snapshot; Claude loads canonical main in place. The decision note carries actual completion. Retain M30 deferred Claude proof and exhausted C3 separately; installation is not their acceptance.

### M31 completion receipt

PR8 merged at3dd4d626; private release v3.0.0 includes the complete archive and checksum. Codex3.0.0 installed/enabled and all27 skills actually discovered through app-server; the superseded personal PM plugin disabled/retained. Claude2.0.0 configured in place; manifest and actual SessionStart binding pass. Configuration backup retained. Installed source stays frozen at the release commit; subsequent maintainer receipt changes are not repackaged source. Start a fresh session for the new catalog; see [HANDOFF](HANDOFF.md). M30 live Claude deferral and C3 remain unchanged.
