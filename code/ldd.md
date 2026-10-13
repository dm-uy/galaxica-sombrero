---
id: code.ldd
title: Log-driven development
status: draft
---

# Log-driven development

This body states source-backed conditional authoring and evidence duties. Runtime mechanisms remain adapter-owned; completion of text supplies no operational adoption claim.

<!-- anchor: code.ldd.identity -->

## Event identity

- **LDD-101** MUST: An authored backend LDD event carries importance from 1 through 10, its own function, its logical block and a meaningful operation or event description. For plain logging the default encoding is [IMP:1-10][FUNCTION_NAME][BLOCK_NAME] Description. The operation can reside in the event or description; this contract creates no universally named operation field. The richer book dialect adds classifier (DB/API/CALC/IO/LOGIC/VALIDATION), operation and status around the same identity; use that dialect only under its actual host profile.

<!-- anchor: code.ldd.scale -->

## Importance meaning

- **LDD-201** MUST: Importance 1–3 is trace: safe local observations within loops. Importance 4–6 is flow: step start/end, internal calls and branching. Importance 7–8 is I/O and boundary: database access, API calls and file reads. Importance 9–10 concerns business logic and belief: critical input/constraint decisions, hypothesis validation, goal achievement and errors.

<!-- anchor: code.ldd.validation -->

## Critical success and failure

- **LDD-301** MUST: A successful authored critical validation is an actual importance9 event in the owning function and block, rather than silence. An authored critical failure emits its owning importance10 diagnosis before propagation or declared handling. A green outcome, any unrelated importance9 string or a borrowed wrapper event cannot discharge this owned critical path.

<!-- anchor: code.ldd.context -->

## Safe exception context

- **LDD-401** MUST: Enrich authored failures with local diagnostic context at importance10; the older template explicitly applies enrichment in complex functions and retains that qualifier. Use safe ordinal, identifier, count and error-class/cause information that explains the failing operation without exposing secrets or sensitive payloads. Temporary repr-style DebugProbe examples are not disclosure permission; remove temporary probes after verification and retain permanent regression evidence.

<!-- anchor: code.ldd.levels -->

## Levels and audit channel

- **LDD-501** MUST: Map importance1–3 to DEBUG, off in production; importance4–6 to INFO; importance7–8 to INFO boundary events; importance9 to INFO or WARNING according to meaning; importance10 to ERROR or CRITICAL. Older illustrative debug calls at importance4 or7 do not override this explicit level mapping. QA audits the actual test-run output for execution meaning; production telemetry and corresponding declared-delivery probes are distinct obligations.

<!-- anchor: code.ldd.encoding -->

## Host encoding and explicit prohibition

- **LDD-601** MUST: When the host mandates structured logging, change bracket encoding only and retain mandatory imp, func and block fields plus meaningful event/operation semantics. Grep and Semantic Trace Verification target the actual host fields; a plan or Deviation omitting those mandatory fields is invalid. Quote an explicit written host prohibition verbatim when claiming an applicable markup/LDD exception. Absent neighboring logs, a docstring style or a structured logger mandate is not such a prohibition; ambiguity defaults to applying the protocol and recording the ambiguity.

<!-- anchor: code.ldd.ownership -->

## Edit locality and owned trajectory

- **LDD-701** MUST: A new function with meaningful branching, validation, I/O or error handling emits its complete owned trajectory. In an existing function instrument only introduced control flow, branches, I/O and errors; do not retrofit untouched branches. A trivial rename, constant or one-line edit without new control flow needs no instrumentation. Wrapper-borrowed logs and an unlogged neighborhood never excuse missing authored flow.

<!-- anchor: code.ldd.audit -->

## Complete log audit

- **LDD-801** MUST: Read the entire produced relevant log and compare actual critical belief, validation, goal and error operations with the intended contracts. Printing filtered records before assertions is necessary exposure and is separate from this full log audit. Report the executed-path conclusion with evidence; passing assertions alone do not establish full correctness.

<!-- anchor: code.ldd.runtime-streams -->

## Original stream bindings

- **LDD-901** MUST: When an original declared CLI logging profile is invoked, retain its actual diagnostic stderr channel and parseable answer stdout. The original `CODEMAP_LOG`, `MARKUP_MIGRATE_LOG` and `ORIENT_LOG` bindings select levels for their respective tools; these are attributed implementation facts, not universal environment requirements or a logger port.

<!-- anchor: code.ldd.worked-example -->

## Bounded executable example

The following file is `count_summary.py` under the current Python rich contract-authoring profile. Its business callable uses a caller-configured stdlib Logger; its return is pure in-process logic, and it promises no external log sink. A declared sink requires the separate real-delivery proof described in [tests](tests.md). Invoke this exact callable directly in the native test module. The fixed input keys `alpha`, `beta`, `gamma` with counts2,5,11 require total18 and count3; this distinguishes summation from first2, last11 and maximum11. Do not derive expected results or operations from its observed output.

```python
# region MODULE_CONTRACT [DOMAIN(8): Counts; CONCEPT(9): Validation, Summation; TECH(7): Python, logging]
## @modulecontract
## @purpose Return a complete validated keyed count summary with an observable owned critical trajectory.
## @scope Finite plain tuple/list entries; duplicate, malformed and negative input rejection; no provider or external sink.
## @input Plain tuple/list of two-item plain tuple/list pairs, unique plain string keys and nonnegative plain integer counts, plus a configured stdlib Logger.
## @output Dict with counts preserving insertion order, total exact sum and count number of keys; actual safe owning validation/error/accumulation/result trace.
## @links [USES_API(8): logging.Logger.info; USES_API(8): logging.Logger.error]
## @invariants
## - bool is rejected as a count despite being an int subclass; empty input and empty string keys are allowed.
## - Validation completes before accumulation; no input payload is included in diagnostic messages.
## - Input is not modified; a rejected input produces no partial returned summary.
## @rationale
## Q: Why validate all pairs before adding counts?
## A: Duplicate keys cannot silently overwrite earlier values and failures cannot return a misleading partial total.
## Q: Why use three unequal counts?
## A: Their sum differs from first, last and maximum, exposing incomplete accumulation.
## @changes
## LAST_CHANGE: [0.13.0 - Bounded sum example with owning critical success and safe failure diagnosis.]
## @modulemap
## FUNC 9[Validate unique keys and accumulate every count] => count_summary.summarize_counts
## @usecases
## - [summarize_counts]: Native test -> direct count summary -> exact keyed total and critical operation sequence.
## @GREP_SUMMARY counts, sum, plain integers, duplicate rejection, safe error, direct logic
## @STRUCTURE ▶ entries → ◇ validate every pair → ○ accumulate all counts → ∑ total → ⎋ complete summary
def _module_contract():
    pass
# endregion MODULE_CONTRACT


import logging

# region FUNC_summarize_counts [DOMAIN(8): Counts; CONCEPT(9): Validation, Sum; TECH(7): logging]
## @purpose Give a caller the exact complete count summary while making critical validation and accumulation observable.
## @uses logging.Logger.info, logging.Logger.error
## @io Input: entries plain tuple/list of finite two-item plain tuple/list pairs; key plain str, including empty;
##   count plain int at least0, never bool; keys unique. logger configured logging.Logger supplied by caller.
##   Output: dict with counts dict[str,int], total int at least0, count int at least0; key order matches input.
##   Side effects: safe trace through caller's actual logger; no file/network/provider setup and no input mutation.
##   Guarantees: validation precedes accumulation; exact sum/count/key population; no partial return on rejection.
##   Raises: TypeError for wrong container, pair shape, key or count type; ValueError for duplicate key or negative count.
##   Each rejection logs own ordinal/cause/error class before raising, without repr of payload.
##   System importance:9 for complete accounting. Example: (("alpha",2),("beta",5),("gamma",11)) gives total18/count3.
## @complexity 6
def summarize_counts(entries, logger):
    # START_BLOCK_Validation
    logger.info("[IMP:4][summarize_counts][INIT] validate supported count input")
    if type(entries) not in (tuple, list):
        logger.error("[IMP:10][summarize_counts][VALIDATION_FAILURE] ordinal=-1 cause=container kind=TypeError")
        raise TypeError("entries require a plain tuple/list")
    counts = {}
    for ordinal, pair in enumerate(entries):
        if type(pair) not in (tuple, list) or len(pair) != 2:
            logger.error("[IMP:10][summarize_counts][VALIDATION_FAILURE] ordinal=%d cause=pair kind=TypeError", ordinal)
            raise TypeError("entry requires a two-item plain pair")
        key, value = pair
        if type(key) is not str or type(value) is not int:
            logger.error("[IMP:10][summarize_counts][VALIDATION_FAILURE] ordinal=%d cause=type kind=TypeError", ordinal)
            raise TypeError("entry requires a string key and plain integer count")
        if key in counts or value < 0:
            cause = "duplicate" if key in counts else "negative"
            logger.error("[IMP:10][summarize_counts][VALIDATION_FAILURE] ordinal=%d cause=%s kind=ValueError", ordinal, cause)
            raise ValueError("entry violates unique-key/nonnegative-count constraint")
        counts[key] = value
        logger.info("[IMP:9][summarize_counts][ITEM_VALID] ordinal=%d", ordinal)
    logger.info("[IMP:9][summarize_counts][VALIDATION_SUCCESS] count=%d", len(counts))
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    total = 0
    for ordinal, value in enumerate(counts.values()):
        total += value
        logger.info("[IMP:9][summarize_counts][ACCUMULATE] ordinal=%d total=%d", ordinal, total)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    result = {"counts": counts, "total": total, "count": len(counts)}
    logger.info("[IMP:9][summarize_counts][RESULT] total=%d count=%d", total, len(counts))
    return result
    # END_BLOCK_Result
# endregion FUNC_summarize_counts
```

Structured encoding uses the actual stdlib API rather than invented keyword arguments: `logger.info("validation accepted", extra={"imp": 9, "func": "summarize_counts", "block": "VALIDATION_SUCCESS"})`. Its LogRecord retains real `levelname`; a real FileHandler formatter can consume `%(imp)s %(func)s %(block)s %(levelname)s %(message)s`. This illustrates encoding only. The plain example above retains the bracket default; neither form automatically configures a sink.
