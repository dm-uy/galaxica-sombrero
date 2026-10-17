# M37 decision packet — how the Claude package gains the consumer PM profile

Consequential-open choice under [brainstorm](../../../../prompting/brainstorm.md#prompting.brainstorm.consequential): package and ownership boundaries, a shared command contract for consumer projects, test/membership oracles and long-term maintenance. Root-coordinated independent packet on 2026-10-16; the owner decides at the C2-port specification gate. Context: [M37 record](../m37-claude-parity.md).

| Step | Actor (Claude Code subagent, requested model) | File | Original SHA-256 | Public copy SHA-256 |
|---|---|---|---|---|
| Brief and predeclared criteria | root | [brief.md](brief.md) | `01838020ce941442ccc6660c820b578c903dd63660aa7fef3ad4fa92ef0d71c7` | `c619d2561b8642f0596240dc3e951141fcb40b4b715c1d81ae8d4a91d81172fe` |
| HOLD, generator A (5 alternatives) | fresh general-purpose, opus | [hold-generator-a.md](hold-generator-a.md) | `25cdfb784d42e979ea4e188860abc707e5f74b1df005a23bc9e97e45b7cdbde8` | `2b48ad707b60465cc5c2c806ea78a4c6765eee7a56a4956f0d98025861ba77b6` |
| HOLD, generator B (6 alternatives) | fresh general-purpose, opus | [hold-generator-b.md](hold-generator-b.md) | `269976cffafe26da8b1e3fcb912f28bac6f120d3b86644ff240d19ded40e58e6` | `30703cd4ed0a831025847420b37003ad41c09ac57bc097bdfbe23c35e66b9ac9` |
| Evaluation | distinct fresh general-purpose, opus; authored no proposal | [evaluation.md](evaluation.md) | `cb9759eee0610e6ce8c8aba0afea131b539dfd6c522f9d84aecf610fc7f7ab3c` | `a4f514b748a362641227f228afa0ae63fb6ee827d68eb9a8525468a2dfd4c1ff` |

Order: both generators received the same brief, read-only, in parallel, without peer output; the root saved each complete reply verbatim and hashed it before dispatching the evaluator, which re-verified the three hashes first. The evaluator merged 11 proposals into 8 mechanisms plus one hybrid of evaluated mechanisms, verified the pivotal facts in the files and scored them on the predeclared weights. Its recommendation is **H** — Claude references the Codex C2 helpers and seeds in place inside the complete checkout (thin Claude carrier, routing, `bin/` launchers that report BLOCKED when the sibling is missing, a root tripwire pinning the Codex files) plus an optional per-project SessionStart hook under a separate grant; runner-up **M1** (byte-locked mirror with a parity oracle) if the package must stay self-contained. Scores are reasoned judgments (about ±0.5), not measurements, and confer no authority.

Post-evaluation fact (root probe, 2026-10-16, Claude Code 2.1.285 headless, clean environment whose PATH held only `/opt/homebrew/bin:/usr/bin:/bin`): a scratch plugin's `bin/m37-bin-probe` ran by bare name in the Bash tool when the plugin was loaded in place, both with `--plugin-dir` and with `CLAUDE_CODE_PLUGIN_DIRS`. The evaluator's open question U1 is therefore answered positively; its first reopen condition does not fire.

Public copies are mechanically redacted: owner-local absolute and home-relative paths (including the run's worktree path, shown as `<worktree>`), the owner's local marketplace and organization names, and the five consumer project names are replaced by placeholders (`<home>`, `<owner-project>`, `<owner-agent-skills-checkout>`, `<owner-org>`, `consumer-A`…`consumer-E`). No other byte differs. The verbatim originals and their `SHA256SUMS` are kept in the owner's private evidence directory outside this public repository.

Decision status: open until the owner approves or reworks the C2-port specification.
