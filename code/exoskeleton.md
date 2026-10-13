---
id: code.exoskeleton
title: Semantic exoskeleton
status: draft
---

# Semantic exoskeleton

This contract describes applicable source authoring and evidence duties under the target rules. Actual runtime mechanisms remain declared adaptation points; textual completion supplies no operational adoption claim.

<!-- anchor: code.exoskeleton.containment -->

## Semantic containers

- **EXO-101** MUST: For authored code, wrap each module contract, function, class and method in correctly named paired region/end-region boundaries at matching indentation. Nest methods inside their class and retain natural algorithm bodies inside the semantic containers; containment applies under the new-module versus edited-function locality rule, never as unsolicited whole-file retrofit.

<!-- anchor: code.exoskeleton.module -->

## New module contract

- **EXO-201** MUST: Start every new module with MODULE_CONTRACT before imports and without a duplicate module-purpose docstring. Include purpose, scope, module input/output, semantic links/dependencies, invariants, rationale Q/A, current changes with LAST_CHANGE, weighted modulemap and actor/action/goal usecases. The LAST descriptive fields are in-contract GREP_SUMMARY and STRUCTURE, then the configured Doxygen metadata anchor, contract end, imports and entity regions. Preserve continuations; the comment syntax is a language binding.

<!-- anchor: code.exoskeleton.functions -->

## Rich function/class/method meaning

- **EXO-301** MUST: Every authored function contract states its outcome and semantically relevant APIs/modules, typed inputs and output, complexity and system importance. Rich substantive information includes input invariants and ranges, output fields and format guarantees, external side effects, operational guarantees, error types with triggering conditions, and a concrete example where applicable. State absence or applicability explicitly. Purpose or I/O vocabulary alone cannot replace these fields; class and method contracts retain their own outcomes and correct containment.

<!-- anchor: code.exoskeleton.relations -->

## Qualified relations and prose

- **EXO-401** MUST: Write project relation entities in uses, links and modulemap with their qualified module.name or module.Class.method and actual package chain; external APIs retain their own names. uses names semantic relevance rather than every call. Remove names the edited body no longer uses. Preserve ALL block-tag paragraphs, continuation content, summary and diagram in XML. In contract prose name tags without at-command syntax and avoid HTML-shaped angle brackets; diagrams use 〈 〉.

<!-- anchor: code.exoskeleton.locality -->

## Incremental authoring and new tests

- **EXO-501** MUST: In an existing module add or edit contracts/regions only for authored or edited functions and instrument only authored new control flow. Preserve untouched branches; do not retrofit missing module metadata unsolicited. Update already-present module facts only when affected and accurately known. Every NEW test module receives the SAME full module tag set, with suite purpose, isolation/determinism invariants, AC-to-test usecases, strategy rationale and each test duty in modulemap; every test keeps its own function purpose. Legacy conversion within authorized edits does not authorize hand-moving standalone summary/structure during a local function edit.

<!-- anchor: code.exoskeleton.repair -->

## Read, repair and retained context

- **EXO-601** MUST: Read the exact source before replacement. When fixing a complex known bug retain BUG_FIX_CONTEXT with the issue, previous approach, cause/problem and chosen fix. Update affected I/O, modulemap, changes/LAST_CHANGE, relevant uses, matching region names and logs. Distill agreed business requirements into rationale and invariants without copying private reasoning; do not fabricate history or document unchanged code as newly authored.

<!-- anchor: code.exoskeleton.enrichment -->

## Semantic enrichment

- **EXO-701** MUST: Keep high-recall domain/concept/technology keywords with their source 1–10 weights, semantically weighted API/data links and modulemap entities, compact one-line module flow diagram, exports/signatures and applicable environment/config dependencies. These describe code meaning, not model telemetry. State environment/config dependencies in links with READS_DATA_FROM and actual names; omit nonexistent dependencies explicitly.
- **EXO-702** MAY: Repeat a mini-diagram in a function description. For complexity above seven, richer explanation remains optional in a dialect whose source says MAY, while an invoked authoring dialect requiring a brief explanation retains that requirement; do not silently exchange their forces.

<!-- anchor: code.exoskeleton.exceptions -->

## Precise conditional exceptions

- **EXO-801** MUST: Apply backend markup unless an explicit written host rule prohibits it; absent neighborhood markup, docstring style or structured logging is not prohibition. Ambiguity defaults to apply and record the ambiguity. Browser/client code alone MAY use the host-permitted minimal JSDoc purpose/invariants and comment-region/summary flavor, or its host convention under the browser-only exemption. Browser verification uses the AX tree and typed component tests. Generated migration revisions whose generator header/revision structure is their contract are exempt from exoskeleton/LDD; retain the revision message and inline why comments for hand-placed changes. Neither exception is a backend waiver.

<!-- anchor: code.exoskeleton.size -->

## Simple modules

- **EXO-901** SHOULD: Prefer small modules solving one clear task and simple explicit blocks, with approximately 300–500 lines as empirical target guidance rather than a universal acceptance ceiling. DRY and modularity remain permitted; avoid opaque universal-switch abstractions. Historical SFT activation, sliding-window and native-scale explanations are attributed source rationale, not measured contemporary model facts.

<!-- anchor: code.exoskeleton.migration -->

## Separately authorized migration safety

- **EXO-1001** MUST: When markup migration is separately authorized, preview exact full old/new changes and prove every changed Python line is an actual COMMENT token in BOTH versions for EVERY promised supported Python interpreter, with identical parsed ASTs before ANY source write. A failed proof aborts ALL writes. Preserve executable behavior, untouched scope, line endings and custom aliases; leave ambiguous/external names and no-anchor cases unchanged and report them. Never invent missing markup or relations. A comment-shaped string or regex match is not token proof. This optional safety contract grants no migration tool port, execution or broader source authorization. Where an actual runtime migration engine is separately provided, preserve its dry-run/check/apply modes, complete old/new Plan and violations, one authorized writer only after ALL proofs, exact token/line coordinates and right-to-left replacements, unparsed/no-anchor/ambiguous/external reporting, stale uses as information only, stable sorted report categories including zero counts, exact unified diff/newline preservation, stdout/stderr/exit contract and actual Python-version limits; its template remains read-only.

<!-- anchor: code.exoskeleton.profiles -->

## Invoked logical-step profile

- **EXO-1101** MUST: Name the actual language/host/authoring profile before authoring and record it in the plan and test guide. Rich contract-authoring and migration profiles retain paired logical-step boundaries for Validation, BusinessLogic and ErrorHandling where applicable, correlated with actual logs. Donor-style code profiles retain plain internal step comments without that second hierarchy and brief step explanations for complexity above seven. Invoking one profile never erases the other profile's applicable MUST; no universal paired-marker mandate or ban follows. Code-region syntax is separate from the planned DraftCodeGraph grammar.

<!-- anchor: code.exoskeleton.anchor -->

## Doxygen language binding

- **EXO-1201** MUST: For configured Doxygen Python code place the dummy metadata anchor after the last descriptive module fields and before contract end/imports. In a host explicitly prohibiting Doxygen omit the anchor and keep pure comments; do not keep it and suppress E402 on every import. Missing configuration is an owed bootstrap requirement, not a neutral exemption. Language-specific region/JSDoc/import/lint bindings remain conditional under actual target rules.

Applicable authored control flow retains its own [LDD](ldd.md) trajectory and [tests](tests.md) evidence. Browser conditions retain [AX](ax-ui.md); data processing retains [data](data.md). The [Doxygen](doxygen.md) and [navigation](navigation.md) contracts bind generated-map use. Their applicability does not depend on a release's disclosure of completion.

<!-- anchor: code.exoskeleton.example -->

## Complete worked module

File `presence_check.py`; profile: current Python rich contract-authoring, with paired logical steps. The callable validates a plain tuple/list container and callable provider before conversion, then nonempty unique plain-string target keys. It rejects unsupported module syntax per item without invoking lookup and continues after lookup failure. Supplied providers owe a caller-owned presence-only/no-import contract; the helper guarantees only its direct actions and default API boundary, not arbitrary provider effects. It checks top-level presence with find_spec, avoiding direct import; dotted lookup can import a parent, so it is deliberately unsupported. The fixture callback is for deterministic example branches and grants no installation proof. Run the extracted module under the target interpreter and inspect its actual process trace; source text alone supplies no result.

```python
# region MODULE_CONTRACT [DOMAIN(8): Environment; CONCEPT(8): Presence, CompleteResult; TECH(7): Python]
## @modulecontract
## @purpose Report every requested module's presence through bounded direct lookup actions without losing later results on error.
## @scope Top-level Python module presence only; dotted imports and installation/readiness are outside this contract.
## @input A plain tuple/list of unique nonempty plain string target keys and an optional callable under the caller's presence-only contract.
## @output Dictionary of every target key to bool; actual safe validation/lookup/failure/count trace.
## @links [USES_API(8): importlib.util.find_spec; USES_API(6): logging]
## @invariants
## - Every validated target key appears exactly once; failed and unsupported lookups are false.
## - The helper never directly imports targets; default top-level find_spec is used within its API boundary.
## - Supplied provider behavior/effects require the caller's contract and are not proved by this helper.
## - Unsupported dotted or malformed targets never reach the lookup callback.
## @rationale
## Q: Why presence rather than importing each package?
## A: Direct import executes target code and can halt the inventory; top-level find_spec requests availability metadata without a direct target import. Provider/hook behavior is a separate boundary.
## Q: Why reject dotted targets?
## A: find_spec for a dotted name may import its parent; a non-importing promise requires this explicit boundary.
## @changes
## LAST_CHANGE: [0.12.0 - Current rich profile and safe per-item continuation, without package readiness claims.]
## @modulemap
## FUNC 8[Complete validated target presence map] => presence_check.check_all_libraries
## @usecases
## - [check_all_libraries]: Environment reviewer -> inspect module presence -> complete bounded status map.
## @GREP_SUMMARY Python, environment, module presence, validation, failure continuation,
##   complete result, non-importing top-level find_spec
## @STRUCTURE ▶ targets → ◇ validate keys → ○ each 〈supported? lookup : false〉
##   → ⊕ complete bool map → ∑ found/total → ⎋ result
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import importlib.util
import logging

logger = logging.getLogger(__name__)

# region FUNC_check_all_libraries [DOMAIN(8): Environment; CONCEPT(8): Presence; TECH(7): find_spec]
## @purpose Give an environment reviewer a complete bounded presence picture despite individual lookup failure.
## @uses importlib.util.find_spec, logging
## @io Input: targets plain tuple/list of unique nonempty plain strings, any finite length including zero;
##   lookup callable str to object-or-None, default top-level find_spec; caller-supplied lookup must
##   obey a presence-only/no-target-import contract, whose behavior is not verified here. Output: dict[str,bool],
##   insertion order equals targets. Side effects: safe trace through the configured logger and lookup calls; supplied lookup effects are caller-owned.
##   Guarantees: all keys returned after validation; unsupported syntax/failing lookup is false; later keys survive.
##   The helper makes no direct target import; provider behavior and package readiness are not guaranteed.
##   Raises: TypeError before conversion/lookup for a container other than plain tuple/list or a non-callable
##   supplied lookup; ValueError before lookup when a key is not a plain string, empty or duplicate.
##   System importance: 8 for complete inventory; Example: check_all_libraries(('math',)) returns {'math': True}
##   in an interpreter providing math; a callback returning None instead returns {'math': False}.
## @complexity 6
def check_all_libraries(targets=("math", "json"), lookup=None) -> dict:
    # START_BLOCK_Validation
    logger.info("[IMP:4][check_all_libraries][INIT] validating supported container/provider")
    if type(targets) not in (tuple, list):
        logger.error("[IMP:10][check_all_libraries][CONTAINER_FAILURE] require plain tuple/list")
        raise TypeError("targets require a plain tuple/list")
    if lookup is not None and not callable(lookup):
        logger.error("[IMP:10][check_all_libraries][PROVIDER_FAILURE] supplied lookup is not callable")
        raise TypeError("lookup requires a callable")
    keys = list(targets)
    if any(type(key) is not str or not key for key in keys) or len(set(keys)) != len(keys):
        logger.error("[IMP:10][check_all_libraries][VALIDATION_FAILURE] invalid or duplicate key")
        raise ValueError("targets require unique nonempty strings")
    logger.info("[IMP:9][check_all_libraries][VALIDATION_SUCCESS] total=%d", len(keys))
    finder = importlib.util.find_spec if lookup is None else lookup
    result_map = {}
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    for ordinal, key in enumerate(keys):
        # START_BLOCK_ItemValidation
        if not key.isidentifier():
            result_map[key] = False
            logger.warning("[IMP:9][check_all_libraries][UNSUPPORTED] item=%d found=false", ordinal)
            continue
        logger.info("[IMP:9][check_all_libraries][ITEM_VALID] item=%d", ordinal)
        # END_BLOCK_ItemValidation
        # START_BLOCK_Lookup
        try:
            logger.info("[IMP:7][check_all_libraries][LOOKUP] item=%d", ordinal)
            result_map[key] = finder(key) is not None
            logger.info("[IMP:6][check_all_libraries][CHECK] item=%d found=%s", ordinal, result_map[key])
        # END_BLOCK_Lookup
        # START_BLOCK_ErrorHandling
        except Exception as error:
            # BUG_FIX_CONTEXT: ImportError-only handling missed ValueError from invalid finder state.
            # Previous: abort the inventory on another lookup exception; Problem: later target keys disappear.
            # Fix: retain false for this item and log ordinal/error class only, then continue safely.
            result_map[key] = False
            logger.error("[IMP:10][check_all_libraries][CHECK_FAILURE] item=%d kind=%s found=false",
                         ordinal, type(error).__name__)
        # END_BLOCK_ErrorHandling
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    installed_count = sum(result_map.values())
    logger.info("[IMP:9][check_all_libraries][RESULT] found=%d total=%d", installed_count, len(keys))
    return result_map
    # END_BLOCK_Result
# endregion FUNC_check_all_libraries
```
