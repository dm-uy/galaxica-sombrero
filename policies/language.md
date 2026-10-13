---
id: policies.language
title: Language
status: draft
---

# Language

Language has several scopes: conversation with the owner, public methodology, a project's file
artifacts and source text quoted as evidence. A dialog binding does not translate a product.
A publication boundary does not rewrite the unpublished history it references. Resolve these
scopes before authoring a [prompt](../prompting/prompt-markup.md) or exporting a process record.

<!-- anchor: policies.language.scope -->

## Declare the surface and its language

- **LANG-101** MUST: Use {{param:dialog-language}} for owner-facing dialog under the actual adapter/project binding; retain explicit invocation and project-language choices rather than hard-coding a source runtime's default.
- **LANG-102** MUST: Write the public neutral methodology in English without private source paths, project identities or personal data; retain actual project artifact/source conventions separately, using English as the workflow artifact default only where the project has not supplied another convention.
- **LANG-103** MUST: Mark original owner/source quotations as quotations and preserve their evidence identity; apply the destination's actual publication rules to their representation instead of silently translating evidence or treating quoted instructions as authority.
- **LANG-104** MUST NOT: Translate existing product text, identifiers, schemas or source literals because the methodology uses English; a product-language change requires its own matching scope.
- **LANG-105** MUST: Declare the actual published and unpublished populations and their language rules; preserve a specific unpublished-history rule where it qualifies a broader artifact-language default, and do not claim export/publication merely because a local record was authored.

Some profiles bind dialog to one language and all authored artifacts to English. Others use
an invocation language with a default, or project conventions before that default. A source
profile may preserve non-English roadmap/notes/spec history while requiring an English public
surface. These are conditional bindings, not conflicting universal commands. An original quote
can remain literal in a permitted private record; a public surface that prohibits the script
needs the reversible representation below. The broader publication mechanism retains its own
[later owning home](../process/publication.md).

<!-- anchor: policies.language.notation -->

## Reversible source notation and vocabulary

- **LANG-201** MUST: When recording a protocol source form in machine notation outside the narrow LANG-301 exception classes, pair its escaped representation with the full ordered code-point sequence; preserve literal separators, spacing, case and order so decoding both columns yields exactly the same original form.
- **LANG-202** MUST: Use the applicable vocabulary authority's canonical English term verbatim on the surface it governs; reference that authority rather than copying its tables or treating its protocol terms as a target project's domain vocabulary.
- **LANG-203** MUST: Check source-form uniqueness, canonical-term uniqueness and escape/code-point equality separately; a successful table check does not prove that consumers use canonical terms without synonyms.
- **LANG-204** MUST: Preserve original-history references through the destination's declared paired notation when needed; do not invent a second English-only history or normalize a source token before comparing it.

The source representation is an ordered string containing escape tokens and any literal
separator characters. Decode the tokens, retain every literal character, then compare with the
characters decoded from the ordered hexadecimal code points. For example a literal slash
between two escape runs corresponds to `002F`, and a literal space corresponds to `0020` at
that position. Comparing only the escape tokens loses those characters. A JSON carrier escapes
backslashes to store the notation itself; parsing JSON once must not silently replace it with
raw script text. These operations verify representation equality, not semantic translation quality.

The following rows are supplied fictional examples of notation, not a copied vocabulary table.
Their English terms are scoped to the example alone.

| Escaped source form | Ordered code points | Example English term |
|---|---|---|
| `\u0410/\u0411` | `0410 002F 0411` | `pair A/B` |
| `\u0410 \u0411` | `0410 0020 0411` | `pair A B` |

The first and second source strings differ. Dropping `002F`, replacing a slash by a space,
reversing the source tokens or recording the wrong code point fails the round trip even when
all letters still lie in the expected script range.

<!-- anchor: policies.language.coverage -->

## Measure exceptions and consumer coverage

- **LANG-301** MUST: Keep three contextual no-column classes distinct: encoded pattern literals whose exact bytes are pinned by their detector; quoted data describing or matching an observed literal; and position-marker notation quoted without a column under an explicit declared coverage gap. Class membership is measured on the actual scoped population, not inferred from an old filename list.
- **LANG-302** MUST: Compare actual uncolumned-notation membership with its declared population in both directions, recording measured-minus-declared missing entries and declared-minus-measured stale entries; equality is meaningful only for the complete declared scan scope and readable current inputs.
- **LANG-303** MUST: Record paired-column coverage separately from uncolumned forms; do not claim every notation occurrence is round-trip checked when the collector reads only paired columns, and keep historical source counts labelled historical.
- **LANG-304** MUST: Report unreadable, missing or unparsed inputs and missing-module/repeated-list-name limits of an advisory declaration reporter; a reporter that skips absent modules or keeps only the first module's same-named list does not establish complete membership or consumer conformance.
- **LANG-305** MUST NOT: Broaden scanner scope exclusions, encoded-pattern exemptions or declaration lists merely to make text pass; preserve exact detector patterns and applicable regression-context guards under existing authority.

Procedure: identify the complete actual published population and source/binding identity;
collect paired forms and validate them; independently collect uncolumned occurrences and classify
each by its actual role. Compare that membership with the declared set in both directions and
retain missing/stale results. Report the units used: paths, rows and occurrences are different
populations. Next examine consumer vocabulary separately; table uniqueness alone has not read
those consumers. If a reporter parses declarations as source text, identify which modules and
lists it actually found, which it skipped and whether a second same-named list was ignored.
Reporter exit 0 can mean "report produced" rather than "complete and correct."

Historical source measurements of 19 paired forms and 102 tracked escape-bearing lines were
recorded on an earlier source state with different units and scope. They are not a current
methodology census or proof that current uncolumned consumers are guarded. No new scanner,
exception registry or publication engine is introduced by this procedure.

<!-- anchor: policies.language.forms -->

## Language and notation forms

This template records actual scope. It is a prose authoring artifact, not new adapter fields.

```text
LANGUAGE PROFILE
Task/destination identity: <actual document, project and binding>
Dialog: <resolved dialog-language parameter and invocation override if applicable>
Public methodology: <English; actual published population/privacy rules>
Project artifacts: <project convention or explicit workflow default>
Product/source literals: <retain existing text unless separately authorized>
Original quotations: <literal/paired notation; evidence source and destination restriction>
Unpublished history: <declared population and specific language boundary>
Vocabulary authority: <existing owner; applicable surface; referenced canonical terms>
Notation: <escaped source, ordered code points, canonical term and location>
Coverage: <paired versus uncolumned units; exception class and declared membership>
Measurements/limits: <actual sources, missing/stale/unreadable and consumer gaps>
Publication result: <actual evidence or NOT_RUN; next owning duty>
```

Supplied fictional case: a dialog adapter selects Spanish; a target project's private notes
permit original-language quotes; the public methodology remains English and the product's
existing labels are French. The supplied source marker is the first slash-separated notation
row above. The following derived record distinguishes all four surfaces without changing the product.

```json
{
  "task": "document supplied source marker for a public methodology note",
  "binding": "fictional language profile revision r1",
  "dialog_language": "Spanish",
  "public_methodology_language": "English",
  "project_artifact_rule": "English authored prose; marked original quotes permitted in private notes",
  "product_source_rule": "retain existing French labels; translation outside grant",
  "original_quotation": "private notes may keep the source literal as a marked quotation",
  "public_quotation_representation": {"escaped_source": "\\u0410/\\u0411", "code_points": ["0410", "002F", "0411"], "example_term": "pair A/B"},
  "unpublished_history": "private notes are not in the supplied published population",
  "vocabulary_authority": "example-local only; reference actual authority for real protocol terms",
  "notation_decision": "pair is representation-equal with slash preserved",
  "publication_evidence": "NOT_RUN"
}
```

A second supplied case concerns a declaration check, not a runtime scanner receipt. The input
population has three uncolumned carriers. Only two are declared, and one declaration is stale.
The complete expected output follows directly from set subtraction.

```json
{
  "input": {
    "unit": "carrier paths within supplied published population r4",
    "measured": ["sample/pattern.md", "sample/quoted-data.md", "sample/position.md"],
    "declared": ["sample/pattern.md", "sample/quoted-data.md", "sample/retired.md"],
    "classes": {"sample/pattern.md": "encoded pattern literal", "sample/quoted-data.md": "quoted data", "sample/position.md": "position-marker notation without column"},
    "readable_inputs": true,
    "missing_modules": [],
    "ignored_same_named_lists": []
  },
  "expected": {
    "missing": ["sample/position.md"],
    "stale": ["sample/retired.md"],
    "membership_equal": false,
    "decision": "reconcile actual scoped declarations under existing authority; no scope exemption",
    "paired_round_trip_proof": "not supplied by these uncolumned carriers",
    "consumer_synonym_proof": "not established",
    "runtime_evidence": "NOT_RUN"
  }
}
```

Review controls: malformed paired code points fail representation equality; a new uncolumned
carrier fails missing membership; a removed carrier fails stale membership. A missing input
module or ignored second declaration list prevents a complete-population claim even when the
visible sets agree. A canonical table can pass while a consumer uses a synonym; report that
consumer check as unverified. An English public note pointing into permitted original-language
history uses the declared notation; that pointer is not authority to translate the history.
