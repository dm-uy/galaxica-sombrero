# Current: RECON-DEC integrated locally and installed

## Owner decisions

Nothing remains for the bounded requested merge/install task. The owner accepted the concrete result and explicitly granted local main merge and installed Codex/Claude/DSH updates; [decision, execution and limits](notes/spec-recon-decision-checkpoint-result.md#accepted-merge-and-installed-updates--2026-11-03). The owner then authorized remote delivery; [main push and readback](notes/spec-recon-decision-checkpoint-result.md#remote-main-delivery--2026-11-03) completed. No unrelated consumer migration is included.

## Current result

Canonical main fast-forwarded to `40328d0b9e67df6f4848b04750f68d5957563103`. Installed Codex4.0.0 uses a complete immutable snapshot of that commit; native install/list, fresh app-server skill discovery and full tracked-byte/executable-mode comparison passed. Previous release/config/catalog backups are retained. Claude3.0.0 reads canonical main in place; native discovery, manifest and actual SessionStart binding to neutral4.0.0 pass. Both registered DSH profiles resolve4.0.0 and their actual filesystem providers discover/load27skills; fresh web composition passes. Desktop full composition remains Electron-only, so active desktop runtime/catalog refresh is unverified.

Source implementation/affected checks/independent review and bounded synthetic behavior remain in [the result receipt](notes/spec-recon-decision-checkpoint-result.md). This closure changes project records only; it does not repackage the installed Codex source snapshot. No active client/session was restarted; use fresh sessions and client restart guidance to load the refreshed catalog. This chat's original catalog is not hot-reload evidence. No model efficacy, hard enforcement or deferred whole-flow acceptance is inferred.

## Continuation

[Tasks](TASKS.md#recon-dec--reviewed-recon-forks-and-owner-authorized-brainstorm). Any later source update, remote publication or consumer migration needs its matching task/action grant. Reuse the completed result decision; do not ask to merge/install this same source again. Current record closure is performed under that existing grant. Preserve the retained obligations below.

## Relevant previous state

PM-INVOKE (Claude 2.4.0) was fast-forwarded into canonical `main` under the owner's 2026-10-28 decision, without push. Its first-fresh-session live probe is still unverified. [Original task, authority and retained probe](TASKS.md#pm-invoke--model-invocable-lifecycle-commands-claude-240-branch-in-review). The later explicit push grant covered the accumulated main delta and delivered these commits too; the original local-only decision is retained as history.

PR19 was accepted, merged and installed under its separate grant. [Receipt and limits](notes/brownfield-source-correspondence.md#merge-and-installed-version-update--2026-10-27). Its installed snapshot proof is not a new runtime efficacy result and is not changed by this documentation task. The earlier continuation and failures remain in those records; no release or installed snapshot was repackaged.

## Retained obligations and relevant traps

- GRACE-Q2 is integrated and delivered; its then-withheld installation is now superseded by the installed PR17 snapshot. [Result and history](notes/grace-qa-evidence-minimal.md). This is history, not another current-version or next-action block.
- M37 consumer migrations still need per-project grants; old in-house plugins are disabled. Retirement losses and historical launcher/PATH caveats remain at [M37](notes/m37-claude-parity.md). [M37 tasks](TASKS.md#m37--claude-package-actualization-merged-through-pr11).
- DSH full-flow probe3 needs a matching target/scope; use the desktop profile deliberately and preserve previous profile backups. [M38](notes/m38-dsh-package.md), [probe evidence](notes/m38-run-01.md).
- C3 remains terminal, unaccepted and exhausted at Debug4/4; no fifth repair or reset. [C3 result](notes/m28-c3-result.md).
- M30 source is integrated and native Claude observations exist through M37, but renewed QA/Review/Finalize and full acceptance remain owed. [M30](notes/m30-result.md), [M37](notes/m37-claude-parity.md).
- The later safeguard/API-database/C4-C6/frontend/Telegram/MCP route remains separately scoped. [ROADMAP](ROADMAP.md). No deferred code continuation is authorized by this correction.
- Use Python3.12 for interpreter-bound AST pins. Run source/package checks in a clean Git-free copy: ignored methodology Markdown can alter inventories. Genuine algorithm changes require review, never automatic re-pinning.
- Preserve known run-state limitations (architect response correction after plan creation; terminal runs cannot restart), explicit in-place versus copied loader boundaries, and missing private self-check coverage. Details remain in [M36](notes/m36-session-handoff.md), [M37](notes/m37-claude-parity.md) and [M38](notes/m38-dsh-package.md).
