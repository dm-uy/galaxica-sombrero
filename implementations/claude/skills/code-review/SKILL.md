---
name: code-review
description: "Use when a stable, completed candidate (a diff, a branch or a finished run) needs an independent cumulative review before the result decision. The reviewer is a separate read-only agent; it never repairs."
---

# code-review

Obtain an independent judgment of the whole current delta, with located findings or evidenced absence of findings.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../roles/reviewer.md`
- `${CLAUDE_PLUGIN_ROOT}/../../flow/finalize.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/code-review.md` (a disclosed stub: it supplies no procedure, the substantive reviewer role and the Finalize evidence apply)
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Confirm the candidate is stable and complete, and gather its absolute paths: target, specification, plan, framework, baseline and candidate identities, MAY EDIT and DO NOT TOUCH, and the QA evidence for the same candidate.
2. Record `git status --porcelain -uall` and HEAD, then dispatch the reviewer with the Agent tool: `subagent_type: methodology-claude:reviewer`, `model: opus`, a self-contained assignment and the granted evidence path. Never review your own work as the independent judge.
3. The reviewer reads the baseline-to-result delta including new and untracked files and the surrounding source, and judges correctness, regressions, contracts, boundary, data-loss, concurrency and security impact, and the real side effects. It returns SUCCESS, BUG_REPORT or BLOCKED with located findings (title, severity, path and line, trigger, impact, evidence, recommendation) or evidenced none and its limits.
4. Record `git status --porcelain -uall` again and report every change outside the granted paths. Validate the returned object yourself before using it; a populated BUG_REPORT goes to counted Debug through feature-dev, and the review itself fixes nothing.

Limits:
- The reviewer never repairs, commits, merges or approves integration; the result decision stays with the owner.
- Original files and Git state are read-only for the reviewer; a check that needs a changed tree uses an authorized copy without `.git`.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.
