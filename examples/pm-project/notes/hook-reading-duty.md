# HOOK-DUTY — SessionStart reading duty scoped to software roles — 2026-11-10

## Owner request and decision

The owner asked whether the methodology could be made lighter after a consumer project replaced the five record forms with self-contained light records. The root measured the mandatory reading and obtained an independent decision packet (below). Its leading candidate was a defect correction, and the owner authorized it with the words «чини хук» on 2026-11-10.

Scope of that authorization: the SessionStart hook sentence of the Claude package and the test pins that hold it, on a separate branch with a pull request. It does not authorize a merge to `main`, a package version change, any other candidate of the packet, or any change to a neutral owner.

## The defect

The hook told every bound session: "Before any methodology role or skill work, read … claude-runtime.md and the six core owners in full". Its own owners state a narrower duty:

- `implementations/claude/references/adoption.md` step 2: "Before any software role acts, read the six core owners in full".
- `implementations/claude/references/claude-runtime.md` section 2: "the six core owners before any software role acts".
- `concepts/principles.md` PRIN-101: "For an assigned software role governed by ROLE-103".

`claude-runtime.md` opens by calling such a difference a package defect. Codex and DSH state only the narrow duty (`references/adoption.md` line 7 in each) and install no start hook, so the defect was in the Claude package alone.

Effect of the wide sentence: a session doing records, research or route work was told to read 102,318 bytes in seven files before its first action; 54,645 of those bytes are the four code-layer owners.

## Change

| Path | Change |
|---|---|
| `implementations/claude/hooks/session_start.py` | One string constant of `render_context`: "… read `<package>/references/claude-runtime.md` in full; before any software role acts, read the six core owners in full; Orient by checks/orient.md." Three contract comments follow it. No other executable change. |
| `implementations/claude/tests/test_session_start.py` | The exact-sentence assertion follows the new sentence; one added assertion refuses the old wide form. |
| `tests/test_c1_review_and_routing.py` | The whole-AST pin of the hook is re-based from `4ee9d7d1…c1e25` to `50cc2c54…f649` under the same serializer. The comparison still permits only the exact `PACKAGE_VERSION` change; both contrary controls are unchanged. |
| `tests/test_guide.md`, `implementations/claude/tests/test_guide.md` | One dated sentence records the re-based pin beside the retained pre-correction values. |

Package version stays 3.1.0 and neutral 4.1.0. The run-state helper refuses ledgers of another package version, so a version change for a one-sentence correction would strand running ledgers in consumer projects; whether to stamp a patch version is left to the owner.

## Checks

On branch `claude/hook-reading-duty`, based on `b8a24a3`, Python 3.12:

- Claude package suite: 548 passed, before and after the test-guide sentence.
- Root suite: 616 passed.
- Real hook process with a real SessionStart payload for a consumer project: exit 0, bound, the context carries the new sentence and the record-presence line. The same payload against `main` still returns the wide sentence.

Not done: Codex and DSH suites were not run because no path of theirs changed; the root suite, which covers their packaging contracts, passed. No live Claude Code session was started on the branch. The package loads in place from `main`, so the correction reaches sessions only after a merge, and the first session start after that merge is the live check.

## Left open

- `implementations/codex/tests/test_guide.md` and `implementations/dsh/tests/test_guide.md` line 174 repeat the sentence "The test retains the ORIGINAL3.9 pin". After this change the pin is re-based, so that sentence is historical there. Sibling packages have their own writers; not edited here.
- `implementations/claude/adapter.json` and `adoption.md` describe the mechanism as "injects the binding status and the six-core reading duty; every carrier lists the six core owners". It stays true for the six role carriers under `agents/`; among skills only `semantic-exoskeleton` lists all six. Not changed.
- Whether a root session that runs the `pm` skill counts as an assigned role under ROLE-103 is not settled by the text. The hook now repeats its owner's sentence and does not decide this.

## Decision packet (private evidence)

The independent packet of `prompting/brainstorm.md` was obtained before this correction: two fresh generators and one separate evaluator, each a distinct subagent with the requested model `opus`, bound to methodology `b8a24a3`. Ten candidates fall into five mechanism families: correct the hook duty; bind skills to anchored sections; an opt-in light records profile; a small kernel with a trigger-loaded library; machine enforcement in place of reading. The evaluator's bands put the hook correction first under both declared weightings and leave the other families unordered or below.

The packet is kept in the canonical checkout's ignored `.methodology/decisions/lightening-2026-11-10/`; preserve it before any cleanup. Contamination limits: separation of actors was behavioural, and all actors share one model family.

| File | SHA-256 |
|---|---|
| `brief.md` | `45faf739ee6a14cd1927f3c2bcc9e4d2677dbd5b9a40d3ea8907558ffb286e56` |
| `hold-generator-a.md` | `265683e6bbfa3f2f6770c90803bb26f00db84788beb3123f0c2678155c8aa373` |
| `hold-generator-b.md` | `afb97f324afbda208ff90b668c8d3755a36a9b0eba26e4377ec2a94b30cb9e30` |
| `hold.md` | `8b55e00a69add115a035e300db02d62a85639905efc328163f6cf92cd6101164` |
| `evaluation.md` | `960783fe688a2ce3f2a03f09905afe0d68a3b94b6791ee60e764654feb81f52d` |

Selected: the hook correction only. Held for the owner, with no implementation authorized: section-level binding (changes the "read in full" check and, for role owners, the meaning of ROLE-102); a light records profile (changes GATE-501 and GATE-504; depends on a cold start in the consumer project that has not been run); the kernel and the enforcement families. Reopening evidence: the cold-start result, and a pilot of section binding on one skill with an independent compliance check.
