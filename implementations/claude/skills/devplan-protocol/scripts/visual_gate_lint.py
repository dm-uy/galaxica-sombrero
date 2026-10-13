# region MODULE_CONTRACT [DOMAIN(9): NativeMethodology; CONCEPT(9): SourceIdentity, BoundedVerification; TECH(8): Python, StandardLibrary]
## @modulecontract
## @purpose Report bounded supported-node requirement coverage on actual plan/specification inputs for the Architect visual gate of the Claude Code package.
## @scope Finite suffix/BR recognizer with real 0/1/2 CLI exit codes; full XML/Mermaid/semantic coverage remains independent judgment.
## @input A plan file path and an optional specification file path, both read as UTF-8 text. No credentials or provider state.
## @output Importable declared functions, the actual CLI report on stdout, a safe trace on stderr and exit 0 clean, 1 named violations, 2 unreadable or no supported node. No fabricated semantic acceptance.
## @links [USES_API(8): pathlib.Path; USES_API(8): logging; READS_DATA_FROM(9): explicit path inputs; no environment secrets]
## @invariants
## - Current neutral role/phase/scan/gate owners remain controlling; structural checks never prove human authority or role independence.
## - The helper reads only its explicit inputs and writes nothing; exit 0 is a bounded structural pass, never proof of semantic coverage.
## - Private locators/payloads/credentials are absent from source; logs use safe logical classes/counts.
## @rationale
## Q: Why does this package carry its own copy of the helper?
## A: The package is loaded in place and must be self-describing; the behavior is intentionally identical to the sibling package helper, and a shared extraction would change that package, which is a separate decision.
## Q: Why direct logic and actual CLI tests separately?
## A: Native imports prove bounded logic; real subprocess/file/stream/exit observations prove their actual shipped channel.
## Q: Why preserve unavailable/unsupported limits?
## A: Same-author fixtures and bounded recognizers cannot replace independent source meaning, current maps or actual native smoke.
## @changes
## LAST_CHANGE: [1.0.0 - Claude Code package copy of the bounded suffix/BR visual gate helper; behavior identical to the sibling package helper.]
## @modulemap
## FUNC 2[Attach full module documentation with no runtime effects] => visual_gate_lint._module_contract
## FUNC 7[Extract the declared graph block while preserving bounded recognizer limits.] => visual_gate_lint._graph_block
## FUNC 9[Select actual line-opening BR declarations with retained explicit loose fallback.] => visual_gate_lint._spec_brs
## FUNC 9[Deliver the helper real CLI answer and honest diagnostics through their own channels.] => visual_gate_lint.main
## @usecases
## - Architect: run the lint over the plan graph and the specification -> named SCOPE_CREEP, UNKNOWN_BR and UNCOVERED_REQUIREMENT violations or a clean bounded pass.
## - Independent judge: compare actual assertions/source/CLI receipts -> bounded evidence; native acceptance remains separately owned.
## @GREP_SUMMARY Claude Code package, visual gate, DraftCodeGraph, BR coverage, suffix node recognizer,
##   scope creep, unknown and uncovered requirement, real CLI exit 0/1/2, bounded limits
## @STRUCTURE ▶ plan + optional spec → ◇ graph block present? → ○ each supported node ∋ satisfies BR-N
##   → ⊕ covered vs declared BR sets → ∑ violations → ⎋ exit 0 PASS / 1 FAIL / 2 unreadable
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import argparse
import logging
from pathlib import Path
import re
import sys

logger = logging.getLogger(__name__)
_NODE_RE = re.compile(r'<([A-Za-z0-9_]+_(?:py|ts|tsx|js|jsx|CLASS|FUNC|METHOD))\b([^>]*?)/?>')
_SAT_RE = re.compile(r'satisfies="([^"]*)"')
_BR_RE = re.compile(r'\bBR-\d+\b')
_BR_DECL_RE = re.compile(r'^[ \t#*\->0-9.)]*(BR-\d+)\*{0,2}\s*[:\-–—]', re.M)


# region FUNC__graph_block [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Extract the declared graph block while preserving bounded recognizer limits.
## @uses re.search, logging.Logger.info
## @io text str whole plan. Returns str first DraftCodeGraph inner body or empty string when absent. No XML parse, input mutation or external I/O; safe found/not-found trace. TypeError for nonstring input. Example: 〈DraftCodeGraph〉x〈/DraftCodeGraph〉 returns x. Importance:7.
## @complexity 5
def _graph_block(text):
    match = re.search(r'<DraftCodeGraph>(.*?)</DraftCodeGraph>', text, re.S)
    logger.info('[IMP:9][_graph_block][RESULT] found=%s', bool(match))
    return match.group(1) if match else ''
# endregion FUNC__graph_block

# region FUNC__spec_brs [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Select actual line-opening BR declarations with retained explicit loose fallback.
## @uses visual_gate_lint._BR_DECL_RE, visual_gate_lint._BR_RE, logging.Logger.info
## @io text str whole specification. Returns set[str] declared BR-N ids using actual furniture/separator grammar; only if none declared, loose any-mention set. No writes or universal-prose claim; safe count/fallback trace. TypeError for nonstring. Example: heading BR-1 plus prose BR-9 selects BR-1 only. Importance:9.
## @complexity 5
def _spec_brs(text):
    # BUG_FIX_CONTEXT: any-mention harvesting inflated requirements; mixed separators and ordered
    # list declarations disappeared under the older colon/furniture recognizer. Preserve actual
    # line-position declaration grammar and loose fallback only when there are no declarations.
    declared = set(_BR_DECL_RE.findall(text))
    result = declared or set(_BR_RE.findall(text))
    logger.info('[IMP:9][_spec_brs][RESULT] declared=%d selected=%d fallback=%s', len(declared), len(result), not bool(declared))
    return result
# endregion FUNC__spec_brs

# region FUNC_main [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Deliver the helper real CLI answer and honest diagnostics through their own channels.
## @uses argparse.ArgumentParser, visual_gate_lint._graph_block, visual_gate_lint._spec_brs, visual_gate_lint._NODE_RE, pathlib.Path.read_text, logging
## @io argv optional list[str] defaults process argv: actual plan path and optional --spec path. Returns int0 supported clean graph,1 named violations,2 unreadable/absent/no-supported-node input. Reads complete real UTF8 files only; prints actual report stdout and safe stderr trace. No XML/semantic/unsupported-carrier proof. Invalid argparse input exits2; read/UTF8 failure returns2. Example: one _py node satisfying the declared BR-1 yields exit0/nonzero count. Importance:9. Complexity9 reflects explicit validation/recognition/coverage/refusal branches.
## @complexity 9
def main(argv=None):
    logging.basicConfig(level=logging.INFO, stream=sys.stderr, format='%(message)s')
    logger.info('[IMP:4][main][START] bounded suffix visual check')
    parser = argparse.ArgumentParser(description='Bounded suffix/BR visual gate; full XML and semantic review remain independent.')
    parser.add_argument('plan')
    parser.add_argument('--spec')
    try:
        args = parser.parse_args(argv)
    except SystemExit as error:
        if error.code == 0:
            logger.info('[IMP:9][main][HELP] declared usage delivered')
        else:
            logger.error('[IMP:10][main][ARGUMENT_REFUSAL] invalid CLI arguments')
        return error.code
    # START_BLOCK_Validation
    try:
        logger.info('[IMP:7][main][READ] plan')
        graph = _graph_block(Path(args.plan).read_text(encoding='utf-8'))
        if not graph.strip():
            logger.error('[IMP:10][main][GRAPH_MISSING] no supported graph input')
            print('visual-gate: no DraftCodeGraph block', file=sys.stderr)
            return 2
        declared = None
        if args.spec:
            logger.info('[IMP:7][main][READ] specification')
            declared = _spec_brs(Path(args.spec).read_text(encoding='utf-8'))
        logger.info('[IMP:9][main][VALIDATION_SUCCESS] readable graph/spec inputs')
    except (OSError, UnicodeError) as error:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][main][READ_FAILURE] kind=%s', type(error).__name__)
        print('visual-gate: input unreadable', file=sys.stderr)
        return 2
        # END_BLOCK_ErrorHandling
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    violations, covered, count = [], set(), 0
    for tag, attrs in _NODE_RE.findall(graph):
        count += 1
        satisfies = _SAT_RE.search(attrs)
        brs = set(_BR_RE.findall(satisfies.group(1))) if satisfies else set()
        if not brs:
            violations.append('SCOPE_CREEP: node '+tag+' satisfies no BR-N')
            logger.error('[IMP:10][main][ORPHAN] supported node ordinal=%d', count)
        else:
            covered |= brs
            logger.info('[IMP:9][main][NODE_VALID] ordinal=%d coverage=%d', count, len(brs))
    if count == 0:
        logger.error('[IMP:10][main][NO_SUPPORTED_NODES] unsupported carriers require independent review')
        print('visual-gate: no supported node definitions', file=sys.stderr)
        return 2
    if declared is not None:
        violations += ['UNKNOWN_BR: satisfies references '+br for br in sorted(covered-declared)]
        violations += ['UNCOVERED_REQUIREMENT: '+br+' is satisfied by no node' for br in sorted(declared-covered)]
    if violations:
        logger.error('[IMP:10][main][VIOLATIONS] count=%d', len(violations))
        print('VISUAL GATE: FAIL ('+str(count)+' node(s) scanned)')
        for violation in violations:
            print('  '+violation)
        return 1
    logger.info('[IMP:9][main][RESULT] supported=%d requirements=%d', count, len(covered))
    print('VISUAL GATE: PASS ('+str(count)+' node(s), '+str(len(covered))+' BR(s) covered)')
    return 0
    # END_BLOCK_BusinessLogic
# endregion FUNC_main

if __name__ == '__main__':
    sys.exit(main())
