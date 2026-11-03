---
name: brownfield-spec-template
description: "ТЗ на изменение существующего проекта: «напиши ТЗ на доработку», «спецификация изменения существующего проекта», «ТЗ на рефакторинг или фикс». Use when reconnaissance of an existing project is complete and a change specification for it must be written (feature addition, refactoring, fix). Not for a genuinely new product."
---

# brownfield-spec-template

Write the change specification of an existing system as a measured delta, ready for the owner's gate.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../protocols/spec-brownfield.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/specification.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Confirm the reconnaissance is complete and measured (load spec-recon if it is not). A brownfield specification without a reconnaissance input is returned to reconnaissance, not approved.
2. Read the actual producers and consumers of the surface that changes: the current Doxygen XML map when it exists, otherwise Grep for `GREP_SUMMARY|STRUCTURE` markers and then the relevant source. Do not copy claims from documents that the source contradicts.
3. Write the current brownfield form: measured context and the RECON pointer, the added behavior, stable BR and AC ids with their exact quantifiers, an Expected Architecture verified against source, MAY EDIT and DO NOT TOUCH, regression constraints, the delivery contract, the real probe and the risks, plus the current Doxygen prerequisite.
4. Resolve every human-dependent contradiction before Code: ask the owner with AskUserQuestion and record the answer. List any known deficiency explicitly, because an approval may only accept a deficiency it names.
5. Mark the result a draft and route it to the specification gate through hitl-gates.

Limits:
- A draft is not an approval, and approving a specification grants no result decision.
- Do not narrow or reinterpret an original requirement silently; record it as a deviation for the owner.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.

Specification-producing RECON checkpoint: read the full `process/reconnaissance.md` Questions and forks section. Save explicit questions and evidenced exclusions; obtain a distinct fresh completeness check even for an empty list, reconcile original findings, and present the reviewed packet to the human. Obtain or reuse authentic matching permission for named brainstorm items before dispatch; silence/decline holds dependent readiness. Trace actual resolutions into BR/AC/boundaries before claiming the spec ready. No empty brainstorm request, self-certified completeness, new role/schema or automatic fanout; standalone non-spec summaries remain outside this checkpoint.
