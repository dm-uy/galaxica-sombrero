---
name: document-protocol
description: "Use when authoring a structured technical document, requirements set or specification that other agents will parse: outline first, paired boundaries, explicit contracts and directed links."
---

# document-protocol

Produce a document whose structure survives zero-context reading: the outline comes first and every artifact carries its own contract.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../protocols/document.md`
- `${CLAUDE_PLUGIN_ROOT}/../../documents/conventions.md`
- `${CLAUDE_PLUGIN_ROOT}/../../FORMAT.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Write the complete DOCUMENT_PLAN before expanding any section.
2. Expand with nested, correctly paired document, section, artifact, contract, body and link boundaries. Give every artifact an explicit TYPE and KEYWORDS, its purpose, description, rationale and acceptance criteria, a substantive body, and real directed ID links to other artifacts.
3. Reconcile the outline with the bodies: every planned item exists and every body is planned.
4. Choose the format by the document's home. Methodology package cards use their own declared format; project records keep the homes and conventions the project adopted. Do not retrofit existing documents unasked.

Limits:
- Structure is not meaning: a passing parser or linter does not show that the content is correct.
- Write only inside the granted paths and report any other write you find.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.
