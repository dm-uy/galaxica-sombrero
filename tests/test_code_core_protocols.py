# region MODULE_CONTRACT [DOMAIN(9): CodeCore; CONCEPT(9): SourceFixedControls, Provenance; TECH(7): pytest, XML]
## @modulecontract
## @purpose Verify actual neutral core source, complete finite controls, extracted behavior and current own-entity XML evidence.
## @scope Core producers and exact allocation consumers; finite support recognition supplements independent full-prose/source review.
## @input Actual current repository, owned pytest scratch roots, source-fixed responsibilities and real Doxygen configuration.
## @output Assertion results, actual safe trace and full physical control/example/map artifacts.
## @links [READS_DATA_FROM(9): code core sources; USES_API(7): pytest, Python, Doxygen]
## @invariants
## - Function comment spans include final logical closures before endregion; string literals never provide semantic comment markers.
## - Complete own XML field content is source-bound, and label-only content loss refuses despite intact location.
## - Every mutation retains complete source files and exact numeric modes; no inspected source is written.
## - Expected duties precede observer outcomes; unknown association remains GAP rather than N/A.
## @rationale
## Q: Why full files and real child/XML probes?
## A: Labels and detached sentences cannot prove retained compound duties, runtime branches or own entity association.
## Q: Why retain independent prose review?
## A: Exact clause recognition has a finite literal boundary and cannot certify arbitrary semantic equivalence.
## @changes
## Debug1: PRE01 ordered comment containment; PRE02 actual relations; PRE03/04 isolated source-bound related sets; PRE05 conditional relation overview; PRE06 full own field content; PRE07 safe owned failures.
## LAST_CHANGE: [1.1.0 - Reconcile current M19 boundary/release facts and paired source operands; preserve original assertions/pins/refusals/restoration; runtime checks pending.]
## @modulemap
## FUNC 9[Bind genuine comment containers, ordered logical steps and complete own field continuations to current source definitions.] => test_code_core_protocols._source_entity_contracts
## FUNC 8[Bind complete sources to exact byte/mode identity before any fixture judgment.] => test_code_core_protocols._read_core_sources
## FUNC 8[Separate live responsibility text from illustrative fenced examples.] => test_code_core_protocols._live_core_lines
## FUNC 8[Observe finite source-fixed support/force/contrary losses without claiming general semantic completeness.] => test_code_core_protocols._core_failures
## FUNC 8[Deliver exact whole-file candidate controls and source-bound restoration into owned absent scratch roots.] => test_code_core_protocols._materialize_fullfile_control
## FUNC 8[Exercise the actually extracted worked function through a real Python process and expose its delivered streams.] => test_code_core_protocols._run_presence_example
## FUNC 8[Read only a current requested entity's own XML/location/fields and expose unavailable association.] => test_code_core_protocols._read_map_entity
## FUNC 8[Verify positive/loss/contrary/compound/restoration decisions on complete physical files.] => test_code_core_protocols.test_core_source_fixed_controls
## FUNC 8[Discriminate actual sample outcomes and safe successful/failing trace.] => test_code_core_protocols.test_core_presence_example_and_trajectory
## FUNC 8[Build actual XML and bind each authored function's own rich paragraphs to current source/location.] => test_code_core_protocols.test_core_map_identity_and_paragraphs
## FUNC 8[Refuse absent/broken/neighbor map evidence and prove only narrow configured absence.] => test_code_core_protocols.test_core_navigation_evidence_limits
## FUNC 8[Check invoked rich step/profile structure and bounded specimen AST equality without migration claim.] => test_code_core_protocols.test_core_profile_and_migration_contract
## FUNC 8[Validate the actual adjacent AC mapping against real test definitions.] => test_code_core_protocols.test_core_guide_direct_mapping
## FUNC 8[Require exactly eight current bodies and physically retained deferred homes.] => test_code_core_protocols.test_core_promotions_and_remaining_homes
## FUNC 8[Prove complete full-byte/mode restoration rather than detached sentence reconstruction.] => test_code_core_protocols.test_core_wholefile_restoration
## @usecases
## - Core AC 3/6: Source verifier -> test_code_core_protocols._source_entity_contracts -> exact genuine containers and complete own fields bound before map observation.
## - Core AC 1/8: Reviewer -> test_core_promotions_and_remaining_homes -> exact current/deferred split.
## - Core AC 2/3/4: Reviewer -> test_core_source_fixed_controls -> full-file observations supplement independent source/prose judgment.
## - Core AC 5/6/7: Verifier -> test_core_map_identity_and_paragraphs -> actual process/XML observations, external whole/artifact review remains owed.
## @GREP_SUMMARY code core, source fixed controls, rich fields, full-file restoration,
##   paired logical steps, exact modes, current map, independent prose limits
## @STRUCTURE ▶ complete source → ◇ fixed intentions → full controls → behavior
##   → actual XML → ⊕ independent review evidence
def _module_contract():
    pass
# endregion MODULE_CONTRACT


import ast
import hashlib
import json
import os
import pathlib
import re
import stat
import subprocess
import sys
import xml.etree.ElementTree as ET

CORE_FILES = ("code/exoskeleton.md", "code/navigation.md", "code/doxygen.md", "README.md", "roles/searcher.md", "roles/debugger.md", "protocols/graph.md")
RESPONSIBILITIES = {'E1': {'path': 'code/exoskeleton.md',
        'norm': 'EXO-101',
        'force': 'MUST',
        'supports': [['For authored code, wrap each module contract, function, class and method in correctly '
                      'named paired region/end-region boundaries at matching indentation. Nest methods inside '
                      'their class and retain natural algorithm bodies inside the semantic containers; '
                      'containment applies under the new-module versus edited-function locality rule, never as '
                      'unsolicited whole-file retrofit.']],
        'contrary': 'An authored function may omit its matching closing function region while retaining its '
                    'complete contract and logical steps.',
        'contrary_paths': ['code/exoskeleton.md'],
        'contrary_losses': ['E1'],
        'loss_losses': ['E1']},
 'E2': {'path': 'code/exoskeleton.md',
        'norm': 'EXO-201',
        'force': 'MUST',
        'supports': [['Start every new module with MODULE_CONTRACT before imports and without a duplicate '
                      'module-purpose docstring. Include purpose, scope, module input/output, semantic '
                      'links/dependencies, invariants, rationale Q/A, current changes with LAST_CHANGE, weighted '
                      'modulemap and actor/action/goal usecases. The LAST descriptive fields are in-contract '
                      'GREP_SUMMARY and STRUCTURE, then the configured Doxygen metadata anchor, contract end, '
                      'imports and entity regions. Preserve continuations; the comment syntax is a language '
                      'binding.']],
        'contrary': 'A new module may keep a duplicate module-purpose docstring in addition to its complete '
                    'correctly placed contract.',
        'contrary_paths': ['code/exoskeleton.md'],
        'contrary_losses': ['E2'],
        'loss_losses': ['E2']},
 'E3': {'path': 'code/exoskeleton.md',
        'norm': 'EXO-301',
        'force': 'MUST',
        'supports': [['Every authored function contract states its outcome and semantically relevant '
                      'APIs/modules, typed inputs and output, complexity and system importance. Rich substantive '
                      'information includes input invariants and ranges, output fields and format guarantees, '
                      'external side effects, operational guarantees, error types with triggering conditions, and '
                      'a concrete example where applicable. State absence or applicability explicitly. Purpose or '
                      'I/O vocabulary alone cannot replace these fields; class and method contracts retain their '
                      'own outcomes and correct containment.']],
        'contrary': 'An authored rich function contract may omit applicable input constraints, output shape, '
                    'effects, guarantees, triggered errors and example if purpose and I/O tags are present.',
        'contrary_paths': ['code/exoskeleton.md'],
        'contrary_losses': ['E3'],
        'loss_losses': ['E3']},
 'E4': {'path': 'code/exoskeleton.md',
        'norm': 'EXO-401',
        'force': 'MUST',
        'supports': [['Write project relation entities in uses, links and modulemap with their qualified '
                      'module.name or module.Class.method and actual package chain; external APIs retain their '
                      'own names. uses names semantic relevance rather than every call. Remove names the edited '
                      'body no longer uses. Preserve ALL block-tag paragraphs, continuation content, summary and '
                      'diagram in XML. In contract prose name tags without at-command syntax and avoid '
                      'HTML-shaped angle brackets; diagrams use 〈 〉.']],
        'contrary': 'Project relations in a complete contract and XML may use unqualified short names, and uses '
                    'must list every call regardless of semantic relevance.',
        'contrary_paths': ['code/doxygen.md', 'code/exoskeleton.md'],
        'contrary_losses': ['E4', 'D3'],
        'loss_losses': ['E4']},
 'E5': {'path': 'code/exoskeleton.md',
        'norm': 'EXO-501',
        'force': 'MUST',
        'supports': [['In an existing module add or edit contracts/regions only for authored or edited functions '
                      'and instrument only authored new control flow. Preserve untouched branches; do not '
                      'retrofit missing module metadata unsolicited. Update already-present module facts only '
                      'when affected and accurately known. Every NEW test module receives the SAME full module '
                      'tag set, with suite purpose, isolation/determinism invariants, AC-to-test usecases, '
                      'strategy rationale and each test duty in modulemap; every test keeps its own function '
                      'purpose. Legacy conversion within authorized edits does not authorize hand-moving '
                      'standalone summary/structure during a local function edit.']],
        'contrary': 'Editing one function permits an unsolicited full module-contract retrofit and '
                    'instrumentation of untouched branches.',
        'contrary_paths': ['code/exoskeleton.md'],
        'contrary_losses': ['E1', 'E5'],
        'loss_losses': ['E5']},
 'E6': {'path': 'code/exoskeleton.md',
        'norm': 'EXO-601',
        'force': 'MUST',
        'supports': [['Read the exact source before replacement. When fixing a complex known bug retain '
                      'BUG_FIX_CONTEXT with the issue, previous approach, cause/problem and chosen fix. Update '
                      'affected I/O, modulemap, changes/LAST_CHANGE, relevant uses, matching region names and '
                      'logs. Distill agreed business requirements into rationale and invariants without copying '
                      'private reasoning; do not fabricate history or document unchanged code as newly '
                      'authored.']],
        'contrary': 'A complex known-bug repair may omit its cause/chosen-fix scar while keeping all affected '
                    'metadata current.',
        'contrary_paths': ['code/exoskeleton.md'],
        'contrary_losses': ['E6'],
        'loss_losses': ['E6']},
 'E7': {'path': 'code/exoskeleton.md',
        'norm': 'EXO-701',
        'force': 'MUST',
        'supports': [['Keep high-recall domain/concept/technology keywords with their source 1–10 weights, '
                      'semantically weighted API/data links and modulemap entities, compact one-line module flow '
                      'diagram, exports/signatures and applicable environment/config dependencies. These describe '
                      'code meaning, not model telemetry. State environment/config dependencies in links with '
                      'READS_DATA_FROM and actual names; omit nonexistent dependencies explicitly.']],
        'contrary': 'An authored module may omit its applicable exports and signatures while preserving all other '
                    'complete module fields.',
        'contrary_paths': ['code/exoskeleton.md'],
        'contrary_losses': ['E7'],
        'loss_losses': ['E7']},
 'E7optional': {'path': 'code/exoskeleton.md',
                'norm': 'EXO-702',
                'force': 'MAY',
                'supports': [['Repeat a mini-diagram in a function description. For complexity above seven, '
                              'richer explanation remains optional in a dialect whose source says MAY, while an '
                              'invoked authoring dialect requiring a brief explanation retains that requirement; '
                              'do not silently exchange their forces.']],
                'contrary': 'Every function must repeat a mini-diagram and an extra description regardless of the '
                            'invoked source dialect.',
                'contrary_paths': ['code/exoskeleton.md'],
                'contrary_losses': ['E7optional'],
                'loss_losses': ['E7optional']},
 'E8': {'path': 'code/exoskeleton.md',
        'norm': 'EXO-801',
        'force': 'MUST',
        'supports': [['Apply backend markup unless an explicit written host rule prohibits it; absent '
                      'neighborhood markup, docstring style or structured logging is not prohibition. Ambiguity '
                      'defaults to apply and record the ambiguity. Browser/client code alone MAY use the '
                      'host-permitted minimal JSDoc purpose/invariants and comment-region/summary flavor, or its '
                      'host convention under the browser-only exemption. Browser verification uses the AX tree '
                      'and typed component tests. Generated migration revisions whose generator header/revision '
                      'structure is their contract are exempt from exoskeleton/LDD; retain the revision message '
                      'and inline why comments for hand-placed changes. Neither exception is a backend waiver.']],
        'contrary': 'Ambiguous backend host markup instructions may be recorded as an explicit written '
                    'prohibition without recording the ambiguity; all required markup otherwise remains present.',
        'contrary_paths': ['code/exoskeleton.md'],
        'contrary_losses': ['E8'],
        'loss_losses': ['E8']},
 'E9': {'path': 'code/exoskeleton.md',
        'norm': 'EXO-901',
        'force': 'SHOULD',
        'supports': [['Prefer small modules solving one clear task and simple explicit blocks, with approximately '
                      '300–500 lines as empirical target guidance rather than a universal acceptance ceiling. DRY '
                      'and modularity remain permitted; avoid opaque universal-switch abstractions. Historical '
                      'SFT activation, sliding-window and native-scale explanations are attributed source '
                      'rationale, not measured contemporary model facts.']],
        'contrary': 'The approximate module-size guidance is a universal acceptance ceiling and DRY is forbidden.',
        'contrary_paths': ['code/exoskeleton.md'],
        'contrary_losses': ['E9'],
        'loss_losses': ['E9']},
 'E10': {'path': 'code/exoskeleton.md',
         'norm': 'EXO-1001',
         'force': 'MUST',
         'supports': [['When markup migration is separately authorized, preview exact full old/new changes and '
                       'prove every changed Python line is an actual COMMENT token in BOTH versions for EVERY '
                       'promised supported Python interpreter, with identical parsed ASTs before ANY source '
                       'write. A failed proof aborts ALL writes. Preserve executable behavior, untouched scope, '
                       'line endings and custom aliases; leave ambiguous/external names and no-anchor cases '
                       'unchanged and report them. Never invent missing markup or relations. A comment-shaped '
                       'string or regex match is not token proof. This optional safety contract grants no '
                       'migration tool port, execution or broader source authorization. Where an actual runtime '
                       'migration engine is separately provided, preserve its dry-run/check/apply modes, complete '
                       'old/new Plan and violations, one authorized writer only after ALL proofs, exact '
                       'token/line coordinates and right-to-left replacements, '
                       'unparsed/no-anchor/ambiguous/external reporting, stale uses as information only, stable '
                       'sorted report categories including zero counts, exact unified diff/newline preservation, '
                       'stdout/stderr/exit contract and actual Python-version limits; its template remains '
                       'read-only.']],
         'contrary': 'An authorized markup migration may write sources before all supported-interpreter '
                     'COMMENT-token and identical-AST proofs, including ambiguous or no-anchor cases.',
         'contrary_paths': ['code/exoskeleton.md'],
         'contrary_losses': ['E10'],
         'loss_losses': ['E10']},
 'E11': {'path': 'code/exoskeleton.md',
         'norm': 'EXO-1101',
         'force': 'MUST',
         'supports': [['Name the actual language/host/authoring profile before authoring and record it in the '
                       'plan and test guide. Rich contract-authoring and migration profiles retain paired '
                       'logical-step boundaries for Validation, BusinessLogic and ErrorHandling where applicable, '
                       'correlated with actual logs. Donor-style code profiles retain plain internal step '
                       'comments without that second hierarchy and brief step explanations for complexity above '
                       "seven. Invoking one profile never erases the other profile's applicable MUST; no "
                       'universal paired-marker mandate or ban follows. Code-region syntax is separate from the '
                       'planned DraftCodeGraph grammar.']],
         'contrary': 'The invoked rich contract-authoring profile may omit its applicable paired logical-step '
                     'boundaries because a donor plain-step profile exists.',
         'contrary_paths': ['code/exoskeleton.md'],
         'contrary_losses': ['E11'],
         'loss_losses': ['E11']},
 'E12': {'path': 'code/exoskeleton.md',
         'norm': 'EXO-1201',
         'force': 'MUST',
         'supports': [['For configured Doxygen Python code place the dummy metadata anchor after the last '
                       'descriptive module fields and before contract end/imports. In a host explicitly '
                       'prohibiting Doxygen omit the anchor and keep pure comments; do not keep it and suppress '
                       'E402 on every import. Missing configuration is an owed bootstrap requirement, not a '
                       'neutral exemption. Language-specific region/JSDoc/import/lint bindings remain conditional '
                       'under actual target rules.']],
         'contrary': 'A missing Doxyfile permits omitting the map requirement and metadata anchor without '
                     'bootstrap or explicit host prohibition.',
         'contrary_paths': ['code/doxygen.md', 'code/exoskeleton.md'],
         'contrary_losses': ['E12', 'D1'],
         'loss_losses': ['E12']},
 'N1': {'path': 'code/navigation.md',
        'norm': 'NAV-101',
        'force': 'MUST',
        'supports': [['Start project-code navigation with the semantic GREP_SUMMARY/STRUCTURE overview, then '
                      'relevant contracts and nodes; consult a current generated Doxygen map before raw source '
                      'for relationships and unmarked areas. Source markup supplies semantic truth, generated XML '
                      'maps it and architecture prose describes intent. Use the bounded read-only Searcher for '
                      'deep marked-code work; keep unmarked/vendor exploration distinct. Jump from actual '
                      'function/block logs to their matching source steps and use dense domain/concept/technology '
                      'terms rather than sentence queries.']],
        'contrary': 'Project navigation may skip semantic overview and the current map and begin with unrelated '
                    'whole-source reads.',
        'contrary_paths': ['code/navigation.md'],
        'contrary_losses': ['N1'],
        'loss_losses': ['N1']},
 'N2': {'path': 'code/navigation.md',
        'norm': 'NAV-201',
        'force': 'MUST',
        'supports': [['State the actual answer source and precise fallback reason. Missing configuration/index, '
                      'stale or unparseable map, excluded source, unmigrated contract, absent OWN entity '
                      'paragraphs or unmapped nested symbol remains GAP/refusal for the unavailable map claim. '
                      'Fall back to source only where it answers and disclose omissions; isolate broken '
                      'compounds. Read-only navigation never executes inspected code or writes source/map: '
                      'request an authorized parent refresh. A degraded source answer never proves a current '
                      'complete map; unknown evidence is not N/A, which requires evidenced bounded absence.']],
        'contrary': 'For an index older than a covered source, a source fallback may certify a current complete '
                    'generated map; current own-entity paragraphs, file/location and configuration identity must '
                    'otherwise remain verified.',
        'contrary_paths': ['code/doxygen.md', 'code/navigation.md'],
        'contrary_losses': ['N2', 'D2'],
        'loss_losses': ['N2']},
 'N3': {'path': 'code/navigation.md',
        'norm': 'NAV-301',
        'force': 'MUST',
        'supports': [['Separate semantic declared relations from observed calls. Caller/callee evidence comes '
                      'from the actual code name scan, never from Doxygen declarations or uses alone. Label '
                      'by-name uncertainty and same-name collisions; resolve local import aliases only within '
                      'measured detector capability, attribute nested calls to their own definition, omit '
                      'self-edges and duplicate proofs, and list ambiguous matches rather than guess. Empty class '
                      'caller lists do not prove non-instantiation. No full dynamic call-graph completeness '
                      'follows.']],
        'contrary': 'Doxygen uses declarations establish a complete caller/callee graph and an empty class caller '
                    'list proves the class is never instantiated.',
        'contrary_paths': ['code/navigation.md'],
        'contrary_losses': ['N3'],
        'loss_losses': ['N3']},
 'N4': {'path': 'code/navigation.md',
        'norm': 'NAV-401',
        'force': 'MUST',
        'supports': [['Bind each map answer to the requested entity by current source bytes/identity, its actual '
                      'file/location and its OWN contract paragraphs, never coincident names or nested neighbors. '
                      'Read actual Doxyfile paths, titles and covered population; parse index first and only '
                      'relevant compounds, retain all continuations and current-form precedence, and disclose '
                      'irreversible rendering differences. Shared dummy metadata needs pinned own source fields '
                      'plus actual behavioral location and disclosed collision ambiguity. Empty compounds, shared '
                      'anchors or aggregate counts alone cannot certify association.']],
        'contrary': 'For entities with complete retained substantive paragraphs and verified current '
                    'source/file/location, a shared dummy anchor alone may resolve an undisclosed metadata '
                    'collision as the requested entity.',
        'contrary_paths': ['code/doxygen.md', 'code/navigation.md'],
        'contrary_losses': ['N4', 'D3'],
        'loss_losses': ['N4']},
 'N5': {'path': 'code/navigation.md',
        'norm': 'NAV-501',
        'force': 'MUST',
        'supports': [['Keep navigation tool implementation at the declared runtime boundary. Where the source '
                      'codemap dialect is supplied, preserve its actual stdout and exit contract: 0 answered, 1 '
                      'not found, 2 could not run; five labelled file lines with source second and (none) for '
                      'missing values; one block per ambiguous symbol; supported Python '
                      'file/function/method/class kinds and path forms. Preserve lazy per-run caches, skipped '
                      'unparseable-source disclosure, dotted/suffix/same-file resolution, restricted local '
                      'from-import alias handling, exact source I/O/errors/order/regexes and detector scope. No '
                      'universal shell permission, hidden coverage gap or tool port follows.']],
        'contrary': 'A supplied source codemap dialect may reorder file lines, guess ambiguous matches and '
                    'silently hide unsupported source.',
        'contrary_paths': ['code/navigation.md'],
        'contrary_losses': ['N5'],
        'loss_losses': ['N5']},
 'N6': {'path': 'code/navigation.md',
        'norm': 'NAV-601',
        'force': 'MUST',
        'supports': [['Retain an invoked runtime snapshot-first dialect: index.xml FIRST and ONLY, then bounded '
                      'per-compound XML; whole-snapshot reads are forbidden there, stale findings stay '
                      'unverified-stale and unavailable-map fallback is explicit. Its measured size rationale is '
                      'historical attribution. Neutral source-markup-first/map-before-raw navigation follows the '
                      "owning project precedence; this does not automatically change another runtime's dialect."]],
        'contrary': 'A runtime requiring snapshot-first index-only reads may read the entire snapshot first and '
                    'report stale findings verified.',
        'contrary_paths': ['code/navigation.md'],
        'contrary_losses': ['N6'],
        'loss_losses': ['N6']},
 'G1': {'path': 'code/navigation.md',
        'norm': 'NAV-701',
        'force': 'MUST',
        'supports': [['When a maintained post-code graph is actually part of the target contract, update added, '
                      'moved and deleted file entities in the same change. Show the load-bearing top-level '
                      'relations needed to orient across the represented files, retaining their actual '
                      'source-backed endpoints and meaning; node coverage alone is not that relation overview. '
                      'Compare the declared tree population against graph coverage, check unique normalized '
                      'identities and every local target, and record unfinished omissions INSIDE the affected '
                      'graph rather than silently leave it stale. Distinguish known gaps from intentionally '
                      'excluded generated/runtime populations and never certify partial coverage as complete. '
                      'Actual source/generation evidence is required; counts and dangling-link checks alone '
                      'cannot establish whole-tree coverage.']],
        'contrary': 'A maintained target graph may leave moved/deleted files silently stale and certify partial '
                    'coverage complete.',
        'contrary_paths': ['code/navigation.md'],
        'contrary_losses': ['G1'],
        'loss_losses': ['G1']},
 'G2': {'path': 'code/navigation.md',
        'norm': 'NAV-702',
        'force': 'MUST',
        'supports': [['Keep the optional maintained post-code KnowledgeGraph/AppGraph distinct from the canonical '
                      'planned DraftCodeGraph in the development plan and from the Doxygen semantic map. Full '
                      'generic taxonomy/weights/authoring grammar is now authored in [graph](../protocols/graph.md); '
                      'external knowledge/storage engines retain their exact runtime or later subject homes; '
                      'this interface neither implements them nor creates a competing architecture source.']],
        'contrary': 'An optional post-code graph is the canonical planned DraftCodeGraph and implements external '
                    'knowledge storage automatically.',
        'contrary_paths': ['code/navigation.md'],
        'contrary_losses': ['G2'],
        'loss_losses': ['G2']},
 'D1': {'path': 'code/doxygen.md',
        'norm': 'DOXY-101',
        'force': 'MUST',
        'supports': [['Provide the actual Doxyfile/tool prerequisites at bootstrap, preserve authorized '
                      'covered-source/exclusion configuration, and finish every code task and finalization with '
                      'an actual Doxygen build after passing tests and documentation fixes under target rules. '
                      'Missing configuration/tool is an owed requirement and unavailable evidence, never clean '
                      'PASS. The sole exception requires an explicit written target prohibition, quoted with '
                      'applicability. XML generation is mandatory unless explicitly prohibited; HTML presentation '
                      'is optional. Ignored XML output is rebuilt rather than committed; a second map owns its '
                      'separate configuration/output. Navigation readers request parent-owned refresh rather than '
                      'writing inspected trees.']],
        'contrary': 'Missing map configuration waives the owed configuration bootstrap and final build without '
                    'explicit written host prohibition; all other source and evidence duties remain required.',
        'contrary_paths': ['code/doxygen.md', 'code/exoskeleton.md'],
        'contrary_losses': ['E12', 'D1'],
        'loss_losses': ['D1']},
 'D2': {'path': 'code/doxygen.md',
        'norm': 'DOXY-201',
        'force': 'MUST',
        'supports': [['Derive covered sources and output/index from actual configuration. A fresh map has an XML '
                      'index newer than EVERY covered source, with current source/config identity also pinned. '
                      'Distinguish no sources yet, not built, fresh, in progress and stale. All newer files being '
                      'uncommitted may satisfy the lifecycle in-progress check but cannot certify a current '
                      'complete navigation answer; any newer committed file is stale, and outside Git only file '
                      'times apply. Excluded source is outside map coverage, not absent code. Source-changing '
                      'repairs renew affected checks/build; map-only rebuild is a distinct action.']],
        'contrary': 'An index older than a covered source may certify a current complete navigation answer; '
                    'current own-entity paragraphs, file/location and configuration identity must otherwise '
                    'remain verified.',
        'contrary_paths': ['code/doxygen.md', 'code/navigation.md'],
        'contrary_losses': ['N2', 'D2'],
        'loss_losses': ['D2']},
 'D3': {'path': 'code/doxygen.md',
        'norm': 'DOXY-301',
        'force': 'MUST',
        'supports': [["Verify actual XML/index and each covered current entity's own file/location/contract "
                      'association, including ALL substantive block-tag paragraphs and wrapped summary/structure. '
                      'Block aliases for modulemap, invariants, usecases, rationale and changes retain '
                      'continuation content instead of a trailing paragraph-closing ^^; same-line aliases '
                      'preserve their actual title/text form. Keep qualified relevant project relations and safe '
                      'prose. Empty file compounds and arbitrary AST/dummy-member quotas prove no association. '
                      'For shared launcher metadata pin its own source fields and the actual behavioral function '
                      'location and explicitly disclose ambiguity instead of renaming protected code to satisfy a '
                      'quota.']],
        'contrary': 'For entities with complete retained substantive paragraphs and verified current '
                    'source/file/location, a shared dummy anchor alone may resolve an undisclosed metadata '
                    'collision as the requested entity.',
        'contrary_paths': ['code/doxygen.md', 'code/navigation.md'],
        'contrary_losses': ['N4', 'D3'],
        'loss_losses': ['D3']},
 'D4': {'path': 'code/doxygen.md',
        'norm': 'DOXY-401',
        'force': 'MUST',
        'supports': [['Use a proven reader for the actual configuration population: quoting, comments, line '
                      'continuation, = reset and += append, '
                      'INPUT/FILE_PATTERNS/RECURSIVE/EXCLUDE/EXCLUDE_PATTERNS/symlink rules and the actual '
                      'project alias titles. Preserve custom aliases and template ordering in authorized '
                      'migrations. General last-assignment readers and dedicated append-aware alias readers are '
                      'distinct measured implementations; do not copy inconsistent algorithms or assume '
                      'all-entity counts suffice. Reader caches, paragraph inverses and fallback behavior remain '
                      'runtime bindings.']],
        'contrary': 'A reader may treat += as reset and ignore actual exclusion/alias configuration while '
                    'claiming the complete covered population.',
        'contrary_paths': ['code/doxygen.md', 'code/navigation.md'],
        'contrary_losses': ['N4', 'D2', 'D4'],
        'loss_losses': ['D4']},
 'D5': {'path': 'code/doxygen.md',
        'norm': 'DOXY-402',
        'force': 'MUST',
        'supports': [["Read only an entity's own detaileddescription for its titled fields. Where the measured "
                      'reader dialect applies, invert code spans to backticks, dash entities to --/--- and forced '
                      'spaces/linebreaks to one space, retaining visible text for other elements; disclose '
                      'irreversible bold/list renderings rather than invent original markup. Broken or missing '
                      'child elements/compounds retain scoped fallback evidence. A current index alone does not '
                      'establish every required entity paragraph.']],
        'contrary': 'An entity reader may reconstruct irreversible bold/list source markup without disclosing the '
                    'rendering difference, while retaining its complete own fields and current file/location.',
        'contrary_paths': ['code/doxygen.md', 'code/navigation.md'],
        'contrary_losses': ['N4', 'D5'],
        'loss_losses': ['D5']},
 # BUG_FIX_CONTEXT: F4 promotions changed both factual allocation alternatives; keep full residual duties and loss/refusal controls.
 'COMPLETION': {'path': 'README.md',
                'norm': '',
                'force': '',
                'supports': [['The exoskeleton, navigation, Doxygen, LDD, tests, AX, data and lints bodies are current F3 bodies; document and greenfield/brownfield specification protocols plus shared specification validation are current F4 bodies; general decision lifecycle (DEC01) and full graph are current F4 bodies; confirmed conventions, lifecycle, batch and session procedures and five project forms are current bounded F4 drafts; eight prompting F5 and three autonomy/credentials/language policy bodies are current bounded drafts; six neutral readiness contracts for principles, glossary, Orient, preflight, run audit and conditional safety/recovery are current bounded drafts; wider F4 duties, learning F8, source completeness, operational adoption and publication remain explicit later or unresolved homes.'],
                             ['Current F3 bodies are [exoskeleton](code/exoskeleton.md), [navigation](code/navigation.md), [documentation](code/doxygen.md), [LDD](code/ldd.md), [tests](code/tests.md), [AX](code/ax-ui.md), [data](code/data.md) and [lints](checks/lints.md). Current F4 bodies are [document](protocols/document.md), [greenfield specification](protocols/spec-greenfield.md), [brownfield specification](protocols/spec-brownfield.md) and [shared specification validation](process/specification.md). General decision lifecycle (DEC01) at [decisions](process/decisions.md) and [full graph](protocols/graph.md) are current F4 bodies; [specification](process/specification.md) retains its validation contract. Confirmed [document conventions](documents/conventions.md), [lifecycle](process/lifecycle.md), [batches](process/batch.md) and [session](process/session.md) procedures and [five project forms](documents/templates/INDEX.md) are current bounded F4 drafts, with full editable forms and fictional filled examples. Current bounded F5 prompting bodies are [agent design](prompting/agent-prompt-design.md), [GRACE](prompting/grace.md), [brainstorm](prompting/brainstorm.md), [decomposition](prompting/decomposition.md), [prompt markup](prompting/prompt-markup.md), [solution design](prompting/solution-design.md), [superposition and collapse](prompting/superposition-collapse.md) and [verification](prompting/verification.md). Current remaining policy bodies are [autonomy](policies/autonomy.md), [credentials](policies/credentials.md) and [language](policies/language.md); [model policy](policies/models.md) retains all eighteen current norms. Current bounded readiness contracts are [principles](concepts/principles.md), [glossary](concepts/glossary.md), [Orient](checks/orient.md), [preflight](checks/preflight.md), [particular-run audit](checks/run-audit.md) and [conditional safety/recovery](process/safety.md), with complete reusable forms and fictional cases. These bounded drafts do not complete all F5 or wider F4, source completeness, learning/evaluation, adoption or publication duties. Detailed F8 learning homes are [improvement](process/learning.md) and [knowledge](process/learning.md).']],
                'contrary': 'The three core bodies prove all remaining F3, F4, F5 and F8 bodies completed.',
                'contrary_paths': ['README.md'],
                'contrary_losses': ['COMPLETION'],
                'loss_losses': ['COMPLETION']},
 'NONWAIVER': {'path': 'README.md',
               'norm': '',
               'force': '',
               'supports': [['A stub or link never proves its detailed body completed.'],
                            ['The remaining subjects have deferred bodies; an interface or link invokes a subject without proving its body complete, including the eight completed F3 bodies.']],
               'contrary': 'A stub or link proves its detailed body completed.',
               'contrary_paths': ['README.md'],
               'contrary_losses': ['NONWAIVER'],
               'loss_losses': ['NONWAIVER']},
 'ADOPTION': {'path': 'README.md',
              'norm': '',
              'force': '',
              'supports': [['Runtime adoption and propagated enforcement remain unproven.']],
              'contrary': 'The core interface links prove runtime adoption and propagated enforcement.',
              'contrary_paths': ['README.md'],
              'contrary_losses': ['ADOPTION'],
              'loss_losses': ['ADOPTION']}}

COMPOUND_CONTROLS = {'M3-paragraphs': {'path': 'code/exoskeleton.md',
                   'norm': 'EXO-401',
                   'grant': 'Block-tag continuation content may be dropped from generated XML while certifying '
                            'that content preserved; entity source/file/location and relation relevance must '
                            'otherwise remain verified.',
                   'losses': ['E4', 'N4', 'D3']},
 'M5-association': {'path': 'code/doxygen.md',
                    'norm': 'DOXY-301',
                    'grant': 'For entities with complete retained substantive paragraphs and verified current '
                             'source/file/location, a shared dummy anchor alone may resolve an undisclosed '
                             'metadata collision as the requested entity.',
                    'losses': ['N4', 'D3']}}

# BUG_FIX_CONTEXT: PRE01-07: AST statement ends omit final comments; copied edges, confounded grants and label-only XML checks gave misleading evidence. Exact genuine comment spans, bounded source-known related sets, full own content and safe owned failure trajectories repair those causes.
# The formulas recognize precisely reviewed live clauses, not arbitrary ordinary-language equivalence.
# Example fences provide behavior evidence and are never substituted for owning normative supports.

# region FUNC__read_core_sources [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Bind complete sources to exact byte/mode identity before any fixture judgment.
## @uses pathlib.Path.read_bytes, pathlib.Path.stat, hashlib.sha256, stat.S_IMODE
## @io Input: root Path with the seven CORE_FILES readable UTF-8. Output: (sources dict[str,str], identities dict[str,dict]) with sha256/bytes/mode for every file.
##   Side effects: reads only actual named files, prints safe counts. Guarantees: complete original files and numeric modes, no inspected-tree writes.
##   Raises: OSError for unreadable source; UnicodeError for non-UTF-8. System importance: 8 for verified core evidence.
##   Example: _read_core_sources(root) returns all seven named source texts.
## @complexity 6
def _read_core_sources(root):
    # START_BLOCK_Read
    print("[IMP:4][_read_core_sources][Read] enter")
    sources, identities = {}, {}
    try:
        for relative in CORE_FILES:
            path = root / relative
            data = path.read_bytes()
            sources[relative] = data.decode("utf-8")
            identities[relative] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "mode": stat.S_IMODE(path.stat().st_mode)}
            print("[IMP:7][_read_core_sources][READ] subject=%s bytes=%d" % (relative, len(data)))
    except (OSError, UnicodeError) as error:
        print("[IMP:10][_read_core_sources][ERROR] kind=%s" % type(error).__name__)
        raise
    # END_BLOCK_Read
    # START_BLOCK_Result
    print("[IMP:4][_read_core_sources][Result] enter")
    print("[IMP:9][_read_core_sources][RESULT] complete=%d" % len(sources))
    return sources, identities
    # END_BLOCK_Result
# endregion FUNC__read_core_sources

# region FUNC__live_core_lines [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Separate live responsibility text from illustrative fenced examples.
## @uses re.match
## @io Input: text str with balanced Markdown fences. Output: list[str] preserving original live line order.
##   Side effects: safe count trace only. Guarantees: fenced text never supplies normative support.
##   Raises: ValueError for an unclosed fence. System importance: 8 for verified core evidence.
##   Example: _live_core_lines("plain") returns ["plain"].
## @complexity 6
def _live_core_lines(text):
    # START_BLOCK_Parse
    print("[IMP:4][_live_core_lines][Parse] enter")
    live, fence = [], ""
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if not fence:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = ""
            continue
        if not fence:
            live.append(line)
    # END_BLOCK_Parse
    # START_BLOCK_Validation
    print("[IMP:4][_live_core_lines][Validation] enter")
    if fence:
        print("[IMP:10][_live_core_lines][ERROR] unclosed fence")
        raise ValueError("unclosed fence")
    print("[IMP:9][_live_core_lines][RESULT] lines=%d" % len(live))
    return live
    # END_BLOCK_Validation
# endregion FUNC__live_core_lines

# region FUNC__core_failures [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Observe finite source-fixed support/force/contrary losses without claiming general semantic completeness.
## @uses test_code_core_protocols._live_core_lines, re.match
## @io Input: sources dict[str,str] containing complete named files. Output: set[str] of exact responsibility IDs refused.
##   Side effects: safe branch and refusal counts on stdout. Guarantees: same formula for shipped bytes, real full-file controls and restored bytes.
##   Raises: ValueError for ambiguous duplicate normative IDs or bad fences. System importance: 8 for verified core evidence.
##   Example: a complete positive source returns set(); all E3 support removed returns {"E3"}.
## @complexity 6
def _core_failures(sources):
    # START_BLOCK_Parse
    print("[IMP:4][_core_failures][Parse] enter")
    live, norms = {}, {}
    for relative, text in sources.items():
        lines = _live_core_lines(text)
        live[relative] = "\n".join(lines)
        norms[relative] = {}
        for line in lines:
            found = re.match(r"^- \*\*([A-Z]+-\d+)\*\* (MUST NOT|SHOULD NOT|MUST|SHOULD|MAY): (.+)$", line)
            if found:
                if found.group(1) in norms[relative]:
                    print("[IMP:10][_core_failures][ERROR] duplicate norm")
                    raise ValueError("duplicate norm")
                norms[relative][found.group(1)] = (found.group(2), found.group(3))
    # END_BLOCK_Parse
    # START_BLOCK_Judgment
    print("[IMP:4][_core_failures][Judgment] enter")
    failures = set()
    for key, duty in RESPONSIBILITIES.items():
        force, clause = norms.get(duty["path"], {}).get(duty["norm"], ("", ""))
        if not duty["norm"]:
            force, clause = "", live.get(duty["path"], "")
        complete = force == duty["force"] and any(all(part in clause for part in alternative) for alternative in duty["supports"])
        contrary = False
        for grant in RESPONSIBILITIES.values():
            if key in grant["contrary_losses"] and any(grant["contrary"] in live.get(path, "") for path in grant["contrary_paths"]):
                contrary = True
        for control in COMPOUND_CONTROLS.values():
            if key in control["losses"] and control["grant"] in live.get(control["path"], ""):
                contrary = True
        if not complete or contrary:
            failures.add(key)
            print("[IMP:9][_core_failures][REFUSAL] responsibility=%s complete=%s contrary=%s" % (key, complete, contrary))
    print("[IMP:9][_core_failures][RESULT] refusals=%d" % len(failures))
    return failures
    # END_BLOCK_Judgment
# endregion FUNC__core_failures

# region FUNC__materialize_fullfile_control [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Deliver exact whole-file candidate controls and source-bound restoration into owned absent scratch roots.
## @uses pathlib.Path.mkdir, pathlib.Path.write_bytes, pathlib.Path.chmod, pathlib.Path.read_bytes, hashlib.sha256, stat.S_IMODE
## @io Input: destination absent Path; complete sources/identities; edits tuple(path,old,new,positive exact count). Output: (readback dict[str,str], observed identities) for every complete file.
##   Side effects: writes only owned destination files, preserves numeric modes and prints readback counts. Guarantees: all reviewed replacement counts validated before writing; exact readback.
##   Raises: ValueError for existing destination or changed support population; OSError for failed delivery. System importance: 8 for verified core evidence.
##   Example: an empty edit list reproduces complete original bytes and modes.
## @complexity 6
def _materialize_fullfile_control(destination, sources, identities, edits):
    try:
        # START_BLOCK_Validation
        print("[IMP:4][_materialize_fullfile_control][Validation] enter")
        if destination.exists():
            print("[IMP:10][_materialize_fullfile_control][ERROR] destination exists")
            raise ValueError("control destination must be absent")
        changed = dict(sources)
        for relative, old, new, population in edits:
            actual = changed[relative].count(old)
            print("[IMP:9][_materialize_fullfile_control][TRIGGER] subject=%s count=%d" % (relative, actual))
            if actual != population:
                print("[IMP:10][_materialize_fullfile_control][ERROR] source support changed")
                raise ValueError("reviewed support population changed")
            changed[relative] = changed[relative].replace(old, new, population)
        # END_BLOCK_Validation
        # START_BLOCK_Delivery
        print("[IMP:4][_materialize_fullfile_control][Delivery] enter")
        readback, observed = {}, {}
        for relative, text in changed.items():
            path = destination / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(text.encode("utf-8"))
            path.chmod(identities[relative]["mode"])
            data = path.read_bytes()
            readback[relative] = data.decode("utf-8")
            observed[relative] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "mode": stat.S_IMODE(path.stat().st_mode)}
            print("[IMP:8][_materialize_fullfile_control][READBACK] subject=%s bytes=%d" % (relative, len(data)))
            assert readback[relative] == text and observed[relative]["mode"] == identities[relative]["mode"]
        print("[IMP:9][_materialize_fullfile_control][RESULT] files=%d" % len(readback))
        return readback, observed
        # END_BLOCK_Delivery
    # START_BLOCK_ErrorHandling
    except (OSError, UnicodeError, SyntaxError, ValueError, ET.ParseError, subprocess.SubprocessError, AssertionError) as error:
        print("[IMP:10][_materialize_fullfile_control][ErrorHandling] condition=owned_operation_failure kind=%s" % type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
# endregion FUNC__materialize_fullfile_control

# region FUNC__run_presence_example [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Exercise the actually extracted worked function through a real Python process and expose its delivered streams.
## @uses pathlib.Path.read_text, ast.parse, re.findall, pathlib.Path.write_text, subprocess.run, sys.executable
## @io Input: root readable protocol; owned destination; variant real/fixture/invalid; optional exact one-span replacement. Output: (source str, CompletedProcess) with actual stdout/stderr/exit.
##   Side effects: writes and executes owned specimen, prints actual captured child streams. Guarantees: one full extract; no installed-package assumption beyond observed real lookup.
##   Raises: ValueError for ambiguous specimen; SyntaxError for invalid source; OSError for process/file failure. System importance: 8 for verified core evidence.
##   Example: variant fixture preserves later keys after a ValueError.
## @complexity 6
def _run_presence_example(root, destination, variant="real", replacement=None):
    try:
        # START_BLOCK_Extraction
        print("[IMP:4][_run_presence_example][Extraction] enter")
        text = (root / "code/exoskeleton.md").read_text(encoding="utf-8")
        blocks = re.findall(r"```python\n(.*?)\n```", text, re.S)
        if len(blocks) != 1:
            print("[IMP:10][_run_presence_example][ERROR] specimen ambiguity")
            raise ValueError("one complete specimen required")
        source = blocks[0] + "\n"
        ast.parse(source, feature_version=(3, 9))
        if replacement:
            old, new = replacement
            assert source.count(old) == 1
            source = source.replace(old, new, 1)
        # END_BLOCK_Extraction
        # START_BLOCK_Delivery
        print("[IMP:4][_run_presence_example][Delivery] enter")
        driver = EXAMPLE_DRIVER.replace("VARIANT_TOKEN", repr(variant))
        destination.mkdir(parents=True, exist_ok=False)
        path = destination / "presence_check.py"
        path.write_text(source + driver, encoding="utf-8")
        print("[IMP:7][_run_presence_example][EXECUTE] variant=%s bytes=%d" % (variant, path.stat().st_size))
        result = subprocess.run([sys.executable, "-B", str(path)], cwd=destination, text=True, capture_output=True)
        if result.returncode:
            print("[IMP:10][_run_presence_example][Delivery] condition=child_exit_failure exit=%d" % result.returncode)
        else:
            print(result.stdout, end="")
            print(result.stderr, end="")
        print("[IMP:9][_run_presence_example][RESULT] variant=%s exit=%d" % (variant, result.returncode))
        return source, result
        # END_BLOCK_Delivery
    # START_BLOCK_ErrorHandling
    except (OSError, UnicodeError, SyntaxError, ValueError, ET.ParseError, subprocess.SubprocessError, AssertionError) as error:
        print("[IMP:10][_run_presence_example][ErrorHandling] condition=owned_operation_failure kind=%s" % type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
# endregion FUNC__run_presence_example

# region FUNC__source_entity_contracts [DOMAIN(8): Core; CONCEPT(9): CommentAssociation; TECH(7): AST]
## @purpose Bind complete own contract fields and properly nested comment steps to actual source definitions and enclosing regions.
##   Parse excludes literal spans before pairing region comments; Association binds field continuations and ordered logical steps to the actual definition, preventing AST statement-end truncation.
## @uses ast.parse, ast.walk, re.fullmatch
## @io Input: source str parseable under Python 3.9; aliases dict[str,str] from the actual Doxyfile titled aliases. Output: dict keyed by top-level function name, each with actual definition line, full region span, expected fields and logical-step coordinates.
##   Side effects: safe count/error-class trace only. Guarantees: literal text cannot supply comment markers; matching ordered names and indentation, closing steps inside the exact function region, full own field continuations retained.
##   Raises: SyntaxError for invalid Python; ValueError for missing/crossed/duplicate regions, incorrect nesting or incomplete field aliases. System importance: 9 for source and XML provenance.
##   Example: a trailing END_BLOCK comment before its function endregion remains part of that function, even after its final return.
## @complexity 9
def _source_entity_contracts(source, aliases):
    try:
        # START_BLOCK_Parse
        print("[IMP:4][_source_entity_contracts][Parse] enter")
        tree = ast.parse(source, feature_version=(3, 9))
        lines = source.splitlines()
        literals = [(n.lineno, n.col_offset, n.end_lineno, n.end_col_offset) for n in ast.walk(tree) if isinstance(n, (ast.Constant, ast.JoinedStr)) and (isinstance(n, ast.JoinedStr) or isinstance(n.value, str))]
        comments = {}
        for number, text in enumerate(lines, 1):
            column = len(text) - len(text.lstrip())
            if not text.lstrip().startswith("#"):
                continue
            in_literal = any(start <= number <= end and (number > start or column >= start_col) and (number < end or column < end_col) for start, start_col, end, end_col in literals)
            if not in_literal:
                comments[number] = (column, text.lstrip())
        regions, stack = {}, []
        for number, (column, comment) in comments.items():
            opening = re.fullmatch(r"# region (\w+)(?: .*|)", comment)
            closing = re.fullmatch(r"# endregion (\w+)", comment)
            if opening:
                stack.append((opening.group(1), column, number))
            elif closing:
                if not stack or stack[-1][:2] != (closing.group(1), column):
                    raise ValueError("region nesting mismatch")
                name, indent, start = stack.pop()
                if name in regions:
                    raise ValueError("duplicate region")
                regions[name] = (start, number, indent)
        if stack:
            raise ValueError("unclosed region")
        # END_BLOCK_Parse
        # START_BLOCK_Association
        print("[IMP:4][_source_entity_contracts][Association] enter")
        entities = {}
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            region_name = "MODULE_CONTRACT" if node.name == "_module_contract" else "FUNC_" + node.name
            if region_name not in regions:
                raise ValueError("function region absent")
            start, end, indent = regions[region_name]
            if not (start < node.lineno <= node.end_lineno < end) or indent != node.col_offset:
                raise ValueError("function containment mismatch")
            fields, active = {}, None
            for number in range(start + 1, node.lineno):
                if number not in comments:
                    continue
                _, comment = comments[number]
                tag = re.fullmatch(r"## @(\w+)(?: (.*))?", comment)
                if tag:
                    active = tag.group(1)
                    if active == "modulecontract":
                        active = None
                        continue
                    if active not in aliases or aliases[active] in fields:
                        raise ValueError("field alias absent or duplicate")
                    fields[aliases[active]] = [tag.group(2) or ""]
                elif active and comment.startswith("##"):
                    content = comment[2:].strip()
                    if content.startswith("- "):
                        content = content[2:]
                    fields[aliases[active]].append(content)
            expected = {title: " ".join(" ".join(parts).split()) for title, parts in fields.items()}
            if not expected or any(not value for value in expected.values()):
                raise ValueError("empty own contract field")
            steps, blocks = [], []
            for number in range(node.lineno + 1, end):
                if number not in comments:
                    continue
                column, comment = comments[number]
                block = re.fullmatch(r"# (START|END)_BLOCK_(\w+)", comment)
                if not block:
                    continue
                kind, block_name = block.groups()
                if column <= node.col_offset:
                    raise ValueError("block outside function indentation")
                if kind == "START":
                    if blocks and column < blocks[-1][1]:
                        raise ValueError("logical step nesting indentation mismatch")
                    blocks.append((block_name, column, number))
                else:
                    if not blocks or blocks[-1][:2] != (block_name, column):
                        raise ValueError("logical step nesting mismatch")
                    opening_name, opening_column, opening_line = blocks.pop()
                    steps.append({"name": opening_name, "start": opening_line, "end": number, "indent": opening_column})
            if blocks or (node.name != "_module_contract" and not steps):
                raise ValueError("logical step closure absent")
            entities[node.name] = {"line": node.lineno, "region": [start, end], "fields": expected, "steps": steps}
        for number, (column, comment) in comments.items():
            if re.fullmatch(r"# (START|END)_BLOCK_\w+", comment) and not any(entity["line"] < number < entity["region"][1] for entity in entities.values()):
                raise ValueError("logical step outside function region")
        print("[IMP:9][_source_entity_contracts][RESULT] entities=%d" % len(entities))
        return entities
        # END_BLOCK_Association
    # START_BLOCK_ErrorHandling
    except (SyntaxError, ValueError) as error:
        print("[IMP:10][_source_entity_contracts][ErrorHandling] condition=source_contract_failure kind=%s" % type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
# endregion FUNC__source_entity_contracts

# region FUNC__read_map_entity [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Read only a current requested entity's own XML/location/fields and expose unavailable association.
## @uses test_code_core_protocols._source_entity_contracts, pathlib.Path.stat, pathlib.Path.read_bytes, pathlib.Path.read_text, xml.etree.ElementTree.parse, hashlib.sha256, re.findall
## @io Input: xml_dir Path; relative source path; name str; positive definition line int; optional actual source_root Path (default configured test-map parent). Output: dict with FOUND and own fields/location/owner, or GAP with precise reason.
##   Side effects: bounded index/relevant compound, source and actual Doxyfile reads and safe trace. Guarantees: all own titled fields and continuations compare with current source-bound content; no sibling paragraph substitution; ambiguity, content mismatch or broken XML refuses.
##   Raises: no propagated read/parse/stat/configuration error; XML/OSError/Unicode/Syntax/invalid-contract conditions return GAP. System importance: 8 for verified core evidence.
##   Example: absent index returns {status:GAP,reason:no index}.
## @complexity 6
def _read_map_entity(xml_dir, relative, name, line, source_root=None):
    try:
        # START_BLOCK_Index
        print("[IMP:4][_read_map_entity][Index] enter")
        index = xml_dir / "index.xml"
        if not index.is_file():
            print("[IMP:9][_read_map_entity][GAP] no index")
            return {"status": "GAP", "reason": "no index"}
        # START_BLOCK_SourceBinding
        print("[IMP:7][_read_map_entity][SourceBinding] bind actual source and all own fields")
        actual_root = xml_dir.parent.parent if source_root is None else source_root
        source_path = actual_root / relative
        if not source_path.is_file():
            print("[IMP:9][_read_map_entity][GAP] actual source unbound")
            return {"status": "GAP", "reason": "actual source unbound"}
        if source_path.stat().st_mtime > index.stat().st_mtime:
            print("[IMP:9][_read_map_entity][GAP] source newer than index")
            return {"status": "GAP", "reason": "source newer than index"}
        source_bytes = source_path.read_bytes()
        configuration = (actual_root / "Doxyfile").read_text(encoding="utf-8")
        aliases = {tag: title for tag, title in re.findall(r'"(\w+)=@par ([^"^]+)(?:\^\^)?"', configuration) if tag != "modulecontract"}
        contracts = _source_entity_contracts(source_bytes.decode("utf-8"), aliases)
        if name not in contracts or contracts[name]["line"] != line:
            print("[IMP:9][_read_map_entity][GAP] current source definition mismatch")
            return {"status": "GAP", "reason": "current source definition mismatch"}
        expected = contracts[name]["fields"]
        # END_BLOCK_SourceBinding
        tree = ET.parse(index).getroot()
        owner_ids = [c.get("refid") for c in tree.findall("compound") if any(m.findtext("name") == name for m in c.findall("member"))]
        matches = []
        for owner in owner_ids:
            if not isinstance(owner, str) or not owner or "/" in owner or "\\" in owner or owner in (".", ".."):
                print("[IMP:10][_read_map_entity][Index] condition=invalid_compound_refid")
                return {"status": "GAP", "reason": "invalid compound reference"}
            compound = ET.parse(xml_dir / (owner + ".xml")).getroot()
            for member in compound.findall(".//memberdef"):
                location = member.find("location")
                if member.findtext("name") == name and location is not None and location.get("file") == relative and int(location.get("line", "0")) == line:
                    detailed = member.find("detaileddescription")
                    fields = {} if detailed is None else {s.findtext("title"): " ".join(" ".join("".join(p.itertext()).split()) for p in s.findall("para")) for s in detailed.findall(".//simplesect[@kind='par']")}
                    matches.append({"status": "FOUND", "fields": fields, "location": dict(location.attrib), "owner": owner, "source_sha256": hashlib.sha256(source_bytes).hexdigest(), "source_fields": expected})
        # END_BLOCK_Index
        # START_BLOCK_Validation
        print("[IMP:4][_read_map_entity][Validation] enter")
        if len(matches) != 1 or not matches[0]["fields"]:
            print("[IMP:9][_read_map_entity][GAP] own matching entities=%d" % len(matches))
            return {"status": "GAP", "reason": "own entity association absent or ambiguous"}
        missing = [title for title, content in expected.items() if " ".join(matches[0]["fields"].get(title, "").split()) != content]
        if missing:
            print("[IMP:9][_read_map_entity][GAP] current own content mismatches=%d" % len(missing))
            return {"status": "GAP", "reason": "current own substantive content mismatch"}
        print("[IMP:9][_read_map_entity][RESULT] fields=%d content_bound=true" % len(expected))
        return matches[0]
        # END_BLOCK_Validation
    # START_BLOCK_ErrorHandling
    except (ET.ParseError, OSError, UnicodeError, SyntaxError, ValueError) as error:
        print("[IMP:10][_read_map_entity][ErrorHandling] condition=map_evidence_failure kind=%s" % type(error).__name__)
        return {"status": "GAP", "reason": type(error).__name__}
    # END_BLOCK_ErrorHandling
# endregion FUNC__read_map_entity

# region FUNC_test_core_source_fixed_controls [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Verify positive/loss/contrary/compound/restoration decisions on complete physical files.
## @uses test_code_core_protocols._read_core_sources, test_code_core_protocols._core_failures, test_code_core_protocols._materialize_fullfile_control
## @io Input: repo_root Path with complete readable current core sources; tmp_path owned existing Path with absent control leaves. Output: None after positive, redundant, true-loss, bounded contrary, compound and restoration assertions.
##   Side effects: delivers complete owned control files and numeric modes, reads them back, prints actual safe observations. Guarantees: source-fixed related sets precede observer results; all complete non-target supports/alternatives and untouched full files retained.
##   Raises: AssertionError for exact expected reason/retention/restoration mismatch; OSError/UnicodeError for source or control delivery failure; ValueError for changed supports, duplicate norms or unclosed fences. System importance: 8 for verified core evidence.
##   Example: invoke test_core_source_fixed_controls with its named native pytest fixtures to observe its actual stated duty.
## @complexity 6
def test_core_source_fixed_controls(repo_root, tmp_path):
    try:
        # START_BLOCK_Positive
        print("[IMP:4][test_core_source_fixed_controls][Positive] enter")
        sources, identities = _read_core_sources(repo_root)
        assert _core_failures(sources) == set()
        # END_BLOCK_Positive
        # START_BLOCK_ControlMatrix
        print("[IMP:4][test_core_source_fixed_controls][ControlMatrix] enter")
        for key, duty in RESPONSIBILITIES.items():
            original = duty["supports"][0][0]
            if len(duty["supports"]) > 1:
                redundant, _ = _materialize_fullfile_control(tmp_path / (key + "-redundant"), sources, identities, [(duty["path"], original, "", 1)])
                print("[IMP:9][test_core_source_fixed_controls][REDUNDANT] key=%s complete alternative retained" % key)
                assert _core_failures(redundant) == set()
            loss_edits = [(duty["path"], alternative[0], "", 1) for alternative in duty["supports"]]
            for kind, edits in (("loss", loss_edits), ("contrary", [(duty["path"], original, original + " " + duty["contrary"], 1)])):
                candidate, actual = _materialize_fullfile_control(tmp_path / (key + "-" + kind), sources, identities, edits)
                observed = _core_failures(candidate)
                print("[IMP:9][test_core_source_fixed_controls][OBSERVED] key=%s kind=%s refusals=%s" % (key, kind, sorted(observed)))
                expected = set(duty["loss_losses"] if kind == "loss" else duty["contrary_losses"])
                assert observed == expected
                for retained in set(RESPONSIBILITIES) - expected:
                    other = RESPONSIBILITIES[retained]
                    assert any(all(part in candidate[other["path"]] for part in alternative) for alternative in other["supports"])
                restored, restored_ids = _materialize_fullfile_control(tmp_path / (key + "-" + kind + "-restored"), sources, identities, [])
                assert restored_ids == identities and _core_failures(restored) == set()
        # END_BLOCK_ControlMatrix
        # START_BLOCK_CompoundControls
        print("[IMP:4][test_core_source_fixed_controls][CompoundControls] enter")
        for name, control in COMPOUND_CONTROLS.items():
            original = next(d["supports"][0][0] for d in RESPONSIBILITIES.values() if d["path"] == control["path"] and d["norm"] == control["norm"])
            candidate, _ = _materialize_fullfile_control(tmp_path / name, sources, identities, [(control["path"], original, original + " " + control["grant"], 1)])
            observed = _core_failures(candidate)
            print("[IMP:9][test_core_source_fixed_controls][COMPOUND] id=%s losses=%s" % (name, sorted(observed)))
            assert observed == set(control["losses"])
            for relative in CORE_FILES:
                if relative != control["path"]:
                    assert candidate[relative] == sources[relative]
            assert all(d["supports"][0][0] in candidate[d["path"]] for d in RESPONSIBILITIES.values())
        # END_BLOCK_CompoundControls
    # START_BLOCK_ErrorHandling
    except (OSError, UnicodeError, SyntaxError, ValueError, ET.ParseError, subprocess.SubprocessError, AssertionError) as error:
        print("[IMP:10][test_core_source_fixed_controls][ErrorHandling] condition=owned_operation_failure kind=%s" % type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
# endregion FUNC_test_core_source_fixed_controls

# region FUNC_test_core_presence_example_and_trajectory [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Discriminate actual sample outcomes and safe successful/failing trace.
## @uses test_code_core_protocols._run_presence_example, json.loads, test_code_core_protocols._read_core_sources, test_code_core_protocols._materialize_fullfile_control, pathlib.Path.write_text, sys.executable
## @io Input: repo_root Path with one complete parseable worked module; tmp_path owned Path with absent process/specimen leaves. Output: None after real/fixture/invalid/provider/container/discrimination and owned error-path assertions.
##   Side effects: writes actual owned specimens/error fixtures, executes the real Python child, delivers its safe streams, temporarily selects an absent executable and restores sys.executable in finally. Guarantees: later keys and all target outcomes survive per-item failure; supplied provider effects remain caller-owned.
##   Raises: AssertionError for wrong sample outcome/trace/refusal or missing expected error; OSError for unforeseen source/file/process failure; SyntaxError for unforeseen specimen AST failure; ValueError for ambiguous extract; declared helper failures propagate after safe own IMP10. System importance: 8 for verified core evidence.
##   Example: invoke test_core_presence_example_and_trajectory with its named native pytest fixtures to observe its actual stated duty.
## @complexity 6
def test_core_presence_example_and_trajectory(repo_root, tmp_path):
    try:
        # START_BLOCK_Behavior
        print("[IMP:4][test_core_presence_example_and_trajectory][Behavior] enter")
        for variant, expected in (("real", {"math": True, "missing_core_example_93842": False, "bad.name": False}), ("fixture", {"present": True, "missing": False, "broken": False, "later": True, "bad.name": False})):
            source, result = _run_presence_example(repo_root, tmp_path / variant, variant)
            assert result.returncode == 0
            payload = json.loads(result.stdout.splitlines()[-1])
            assert payload == expected
            assert "VALIDATION_SUCCESS" in result.stderr and "[RESULT] found=%d total=%d" % (sum(expected.values()), len(expected)) in result.stderr
            assert "[LOOKUP]" in result.stderr and "[CHECK]" in result.stderr and "[UNSUPPORTED]" in result.stderr
            if variant == "fixture":
                assert "[CHECK_FAILURE] item=2 kind=ValueError found=false" in result.stderr
                assert "[CHECK] item=3 found=True" in result.stderr
            assert "SECRET_EXCEPTION_PAYLOAD" not in result.stderr
        _, invalid = _run_presence_example(repo_root, tmp_path / "invalid", "invalid")
        assert invalid.returncode == 0 and json.loads(invalid.stdout.splitlines()[-1]) == {"error": "ValueError"}
        assert "[VALIDATION_FAILURE]" in invalid.stderr and "[LOOKUP]" not in invalid.stderr
        for variant, marker in (("invalid-container", "CONTAINER_FAILURE"), ("invalid-provider", "PROVIDER_FAILURE")):
            _, rejected = _run_presence_example(repo_root, tmp_path / variant, variant)
            print("[IMP:9][test_core_presence_example_and_trajectory][INPUT_REFUSAL] variant=%s exit=%d" % (variant, rejected.returncode))
            assert rejected.returncode == 0 and json.loads(rejected.stdout.splitlines()[-1]) == {"error": "TypeError"}
            assert "[IMP:10][check_all_libraries][" + marker + "]" in rejected.stderr
            assert "[LOOKUP]" not in rejected.stderr and "[RESULT]" not in rejected.stderr
        # END_BLOCK_Behavior
        # START_BLOCK_Discrimination
        print("[IMP:4][test_core_presence_example_and_trajectory][Discrimination] enter")
        _, mutant = _run_presence_example(repo_root, tmp_path / "mutant", "fixture", ("result_map[key] = finder(key) is not None", "result_map[key] = False"))
        assert mutant.returncode == 0
        assert json.loads(mutant.stdout.splitlines()[-1]) != {"present": True, "missing": False, "broken": False, "later": True, "bad.name": False}
        assert "[CHECK_FAILURE]" not in mutant.stderr
        # END_BLOCK_Discrimination
        # START_BLOCK_OwnFailures
        print("[IMP:4][test_core_presence_example_and_trajectory][OwnFailures] enter")
        invalid_root = tmp_path / "invalid-source"
        (invalid_root / "code").mkdir(parents=True)
        (invalid_root / "code/exoskeleton.md").write_text("```python\ndef broken(\n```\n", encoding="utf-8")
        for root, destination, expected in ((tmp_path / "missing-source", tmp_path / "missing-result", FileNotFoundError), (invalid_root, tmp_path / "invalid-result", SyntaxError)):
            caught = False
            try:
                _run_presence_example(root, destination)
            except expected:
                caught = True
            assert caught
        blocked = tmp_path / "delivery-parent-file"
        blocked.write_text("owned boundary", encoding="utf-8")
        caught = False
        try:
            _read_core_sources(tmp_path / "missing-core-root")
        except FileNotFoundError:
            caught = True
        assert caught
        sources, identities = _read_core_sources(repo_root)
        caught = False
        try:
            _materialize_fullfile_control(blocked / "child", sources, identities, [])
        except OSError:
            caught = True
        assert caught
        executable = sys.executable
        try:
            sys.executable = str(tmp_path / "absent-python-executable")
            caught = False
            try:
                _run_presence_example(repo_root, tmp_path / "process-failure")
            except OSError:
                caught = True
            assert caught
        finally:
            sys.executable = executable
        # END_BLOCK_OwnFailures
    # START_BLOCK_ErrorHandling
    except (OSError, UnicodeError, SyntaxError, ValueError, ET.ParseError, subprocess.SubprocessError, AssertionError) as error:
        print("[IMP:10][test_core_presence_example_and_trajectory][ErrorHandling] condition=owned_operation_failure kind=%s" % type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
# endregion FUNC_test_core_presence_example_and_trajectory

# region FUNC_test_core_map_identity_and_paragraphs [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Build actual XML and bind each authored function's own rich paragraphs to current source/location.
## @uses test_code_core_protocols._read_map_entity, test_code_core_protocols._source_entity_contracts, subprocess.run, ast.parse, xml.etree.ElementTree.parse, xml.etree.ElementTree.fromstring, hashlib.sha256, re.findall, re.search
## @io Input: repo_root Path with current actual source; repo_copy Path containing a complete owned same-source copy and actual Doxyfile; tmp_path owned Path for the label-retaining negative. Output: None after current own source/location/full-field/continuation/XML and negative assertions.
##   Side effects: runs real Doxygen in repo_copy, reads actual current index/relevant compounds, delivers a complete index/compound negative retaining location/labels, prints safe observations. Guarantees: every own expected field is extracted from current source before XML judgment; shared launcher metadata ambiguity stays disclosed.
##   Raises: AssertionError for build/streams/freshness/identity/full-content/negative mismatch; OSError/UnicodeError for actual file/process failure; SyntaxError for invalid current source; ET.ParseError for broken actual XML; ValueError for invalid own source contracts/locations. System importance: 8 for verified core evidence.
##   Example: invoke test_core_map_identity_and_paragraphs with its named native pytest fixtures to observe its actual stated duty.
## @complexity 6
def test_core_map_identity_and_paragraphs(repo_root, repo_copy, tmp_path):
    try:
        # START_BLOCK_Build
        print("[IMP:4][test_core_map_identity_and_paragraphs][Build] enter")
        print("[IMP:7][test_core_map_identity_and_paragraphs][BUILD] actual scoped copy")
        result = subprocess.run(["doxygen", "Doxyfile"], cwd=repo_copy, capture_output=True, text=True)
        print("[IMP:9][test_core_map_identity_and_paragraphs][RESULT] exit=%d" % result.returncode)
        assert result.returncode == 0 and result.stdout == "" and result.stderr == ""
        xml_dir = repo_copy / "doxygen_output/xml"
        index_time = (xml_dir / "index.xml").stat().st_mtime
        covered = list((repo_copy / "tools").rglob("*.py")) + list((repo_copy / "tests").rglob("*.py")) + [repo_copy / "bin/conform"]
        assert all(path.stat().st_mtime <= index_time for path in covered if "__pycache__" not in path.parts)
        # END_BLOCK_Build
        # START_BLOCK_Association
        print("[IMP:4][test_core_map_identity_and_paragraphs][Association] enter")
        relative = "tests/test_code_core_protocols.py"
        source = (repo_copy / relative).read_text(encoding="utf-8")
        assert source == (repo_root / relative).read_text(encoding="utf-8")
        tree = ast.parse(source)
        configuration = (repo_copy / "Doxyfile").read_text(encoding="utf-8")
        aliases = {tag: title for tag, title in re.findall(r'"(\w+)=@par ([^"^]+)(?:\^\^)?"', configuration) if tag != "modulecontract"}
        source_contracts = _source_entity_contracts(source, aliases)
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                observed = _read_map_entity(xml_dir, relative, node.name, node.lineno)
                assert observed["status"] == "FOUND"
                fields = observed["fields"]
                assert fields and observed["source_sha256"] == hashlib.sha256(source.encode("utf-8")).hexdigest()
                assert observed["source_fields"] == source_contracts[node.name]["fields"]
                for title, expected in source_contracts[node.name]["fields"].items():
                    assert " ".join(fields[title].split()) == expected
        negative_dir = tmp_path / "label-retaining-map"
        negative_dir.mkdir()
        index_bytes = (xml_dir / "index.xml").read_bytes()
        (negative_dir / "index.xml").write_bytes(index_bytes)
        victim = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "_read_core_sources")
        index = ET.fromstring(index_bytes)
        owners = [c.get("refid") for c in index.findall("compound") if any(m.findtext("name") == victim.name for m in c.findall("member"))]
        for owner in owners:
            xml = ET.parse(xml_dir / (owner + ".xml"))
            for member in xml.findall(".//memberdef"):
                location = member.find("location")
                if member.findtext("name") == victim.name and location is not None and location.get("file") == relative and int(location.get("line", "0")) == victim.lineno:
                    io = member.find("detaileddescription").find(".//simplesect[@kind='par'][title='I/O:']")
                    for paragraph in io.findall("para"):
                        paragraph.clear()
                        paragraph.text = "Input: Output: Side effects: Guarantees: Raises: System importance: Example:"
            xml.write(negative_dir / (owner + ".xml"), encoding="utf-8")
        refused = _read_map_entity(negative_dir, relative, victim.name, victim.lineno, repo_copy)
        print("[IMP:9][test_core_map_identity_and_paragraphs][MISSING_CONTENT] status=%s" % refused["status"])
        assert refused == {"status": "GAP", "reason": "current own substantive content mismatch"}
        launcher = (repo_copy / "bin/conform").read_text(encoding="utf-8")
        launch = next(n for n in ast.parse(launcher).body if isinstance(n, ast.FunctionDef) and n.name == "launch")
        launcher_index = ET.parse(xml_dir / "index.xml").getroot()
        launcher_owners = [c.get("refid") for c in launcher_index.findall("compound") if any(m.findtext("name") == "launch" for m in c.findall("member"))]
        launch_locations = []
        for owner in launcher_owners:
            for member in ET.parse(xml_dir / (owner + ".xml")).findall(".//memberdef"):
                location = member.find("location")
                if member.findtext("name") == "launch" and location is not None and location.get("file") == "bin/conform" and int(location.get("line", "0")) == launch.lineno:
                    launch_locations.append(dict(location.attrib))
        assert len(launch_locations) == 1
        merged = ET.parse(xml_dir / "namespaceconform.xml").getroot()
        metadata = [m for m in merged.findall(".//memberdef") if m.findtext("name") == "_module_contract"]
        assert metadata
        launcher_purpose = re.search(r"## @purpose (.*?)\n## @scope", launcher, re.S).group(1)
        normalized_purpose = " ".join(re.sub(r"\n##\s*", " ", launcher_purpose).split())
        combined = " ".join(" ".join(m.itertext()) for m in metadata)
        assert normalized_purpose in " ".join(combined.split())
        print("[IMP:9][test_core_map_identity_and_paragraphs][QUALIFIED] shared conform metadata collision disclosed; launch source/location and own purpose pinned")
        # END_BLOCK_Association
    # START_BLOCK_ErrorHandling
    except (OSError, UnicodeError, SyntaxError, ValueError, ET.ParseError, subprocess.SubprocessError, AssertionError) as error:
        print("[IMP:10][test_core_map_identity_and_paragraphs][ErrorHandling] condition=owned_operation_failure kind=%s" % type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
# endregion FUNC_test_core_map_identity_and_paragraphs

# region FUNC_test_core_navigation_evidence_limits [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Refuse absent/broken/neighbor map evidence and prove only narrow configured absence.
## @uses test_code_core_protocols._read_map_entity, pathlib.Path.write_text, os.utime, re.search
## @io Input: repo_root Path with actual Doxyfile; tmp_path owned existing Path for real marked source and XML evidence carriers. Output: None after absent/neighbor/broken/missing-compound/invalid-source/stale GAP and narrow configured absence assertions.
##   Side effects: writes owned source/config/XML fixtures, removes only its own deliberately missing compound, advances only its own source time, reads actual FILE_PATTERNS. Guarantees: each unavailable-evidence trigger has its own actual carrier and precise reason; configured JSON exclusion grants only narrow XML-membership N/A.
##   Raises: AssertionError for wrong actual GAP/reason or incorrect bounded exclusion; OSError/UnicodeError for unexpected fixture/config delivery/read failure; map helper handles its declared source/XML/stat failures as GAP. System importance: 8 for verified core evidence.
##   Example: invoke test_core_navigation_evidence_limits with its named native pytest fixtures to observe its actual stated duty.
## @complexity 6
def test_core_navigation_evidence_limits(repo_root, tmp_path):
    try:
        # START_BLOCK_Unknown
        print("[IMP:4][test_core_navigation_evidence_limits][Unknown] enter")
        assert _read_map_entity(tmp_path / "absent", "sample.py", "f", 1)["status"] == "GAP"
        source_root = tmp_path / "source-root"
        source_root.mkdir()
        (source_root / "Doxyfile").write_bytes((repo_root / "Doxyfile").read_bytes())
        specimen = "# region FUNC_f [DOMAIN(1): Fixture]\n## @purpose Own fixture purpose.\n## @uses None: pure literal return.\n## @io Input: none. Output: int. Side effects: none. Guarantees: literal one. Raises: none. System importance: 1. Example: f() returns 1.\n## @complexity 1\ndef f():\n    # START_BLOCK_Result\n    return 1\n    # END_BLOCK_Result\n# endregion FUNC_f\n"
        (source_root / "sample.py").write_text(specimen, encoding="utf-8")
        xml_dir = tmp_path / "partial"
        xml_dir.mkdir()
        index_text = '<doxygenindex><compound refid="sample"><member><name>f</name></member></compound></doxygenindex>'
        (xml_dir / "index.xml").write_text(index_text, encoding="utf-8")
        (xml_dir / "sample.xml").write_text('<doxygen><compounddef><memberdef><name>f</name><location file="other.py" line="6"/><detaileddescription><simplesect kind="par"><title>Purpose:</title><para>Neighbor purpose.</para></simplesect></detaileddescription></memberdef></compounddef></doxygen>', encoding="utf-8")
        neighbor = _read_map_entity(xml_dir, "sample.py", "f", 6, source_root)
        assert neighbor == {"status": "GAP", "reason": "own entity association absent or ambiguous"}
        (xml_dir / "sample.xml").write_text("<broken", encoding="utf-8")
        assert _read_map_entity(xml_dir, "sample.py", "f", 6, source_root) == {"status": "GAP", "reason": "ParseError"}
        (xml_dir / "sample.xml").unlink()
        assert _read_map_entity(xml_dir, "sample.py", "f", 6, source_root) == {"status": "GAP", "reason": "FileNotFoundError"}
        (source_root / "sample.py").write_text("def invalid(\n", encoding="utf-8")
        (xml_dir / "index.xml").write_text(index_text, encoding="utf-8")
        assert _read_map_entity(xml_dir, "sample.py", "f", 6, source_root) == {"status": "GAP", "reason": "SyntaxError"}
        (source_root / "sample.py").write_text(specimen, encoding="utf-8")
        (xml_dir / "index.xml").write_text(index_text, encoding="utf-8")
        newer = (xml_dir / "index.xml").stat().st_mtime + 1
        os.utime(source_root / "sample.py", (newer, newer))
        stale = _read_map_entity(xml_dir, "sample.py", "f", 6, source_root)
        print("[IMP:9][test_core_navigation_evidence_limits][STALE] status=%s" % stale["status"])
        assert stale == {"status": "GAP", "reason": "source newer than index"}
        # END_BLOCK_Unknown
        # START_BLOCK_NarrowAbsence
        print("[IMP:4][test_core_navigation_evidence_limits][NarrowAbsence] enter")
        configuration = (repo_root / "Doxyfile").read_text(encoding="utf-8")
        assert re.search(r"^FILE_PATTERNS\s*=\s*\*\.py conform$", configuration, re.M)
        assert not pathlib.Path("tests/.test_counter.json").match("*.py")
        print("[IMP:9][test_core_navigation_evidence_limits][N_A] json counter excluded from this Python map by actual FILE_PATTERNS; no wider map exemption")
        # END_BLOCK_NarrowAbsence
    # START_BLOCK_ErrorHandling
    except (OSError, UnicodeError, SyntaxError, ValueError, ET.ParseError, subprocess.SubprocessError, AssertionError) as error:
        print("[IMP:10][test_core_navigation_evidence_limits][ErrorHandling] condition=owned_operation_failure kind=%s" % type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
# endregion FUNC_test_core_navigation_evidence_limits

# region FUNC_test_core_profile_and_migration_contract [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Check invoked rich step/profile structure and bounded specimen AST equality without migration claim.
## @uses test_code_core_protocols._source_entity_contracts, test_code_core_protocols._read_core_sources, test_code_core_protocols._core_failures, ast.parse, ast.dump, re.findall
## @io Input: repo_root Path with actual core/Doxyfile; own current module source readable as Python 3.9. Output: None after exact real comment-region/step/field source association and bounded worked-specimen AST equality assertions.
##   Side effects: reads current source/config and evaluates owned in-memory valid/malformed source carriers, safe trace only. Guarantees: AST string literals cannot forge comments; closures after final executable statements remain inside exact regions; no COMMENT-token/multi-interpreter migration proof or execution is claimed.
##   Raises: AssertionError for positive association, malformed-carrier refusal or AST-equivalence mismatch; OSError/UnicodeError for source/config reads; SyntaxError/ValueError for unexpected invalid current source/contract; intended malformed source ValueErrors are observed separately. System importance: 8 for verified core evidence.
##   Example: invoke test_core_profile_and_migration_contract with its named native pytest fixtures to observe its actual stated duty.
## @complexity 6
def test_core_profile_and_migration_contract(repo_root):
    try:
        # START_BLOCK_Profile
        print("[IMP:4][test_core_profile_and_migration_contract][Profile] enter")
        sources, _ = _read_core_sources(repo_root)
        assert _core_failures(sources) == set()
        source = pathlib.Path(__file__).read_text(encoding="utf-8")
        tree = ast.parse(source, feature_version=(3, 9))
        assert ast.get_docstring(tree) is None
        prefix = source.split("def _module_contract", 1)[0]
        tags = re.findall(r"^## @([A-Za-z_]+)", prefix, re.M)
        assert tags[-2:] == ["GREP_SUMMARY", "STRUCTURE"]
        configuration = (repo_root / "Doxyfile").read_text(encoding="utf-8")
        aliases = {tag: title for tag, title in re.findall(r'"(\w+)=@par ([^"^]+)(?:\^\^)?"', configuration) if tag != "modulecontract"}
        contracts = _source_entity_contracts(source, aliases)
        assert set(contracts) == {n.name for n in tree.body if isinstance(n, ast.FunctionDef)}
        for name, contract in contracts.items():
            if name != "_module_contract":
                assert contract["steps"] and all(contract["region"][0] < s["start"] < s["end"] < contract["region"][1] for s in contract["steps"])
        specimen = "# region FUNC_f [DOMAIN(1): Fixture]\n## @purpose Keep genuine comments associated.\n## @uses None: pure literal return.\n## @io Input: none. Output: str.\n## @complexity 1\ndef f():\n    # START_BLOCK_Result\n    value = \"\"\"# END_BLOCK_Result\n# endregion FUNC_f\n\"\"\"\n    return value\n    # END_BLOCK_Result\n# endregion FUNC_f\n"
        assert _source_entity_contracts(specimen, aliases)["f"]["steps"][0]["end"] == 12
        malformed = (
            specimen.replace("    # END_BLOCK_Result\n# endregion FUNC_f", "# endregion FUNC_f\n    # END_BLOCK_Result"),
            specimen.replace("    # END_BLOCK_Result\n# endregion FUNC_f", "    # END_BLOCK_Other\n# endregion FUNC_f"),
            specimen.replace("    # END_BLOCK_Result\n# endregion FUNC_f", "        # END_BLOCK_Result\n# endregion FUNC_f"),
            specimen.replace("    # START_BLOCK_Result", "    # START_BLOCK_Result\n    # START_BLOCK_Inner").replace("    # END_BLOCK_Result\n# endregion FUNC_f", "    # END_BLOCK_Result\n    # END_BLOCK_Inner\n# endregion FUNC_f"),
        )
        for candidate in malformed:
            rejected = False
            try:
                _source_entity_contracts(candidate, aliases)
            except ValueError:
                rejected = True
            assert rejected
        # END_BLOCK_Profile
        # START_BLOCK_BoundedAST
        print("[IMP:4][test_core_profile_and_migration_contract][BoundedAST] enter")
        example = re.findall(r"```python\n(.*?)\n```", sources["code/exoskeleton.md"], re.S)[0]
        renamed_comment = example.replace("# START_BLOCK_Result", "# START_BLOCK_FinalResult").replace("# END_BLOCK_Result", "# END_BLOCK_FinalResult")
        assert ast.dump(ast.parse(example)) == ast.dump(ast.parse(renamed_comment))
        print("[IMP:9][test_core_profile_and_migration_contract][LIMIT] specimen AST equality only; no COMMENT-token/multi-interpreter migration execution or authorization")
        # END_BLOCK_BoundedAST
    # START_BLOCK_ErrorHandling
    except (OSError, UnicodeError, SyntaxError, ValueError, ET.ParseError, subprocess.SubprocessError, AssertionError) as error:
        print("[IMP:10][test_core_profile_and_migration_contract][ErrorHandling] condition=owned_operation_failure kind=%s" % type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
# endregion FUNC_test_core_profile_and_migration_contract

# region FUNC_test_core_guide_direct_mapping [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Validate the actual adjacent AC mapping against real test definitions.
## @uses pathlib.Path.read_text, ast.parse, re.findall
## @io Input: repo_root Path with readable actual test guide; own current module source readable Python. Output: None after each AC-CORE-1 through 8 row names actual test definitions and substantive evidence/limits.
##   Side effects: actual guide/source reads and safe AC/test-count trace only. Guarantees: mapping is derived from real AST definitions, preserving the legacy guide recognizer separately.
##   Raises: AssertionError for missing criterion, nonexistent test or empty evidence; OSError/UnicodeError for guide/source reads; SyntaxError for invalid current test source. System importance: 8 for verified core evidence.
##   Example: invoke test_core_guide_direct_mapping with its named native pytest fixtures to observe its actual stated duty.
## @complexity 6
def test_core_guide_direct_mapping(repo_root):
    try:
        # START_BLOCK_Mapping
        print("[IMP:4][test_core_guide_direct_mapping][Mapping] enter")
        guide = (repo_root / "tests/test_guide.md").read_text(encoding="utf-8")
        current = pathlib.Path(__file__).read_text(encoding="utf-8")
        functions = {n.name for n in ast.parse(current).body if isinstance(n, ast.FunctionDef)}
        rows = re.findall(r"^\| `AC-CORE-([1-8])` \| (.*?) \| (.*?) \|$", guide, re.M)
        assert {n for n, _, _ in rows} == set("12345678")
        for n, names, evidence in rows:
            actual = set(re.findall(r"test_[a-z0-9_]+", names))
            print("[IMP:9][test_core_guide_direct_mapping][CHECK] ac=%s tests=%d" % (n, len(actual)))
            assert actual and actual <= functions and evidence.strip()
        assert "current Python rich contract-authoring" in guide and "independent" in guide
        # END_BLOCK_Mapping
    # START_BLOCK_ErrorHandling
    except (OSError, UnicodeError, SyntaxError, ValueError, ET.ParseError, subprocess.SubprocessError, AssertionError) as error:
        print("[IMP:10][test_core_guide_direct_mapping][ErrorHandling] condition=owned_operation_failure kind=%s" % type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
# endregion FUNC_test_core_guide_direct_mapping

# region FUNC_test_core_promotions_and_remaining_homes [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Require exactly eight current bodies and physically retained deferred homes.
## @uses test_code_core_protocols._read_core_sources, pathlib.Path.read_text
## @io Input: repo_root Path with all readable current core/README/consumer/deferred source files. Output: None after exactly eight current bodies, real completed F3 files and exact current/deferred consumer assertions.
##   Side effects: reads actual complete core and remaining home files, safe allocation result only. Guarantees: source allocation never certifies remaining body completion, runtime adoption or integration consent.
##   Raises: AssertionError for incorrect body status/allocation/disclosure; OSError/UnicodeError for missing or unreadable named sources. System importance: 8 for verified core evidence.
##   Example: invoke test_core_promotions_and_remaining_homes with its named native pytest fixtures to observe its actual stated duty.
## @complexity 6
def test_core_promotions_and_remaining_homes(repo_root):
    try:
        # START_BLOCK_Allocation
        print("[IMP:4][test_core_promotions_and_remaining_homes][Allocation] enter")
        sources, _ = _read_core_sources(repo_root)
        for relative in CORE_FILES[:3]:
            assert "status: draft" in sources[relative]
        readme = sources["README.md"]
        assert "69 drafts and 2 stubs" in readme and "Version: `3.1.0`" in readme
        for path in ("code/ldd.md", "code/tests.md"):
            assert "status: draft" in (repo_root / path).read_text(encoding="utf-8")
        for path in ("code/ax-ui.md", "code/data.md", "checks/lints.md"):
            assert "status: draft" in (repo_root / path).read_text(encoding="utf-8")
        for duty in ("AX, data and lints bodies are current F3 bodies", "general decision lifecycle (DEC01) and full graph are current F4 bodies", "eight prompting F5 and three autonomy/credentials/language policy bodies", "learning F8", "Runtime adoption and propagated enforcement remain unproven"):
            assert duty in readme
        assert "current substantive core bodies" in sources["roles/searcher.md"]
        assert "AX/data/lints bodies are current substantive contracts" in sources["roles/debugger.md"]
        assert "conditional maintenance of an actual target graph is current" in sources["protocols/graph.md"]
        print("[IMP:9][test_core_promotions_and_remaining_homes][RESULT] exactly eight current bodies; remaining homes retained")
        # END_BLOCK_Allocation
    # START_BLOCK_ErrorHandling
    except (OSError, UnicodeError, SyntaxError, ValueError, ET.ParseError, subprocess.SubprocessError, AssertionError) as error:
        print("[IMP:10][test_core_promotions_and_remaining_homes][ErrorHandling] condition=owned_operation_failure kind=%s" % type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
# endregion FUNC_test_core_promotions_and_remaining_homes

# region FUNC_test_core_wholefile_restoration [DOMAIN(8): Core; CONCEPT(8): SourceEvidence; TECH(6): Python]
## @purpose Prove complete full-byte/mode restoration rather than detached sentence reconstruction.
## @uses test_code_core_protocols._read_core_sources, test_code_core_protocols._materialize_fullfile_control, test_code_core_protocols._core_failures, pathlib.Path.read_bytes
## @io Input: repo_root Path with all seven complete core files; tmp_path owned existing Path with absent positive leaf. Output: None after exact original complete bytes/numeric modes, fixed positive judgment and actual file-byte equality.
##   Side effects: reads actual source, writes/readbacks only complete owned positive files with original modes, prints safe restored result. Guarantees: restoration uses original complete source bytes rather than detached sentence reconstruction.
##   Raises: AssertionError for source/full-byte/mode/restored-observation mismatch; OSError/UnicodeError for original or scratch delivery/read failure; ValueError for non-absent destination or invalid normative source. System importance: 8 for verified core evidence.
##   Example: invoke test_core_wholefile_restoration with its named native pytest fixtures to observe its actual stated duty.
## @complexity 6
def test_core_wholefile_restoration(repo_root, tmp_path):
    try:
        # START_BLOCK_Restoration
        print("[IMP:4][test_core_wholefile_restoration][Restoration] enter")
        sources, identities = _read_core_sources(repo_root)
        positive, physical = _materialize_fullfile_control(tmp_path / "positive", sources, identities, [])
        assert physical == identities and _core_failures(positive) == set()
        for relative in CORE_FILES:
            assert (tmp_path / "positive" / relative).read_bytes() == (repo_root / relative).read_bytes()
        print("[IMP:9][test_core_wholefile_restoration][RESULT] exact full bytes and numeric modes restored")
        # END_BLOCK_Restoration
    # START_BLOCK_ErrorHandling
    except (OSError, UnicodeError, SyntaxError, ValueError, ET.ParseError, subprocess.SubprocessError, AssertionError) as error:
        print("[IMP:10][test_core_wholefile_restoration][ErrorHandling] condition=owned_operation_failure kind=%s" % type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
# endregion FUNC_test_core_wholefile_restoration

EXAMPLE_DRIVER = '\nimport json\nimport sys\nlogging.basicConfig(level=logging.INFO, stream=sys.stderr, format="%(message)s")\n# region FUNC_fixture_lookup [DOMAIN(6): Example; CONCEPT(7): Discrimination; TECH(5): Python]\n## @purpose Supply deterministic found/missing/failing cases without claiming package installation.\n## @uses builtins.ValueError\n## @io Input: one nonempty synthetic string; Output: object for present/later, None for missing.\n##   Side effects: safe configured trace. Guarantees: deterministic for these keys, no target imports. Raises: ValueError for broken.\n##   System importance: 7 for branch discrimination; Example: fixture_lookup(\'missing\') returns None.\n## @complexity 2\ndef fixture_lookup(key):\n    # START_BLOCK_Lookup\n    logger.info("[IMP:4][fixture_lookup][LOOKUP] deterministic presence branch")\n    if key == "broken":\n        logger.error("[IMP:10][fixture_lookup][FAILURE] synthetic ValueError")\n        raise ValueError("SECRET_EXCEPTION_PAYLOAD")\n    observed = {"present": True, "later": True}.get(key)\n    logger.info("[IMP:9][fixture_lookup][RESULT] present=%s", observed is not None)\n    return observed\n    # END_BLOCK_Lookup\n# endregion FUNC_fixture_lookup\nvariant = VARIANT_TOKEN\nif variant == "fixture":\n    output = check_all_libraries(("present", "missing", "broken", "later", "bad.name"), fixture_lookup)\nelif variant in ("invalid", "invalid-container", "invalid-provider"):\n    try:\n        if variant == "invalid-container":\n            check_all_libraries("math")\n        elif variant == "invalid-provider":\n            check_all_libraries(("math",), lookup=1)\n        else:\n            check_all_libraries(("math", "math"))\n    except (ValueError, TypeError) as error:\n        output = {"error": type(error).__name__}\nelse:\n    output = check_all_libraries(("math", "missing_core_example_93842", "bad.name"))\nprint(json.dumps(output, sort_keys=True))\n'
