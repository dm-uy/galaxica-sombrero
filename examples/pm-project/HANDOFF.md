# Current: PR17 merged; working packages updated

The owner explicitly requested PR merge and installation on 2026-10-21. [PR17](https://github.com/dm-uy/galaxica-sombrero/pull/17) is merged at `a3210036e43c1ce0c873df46e50b560a7e1da93e`, including reviewed head `bfdb2e9edb4925b547b9d98165c025078488e958`. Source versions are neutral/Codex/DSH3.1.0 and Claude2.2.0. [Scope, review history and installation receipt](notes/qa-reflection-clarification.md); [tasks](TASKS.md).

## Current result and evidence

Codex uses the complete immutable merge snapshot through the existing methodology-local marketplace: enabled3.1.0, fresh app-server discovery of27 enabled skills, including PM, feature-dev and prompting-verify. Independent verification matched all426 tracked files and executable bits in both release and installed cache; the sole extra is the root transport manifest with only its skills path changed. Prior config/catalog and release snapshots are retained for rollback.

Claude stays in place on canonical main: native plugin details discovers2.2.0; validation and actual SessionStart binding to neutral3.1.0 pass. DSH web/desktop remain registered in place and both resolve3.1.0 with27 skill files. Fresh web configuration composes the methodology provider. CLI dumping desktop was refused because Electron exclusively manages that profile; desktop's fresh runtime catalog was not checked. No active application or user session was restarted.

The earlier full-suite results belong to dc25ea4; bounded comment/record/reference follow-up checks belong to the reviewed PR head. Installation checks are loading/integrity evidence, not new full-suite tests or real-agent efficacy proof. Original failed attempts and retained obligations remain in their linked records.

## Next action

Start a fresh session in each affected client for refreshed discovery; follow the DSH package's profile-restart guidance when needed. This construction conversation is not hot-reload proof. The next substantive development work requires its own actual scope from the retained route; merge/install approval is fulfilled. This receipt-only closure does not repackage the frozen Codex snapshot or publish a release tag.

## Retained obligations and relevant traps

- GRACE-Q2 is integrated and delivered; its then-withheld installation is now superseded by the installed PR17 snapshot. [Result and history](notes/grace-qa-evidence-minimal.md). This is history, not another current-version or next-action block.
- M37 consumer migrations still need per-project grants; old in-house plugins are disabled. Retirement losses and historical launcher/PATH caveats remain at [M37](notes/m37-claude-parity.md). [M37 tasks](TASKS.md#m37--claude-package-actualization-merged-through-pr11).
- DSH full-flow probe3 needs a matching target/scope; use the desktop profile deliberately and preserve previous profile backups. [M38](notes/m38-dsh-package.md), [probe evidence](notes/m38-run-01.md).
- C3 remains terminal, unaccepted and exhausted at Debug4/4; no fifth repair or reset. [C3 result](notes/m28-c3-result.md).
- M30 source is integrated and native Claude observations exist through M37, but renewed QA/Review/Finalize and full acceptance remain owed. [M30](notes/m30-result.md), [M37](notes/m37-claude-parity.md).
- The later safeguard/API-database/C4-C6/frontend/Telegram/MCP route remains separately scoped. [ROADMAP](ROADMAP.md). No deferred code continuation is authorized by this correction.
- Use Python3.12 for interpreter-bound AST pins. Run source/package checks in a clean Git-free copy: ignored methodology Markdown can alter inventories. Genuine algorithm changes require review, never automatic re-pinning.
- Preserve known run-state limitations (architect response correction after plan creation; terminal runs cannot restart), explicit in-place versus copied loader boundaries, and missing private self-check coverage. Details remain in [M36](notes/m36-session-handoff.md), [M37](notes/m37-claude-parity.md) and [M38](notes/m38-dsh-package.md).
