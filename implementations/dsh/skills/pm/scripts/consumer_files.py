# region MODULE_CONTRACT [DOMAIN(9): ConsumerPM; CONCEPT(9): CompleteEvidence, Scope; TECH(7): Python, stdlib]
## @modulecontract
## @purpose Provide one supported metadata/home/config/source-population reader for all three native commands.
## @scope Read-only supported subsets; no full YAML/Doxygen grammar, automatic adoption or code execution.
## @input Explicit root, complete UTF8 records/config and current filesystem.
## @output Layout, DoxyfileInfo, Population and current identities or safe ConsumerInputError.
## @links [USES_API(9): consumer_files.parse_front_matter, consumer_files.covered_sources; READS_DATA_FROM(7): explicitly granted record/config files]
## @invariants
## - Unavailable required evidence is never converted to an empty clean success.
## - Explicit resources and controlling human scope remain separate from structural recognition.
## - Consumer content is never imported or executed; inherited framework inputs remain read-only.
## @rationale
## Q: Why explicit shared input boundaries?
## A: Complete populations prevent the original source omission and false-clean classes; they also expose unsupported grammar.
## Q: Why keep endpoint receipts separate from captured events?
## A: A log API call cannot prove actual file, process or map delivery.
## @changes
## LAST_CHANGE: [2.2.0 - Completed C2 causal repairs, scoped donor capacity and rich per-entity/trajectory/regression evidence.]
## @modulemap
## CLASS 9[Preserve standard help/usage and exit codes while refusing invalid arguments without echoing their dynamic payload.] => consumer_files.SafeArgumentParser
## FUNC 9[Refuse the actual parse failure with constant safe diagnostics and ordinary usage before exit2.] => consumer_files.SafeArgumentParser.error
## CLASS 9[Carry a safe cause for unsupported or unavailable consumer data.] => consumer_files.ConsumerInputError
## CLASS 9[Carry the explicitly selected immutable-by-contract consumer homes and budget overrides.] => consumer_files.Layout
## CLASS 9[Retain effective reset/append settings and original physical alias token coordinates.] => consumer_files.DoxyfileInfo
## CLASS 9[Carry the full configured sorted source population and explicit known-empty distinction.] => consumer_files.Population
## FUNC 9[Emit a safe owning critical diagnostic and refuse unsupported input.] => consumer_files.fail
## FUNC 9[Read all strict UTF8 text while retaining CR/LF/CRLF endings.] => consumer_files.read_text
## FUNC 9[Bind complete regular-file bytes and numeric permission mode.] => consumer_files.identity
## FUNC 9[Resolve a bounded lexical project path and optionally refuse every symlink ancestor.] => consumer_files.contained
## FUNC 9[Split only top-level separators while preserving quoted/nested metadata values.] => consumer_files.split_inline
## FUNC 9[Parse one value from the supported scalar/map/list metadata subset.] => consumer_files.scalar
## FUNC 9[Parse complete selected nested front matter without inventing metadata on absence.] => consumer_files.parse_front_matter
## FUNC 9[Resolve the opt-in profile and real declared homes without relocating consumer records.] => consumer_files.resolve_layout
## FUNC 9[Parse effective supported Doxygen assignments with actual physical token spans.] => consumer_files.parse_doxyfile
## FUNC 9[Enumerate every configured contained source once and retain exact byte/mode identities.] => consumer_files.covered_sources
## FUNC 9[Read current modified paths only from the explicitly selected own repository root with safe Git settings.] => consumer_files.repository_changes
## FUNC 9[Validate an explicit real-shaped UTC timestamp against the actual clock.] => consumer_files.timestamp
## FUNC 9[Validate selected nonfuture actor/channel fields without authenticating human consent.] => consumer_files.provenance
## FUNC 9[Consume one indentation-level mapping or scalar list from the validated metadata rows.] => consumer_files.block
## FUNC 9[Visit one configured candidate under actual exclusion/link/recursive policy.] => consumer_files.visit
## @usecases
## - [declared APIs]: Consumer custodian -> supply actual bounded resources -> inspect complete attributable results.
## - [failure paths]: Independent verifier -> supply unsupported or stale input -> retain refusal evidence.
## @GREP_SUMMARY consumer_files, consumer PM, explicit paths, complete population, supported grammar, evidence
## @STRUCTURE ▶ explicit inputs → ◇ validate supported shape → ○ own operations → ⎋ attributable result or refusal
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import ast
import argparse
import sys
import datetime
import fnmatch
import hashlib
import io
import json
import logging
import os
import re
import stat
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger('consumer_files')
PROFILE = 'methodology-consumer-pm/1.0.0'
DEFAULT_HOMES = {'entry':'AGENTS.md','vision':'VISION.md','roadmap':'ROADMAP.md','handoff':'HANDOFF.md','tasks':'TASKS.md','decisions':'docs/decisions','specs':'specs','recon':'docs/recon','notes':'notes','open_questions':'OPEN_QUESTIONS.md','config':'Doxyfile'}
BUDGETS = {'always_read_lines':600,'handoff_lines':150,'handoff_dates':2,'roadmap_step_chars':300,'roadmap_chars':25000}
BLOCK_TAGS = ('modulemap','invariants','usecases','rationale','changes')

# region CLASS_SafeArgumentParser [DOMAIN(9): ConsumerPM; CONCEPT(10): PayloadSafety; TECH(8): argparse]
## @purpose Preserve standard help/usage and exit codes while refusing invalid arguments without echoing their dynamic payload.
## @uses argparse.ArgumentParser, logging.Logger.error
## @io Input: trusted CLI schema constructor arguments supported by argparse. Output: ArgumentParser subtype with redacted error boundary.
##   Side effects: only declared help/usage/error stderr/stdout; parser does not log supplied values. Guarantee: help0 and invalid2 remain standard.
##   Errors: SystemExit from inherited parser; error override never renders raw message. Example: unknown synthetic credential argument yields safe invalid-arguments only. Importance10.
## @complexity 2
class SafeArgumentParser(argparse.ArgumentParser):
    # region FUNC_error [DOMAIN(9): ConsumerPM; CONCEPT(10): PayloadSafety; TECH(8): argparse]
    ## @purpose Refuse the actual parse failure with constant safe diagnostics and ordinary usage before exit2.
    ## @uses argparse.ArgumentParser.print_usage, argparse.ArgumentParser.exit, logging.Logger.error
    ## @io Input: message str from argparse, intentionally never rendered; self trusted schema. Output: never returns, SystemExit2.
    ##   Side effects: safe owning ERROR importance10 and standard usage stderr. Guarantee: no argument/provenance/credential payload output.
    ##   Errors: SystemExit2; stderr I/O failure remains actual OS error. Example: missing required target emits invalid-arguments without input repr. Importance10.
    ## @complexity 2
    def error(self,message):
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][SafeArgumentParser.error][ARGUMENT_REFUSAL] cause=invalid-arguments')
        self.print_usage(sys.stderr)
        self.exit(2,'error: invalid arguments; inspect declared usage\n')
        # END_BLOCK_ErrorHandling
    # endregion FUNC_error
# endregion CLASS_SafeArgumentParser

# region CLASS_ConsumerInputError [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Carry a safe cause for unsupported or unavailable consumer data.
## @uses ValueError
## @io Input: message str containing a safe class/cause, never payload. Output: ValueError subtype; no parser or filesystem operation. Example: ConsumerInputError("missing-input").
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
class ConsumerInputError(ValueError):
    """Unavailable or unsupported consumer data; safe cause only."""
# endregion CLASS_ConsumerInputError

# region CLASS_Layout [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Carry the explicitly selected immutable-by-contract consumer homes and budget overrides.
## @uses pathlib.Path, dataclasses.dataclass
## @io Input: root/layer absolute contained Path; profile/version/mode str; homes dict[str,Path]; overrides dict[str,int>=0], legacy bool. Output: same named fields, no automatic validation or adoption. Example: single-layer Layout has root==layer and homes["vision"] under root.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
@dataclass
class Layout:
    root: Path
    profile: str
    version: str
    mode: str
    layer: Path
    homes: dict
    overrides: dict = field(default_factory=dict)
    legacy: bool = False
# endregion CLASS_Layout

# region CLASS_DoxyfileInfo [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Retain effective reset/append settings and original physical alias token coordinates.
## @uses dataclasses.dataclass
## @io Input: settings dict[str,list[str]], aliases dict[str,str], physical_spans list[dict key/value/start/end/operator], text complete str. Output: those exact fields; each start/end zero-based physical row/column. Example: ALIASES += token retains its original span.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
@dataclass
class DoxyfileInfo:
    settings: dict
    aliases: dict
    physical_spans: list
    text: str
# endregion CLASS_DoxyfileInfo

# region CLASS_Population [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Carry the full configured sorted source population and explicit known-empty distinction.
## @uses dataclasses.dataclass
## @io Input: files sorted unique relative str list; config_identity lowercase SHA256 str; source_identities list[{path,sha256,mode:int}], coverage_status complete|known-empty, excluded/reasons str lists. Output: same records. Example: empty readable src yields known-empty, never missing-input.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
@dataclass
class Population:
    files: list
    config_identity: str
    source_identities: list
    coverage_status: str
    excluded: list
    reasons: list
# endregion CLASS_Population


# region FUNC_fail [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Emit a safe owning critical diagnostic and refuse unsupported input.
## @uses logging.Logger.error, consumer_files.ConsumerInputError
## @io Input: function/cause safe str identifiers. Output: never returns; raises ConsumerInputError(cause). Side effect: ERROR importance10 with supplied owning function, no payload. Example: fail("covered_sources","missing-input") refuses.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def fail(function, cause):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][fail][INIT] begin owned scoped operation')
    logger.error('[IMP:10][%s][VALIDATION_FAILURE] cause=%s', function, cause)
    raise ConsumerInputError(cause)
    # END_BLOCK_BusinessLogic
# endregion FUNC_fail


# region FUNC_read_text [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Read all strict UTF8 text while retaining CR/LF/CRLF endings.
## @uses pathlib.Path.open, consumer_files.fail
## @io Input: path str|Path to readable regular UTF8 file. Output: complete str with newline=""; zero-length is genuine content. Raises ConsumerInputError on absent/nonregular/no-read-bit/OSError/UnicodeError; Path type errors caller-owned. Example: bytes b"a\r\nb" return "a\r\nb".
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def read_text(path):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][read_text][INIT] begin owned scoped operation')
    path = Path(path)
    logger.info('[IMP:7][read_text][READ] regular UTF8 input')
    try:
        if not path.is_file() or not stat.S_IMODE(path.stat().st_mode) & 0o444:
            fail('read_text','not-readable-regular-file')
        with path.open('r', encoding='utf-8', newline='') as stream:
            result = stream.read()
    except (OSError, UnicodeError):
        fail('read_text','read-or-encoding')
    logger.info('[IMP:7][read_text][READ_SUCCESS] chars=%d',len(result))
    _trajectory_return = result; logger.debug('[IMP:3][read_text][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_read_text


# region FUNC_identity [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Bind complete regular-file bytes and numeric permission mode.
## @uses consumer_files.read_text, hashlib.sha256, stat.S_IMODE
## @io Input: path str|Path readable UTF8 regular file. Output: dict sha256 lowercase64 str, mode int0..4095. Requires stable caller-owned filesystem observation; not a hard race barrier. Raises ConsumerInputError from read boundary/OSError from second stat/read. Example: chmod changes mode but leaves byte hash.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def identity(path):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][identity][INIT] begin owned scoped operation')
    path = Path(path)
    read_text(path)
    _trajectory_return = {'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'mode':stat.S_IMODE(path.stat().st_mode)}; logger.info('[IMP:7][identity][BOUND_IDENTITY] sha256=%s mode=%o',_trajectory_return['sha256'],_trajectory_return['mode']); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_identity


# region FUNC_contained [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Resolve a bounded lexical project path and optionally refuse every symlink ancestor.
## @uses pathlib.Path.resolve, consumer_files.fail
## @io Input: root existing Path; value relative or absolute-contained str|Path without ..; no_symlinks bool. Output: lexical Path under resolved root, preserving link spelling for reads. Raises ConsumerInputError on traversal/escape/cycle or any apply link. Example: contained(root,"src/a.py",True) refuses linked src.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def contained(root, value, no_symlinks=False):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][contained][INIT] begin owned scoped operation')
    root = Path(root).resolve()
    value = Path(value)
    path = value if value.is_absolute() else root/value
    if '..' in value.parts:
        fail('contained','traversal')
    try:
        path.resolve().relative_to(root)
    except (ValueError, RuntimeError, OSError):
        fail('contained','outside-or-cyclic-path')
    if no_symlinks:
        node=path
        while node != root:
            if node.is_symlink():
                fail('contained','symlink-apply-target')
            node=node.parent
    _trajectory_return = path; logger.debug('[IMP:3][contained][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_contained


# region FUNC_split_inline [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Split only top-level separators while preserving quoted/nested metadata values.
## @uses consumer_files.fail
## @io Input: text complete str; separator single-character str default comma. Output: ordered stripped str slices including an empty terminal slice. Raises ConsumerInputError on unclosed quote/unbalanced bracket. Example: a,"b,c" returns ["a", "\"b,c\""].
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def split_inline(text, separator=','):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][split_inline][INIT] begin owned scoped operation')
    result=[]; start=0; quote=None; depth=0; i=0
    while i<len(text):
        c=text[i]
        if quote:
            if c=='\\' and quote=='"':
                i+=2; continue
            if c==quote:
                if quote=="'" and i+1<len(text) and text[i+1]=="'":
                    i+=2; continue
                quote=None
        elif c in "\"'":
            quote=c
        elif c in '{[':
            depth+=1
        elif c in '}]':
            depth-=1
        elif c==separator and depth==0:
            result.append(text[start:i].strip()); start=i+1
        if depth<0:
            fail('split_inline','unbalanced-inline')
        i+=1
    if quote or depth:
        fail('split_inline','unterminated-inline')
    result.append(text[start:].strip())
    _trajectory_return = result; logger.debug('[IMP:3][split_inline][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_split_inline


# region FUNC_scalar [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Parse one value from the supported scalar/map/list metadata subset.
## @uses consumer_files.split_inline, json.loads, consumer_files.fail
## @io Input: value str. Output: str|bool|int|list|dict; plain empty stays empty str; unknown simple scalars preserved. Raises ConsumerInputError on malformed quotes/maps/lists, duplicates, anchors/tags/multiline syntax. Example: [alpha, 2] returns ["alpha",2].
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def scalar(value):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][scalar][INIT] begin owned scoped operation')
    value=value.strip()
    if value.startswith('['):
        if not value.endswith(']'):
            fail('scalar','malformed-list')
        _trajectory_return = [] if not value[1:-1].strip() else [scalar(x) for x in split_inline(value[1:-1])]; logger.debug('[IMP:3][scalar][RETURN] owned result evaluated'); return _trajectory_return
    if value.startswith('{'):
        if not value.endswith('}'):
            fail('scalar','malformed-map')
        result={}
        for item in ([] if not value[1:-1].strip() else split_inline(value[1:-1])):
            # First colon is the map boundary; timestamps stay inside the value.
            match=re.match(r'\s*("(?:\\.|[^"\\])*"|\'(?:\'\'|[^\'])*\'|[A-Za-z_][\w-]*)\s*:\s*(.*)\Z',item)
            if not match:
                fail('scalar','malformed-map-item')
            key=scalar(match.group(1)); val=scalar(match.group(2))
            if key in result:
                fail('scalar','duplicate-map-key')
            result[key]=val
        _trajectory_return = result; logger.debug('[IMP:3][scalar][RETURN] owned result evaluated'); return _trajectory_return
    if value.startswith('"'):
        try:
            result=json.loads(value)
        except (ValueError,TypeError):
            fail('scalar','malformed-quoted-value')
        if not isinstance(result,str):
            fail('scalar','non-string-quoted-value')
        _trajectory_return = result; logger.debug('[IMP:3][scalar][RETURN] owned result evaluated'); return _trajectory_return
    if value.startswith("'"):
        if len(value)<2 or not value.endswith("'"):
            fail('scalar','malformed-single-quote')
        _trajectory_return = value[1:-1].replace("''","'"); logger.debug('[IMP:3][scalar][RETURN] owned result evaluated'); return _trajectory_return
    if value in ('|','>') or re.match(r'^[&*!]',value) or value.startswith('<<:'):
        fail('scalar','unsupported-yaml-construct')
    if any(c in value for c in '{}[]'):
        fail('scalar','malformed-inline-value')
    if value in ('true','false'):
        _trajectory_return = value=='true'; logger.debug('[IMP:3][scalar][RETURN] owned result evaluated'); return _trajectory_return
    if re.fullmatch(r'-?\d+',value):
        _trajectory_return = int(value); logger.debug('[IMP:3][scalar][RETURN] owned result evaluated'); return _trajectory_return
    _trajectory_return = value.split(' #',1)[0].rstrip(); logger.debug('[IMP:3][scalar][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_scalar


# region FUNC_parse_front_matter [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Parse complete selected nested front matter without inventing metadata on absence.
## @uses consumer_files.block, consumer_files.scalar, consumer_files.fail
## @io Input: text complete str whose optional header starts/ends exact --- lines; indentation two spaces. Output: dict with preserved unknown keys; {} only when header genuinely absent. Raises ConsumerInputError on unterminated header/tabs/duplicate or malformed keys/unsupported values. Example: generated block returns dict generated with by and at.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def parse_front_matter(text):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][parse_front_matter][INIT] begin owned scoped operation')
    logger.info('[IMP:4][parse_front_matter][INIT] supported metadata subset')
    lines=text.splitlines()
    if not lines or lines[0]!='---':
        _trajectory_return = {}; logger.debug('[IMP:3][parse_front_matter][RETURN] owned result evaluated'); return _trajectory_return
    try:
        end=lines.index('---',1)
    except ValueError:
        fail('parse_front_matter','unterminated-front-matter')
    items=[]
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if '\t' in line:
            fail('parse_front_matter','tab-indentation')
        indent=len(line)-len(line.lstrip(' '))
        if indent%2:
            fail('parse_front_matter','indentation')
        items.append((indent,line.strip()))
    result,pos=block(items,0,0) if items else ({},0)
    if not isinstance(result,dict) or pos!=len(items):
        fail('parse_front_matter','root-not-map')
    logger.info('[IMP:9][parse_front_matter][VALIDATION_SUCCESS] keys=%d',len(result))
    _trajectory_return = result; logger.debug('[IMP:3][parse_front_matter][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_parse_front_matter


# region FUNC_resolve_layout [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Resolve the opt-in profile and real declared homes without relocating consumer records.
## @uses consumer_files.read_text, consumer_files.parse_front_matter, consumer_files.contained, consumer_files.Layout
## @io Input: root existing str|Path with AGENTS/CONVENTIONS. Output: Layout(root,profile,version,mode,layer,homes,overrides,legacy). Overrides plain int>=0 require decision pointer; legacy only explicit literal1.4 detection. Raises ConsumerInputError on unsupported declaration/invalid home/mode/override/escape. Example: homes vision=charter.md retains that existing home.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def resolve_layout(root):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][resolve_layout][INIT] begin owned scoped operation')
    root=Path(root).resolve()
    agents=read_text(root/'AGENTS.md')
    convention=read_text(root/'CONVENTIONS.md')
    data=parse_front_matter(convention)
    profile=data.get('profile')
    if profile!=PROFILE:
        if 'Project Conventions `1.4.0`' in agents or 'Project Conventions 1.4.0' in agents:
            _trajectory_return = Layout(root,'Project Conventions','1.4.0','single-layer',root,dict(DEFAULT_HOMES),{},True); logger.debug('[IMP:3][resolve_layout][RETURN] owned result evaluated'); return _trajectory_return
        fail('resolve_layout','undeclared-or-unsupported-profile')
    if PROFILE not in agents or str(data.get('conventions_version'))!='1.0.0':
        fail('resolve_layout','entry-profile-version-mismatch')
    mode=data.get('mode'); layer=contained(root,str(data.get('layer','.')))
    if mode not in ('single-layer','layered') or (mode=='single-layer' and layer!=root):
        fail('resolve_layout','invalid-mode-layer')
    homes=dict(DEFAULT_HOMES)
    if mode=='layered':
        for key in ('roadmap','handoff','tasks','specs','recon','notes','open_questions'):
            homes[key]=str(layer.relative_to(root)/homes[key])
    declared=data.get('homes',{})
    if not isinstance(declared,dict) or any(k not in homes for k in declared):
        fail('resolve_layout','invalid-homes')
    homes.update(declared)
    homes={key:contained(root,value) for key,value in homes.items()}
    overrides=data.get('overrides',{})
    if not isinstance(overrides,dict):
        fail('resolve_layout','invalid-overrides')
    if overrides:
        if not data.get('overrides_decision'):
            fail('resolve_layout','overrides-missing-decision')
        for key,value in overrides.items():
            if key not in BUDGETS or type(value)!=int or value<0:
                fail('resolve_layout','invalid-budget-override')
    logger.info('[IMP:9][resolve_layout][VALIDATION_SUCCESS] declared homes=%d',len(homes))
    _trajectory_return = Layout(root,profile,'1.0.0',mode,layer,homes,overrides); logger.debug('[IMP:3][resolve_layout][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_resolve_layout


# region FUNC_parse_doxyfile [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Parse effective supported Doxygen assignments with actual physical token spans.
## @uses io.StringIO, consumer_files.fail, consumer_files.DoxyfileInfo
## @io Input: text complete UTF8 str, CR/LF/CRLF rows; supported KEY =|+=, quoted/bare tokens, comments and continuation. Output: DoxyfileInfo with reset-aware settings/aliases and original zero-based spans. Raises ConsumerInputError on include/variables/effect filters/malformed tokens/booleans or duplicate effective aliases. Example: INPUT=a then INPUT=b then +=c yields [b,c].
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def parse_doxyfile(text):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][parse_doxyfile][INIT] begin owned scoped operation')
    logger.info('[IMP:4][parse_doxyfile][INIT] assignments and original coordinates')
    settings={}; spans=[]; aliases={}; logical=''; coords=[]
    # BUG_FIX_CONTEXT: splitlines also split formfeed/Unicode, unlike tokenizer physical rows.
    physical=io.StringIO(text,newline='').readlines()
    # Preserve each physical character coordinate while joining only genuine continuations.
    for row,line in enumerate(physical):
        body=line.rstrip('\r\n'); quote=False; escaped=False; stop=len(body)
        for col,char in enumerate(body):
            if escaped:
                escaped=False; continue
            if char=='\\' and quote:
                escaped=True; continue
            if char=='"':
                quote=not quote
            elif char=='#' and not quote:
                stop=col; break
        segment=body[:stop].rstrip(); continuation=segment.endswith('\\') and not quote
        if continuation:
            segment=segment[:-1]
        logical+=segment
        coords.extend((row,c) for c in range(len(segment)))
        if continuation:
            logical+=' '; coords.append((row,len(segment))); continue
        if not logical.strip():
            logical=''; coords=[]; continue
        match=re.match(r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*(\+?=)\s*(.*)\Z',logical)
        if not match:
            fail('parse_doxyfile','malformed-or-include-assignment')
        key,op,value=match.groups(); key=key.upper()
        if '$(' in value or '${' in value or '@INCLUDE' in logical or key in ('INPUT_FILTER','FILTER_PATTERNS','FILTER_SOURCE_FILES','ENABLE_PREPROCESSING','PREDEFINED','EXPAND_AS_DEFINED','INCLUDE_PATH','INCLUDE_FILE_PATTERNS'):
            fail('parse_doxyfile','unsupported-effect-construct')
        tokens=[]; i=match.start(3)
        while i<len(logical):
            if logical[i].isspace():
                i+=1; continue
            start=i; token=''
            if logical[i]=='"':
                i+=1
                while i<len(logical) and logical[i]!='"':
                    if logical[i]=='\\' and i+1<len(logical) and logical[i+1] in ('"','\\'):
                        i+=1
                    token+=logical[i]; i+=1
                if i>=len(logical):
                    fail('parse_doxyfile','unterminated-config-quote')
                i+=1
                if i<len(logical) and not logical[i].isspace():
                    fail('parse_doxyfile','unseparated-config-token')
            else:
                while i<len(logical) and not logical[i].isspace():
                    if logical[i]=='"':
                        fail('parse_doxyfile','quote-inside-bare-token')
                    token+=logical[i]; i+=1
            tokens.append(token)
            spans.append({'key':key,'value':token,'start':coords[start],'end':(coords[i-1][0],coords[i-1][1]+1),'operator':op})
        if op=='=':
            settings[key]=[]
        settings.setdefault(key,[]).extend(tokens)
        logical=''; coords=[]
    if logical:
        fail('parse_doxyfile','unfinished-continuation')
    for key in ('RECURSIVE','EXCLUDE_SYMLINKS','GENERATE_XML'):
        if key in settings and (len(settings[key])!=1 or settings[key][0] not in ('YES','NO')):
            fail('parse_doxyfile','unsupported-boolean')
    for token in settings.get('ALIASES',[]):
        name,sep,value=token.partition('=')
        if not sep or not name or name in aliases:
            fail('parse_doxyfile','invalid-or-duplicate-effective-alias')
        aliases[name]=value
    logger.info('[IMP:9][parse_doxyfile][VALIDATION_SUCCESS] settings=%d aliases=%d',len(settings),len(aliases))
    _trajectory_return = DoxyfileInfo(settings,aliases,spans,text); logger.debug('[IMP:3][parse_doxyfile][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_parse_doxyfile


# region FUNC_covered_sources [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Enumerate every configured contained source once and retain exact byte/mode identities.
## @uses consumer_files.visit, consumer_files.contained, consumer_files.identity
## @io Input: root existing Path and DoxyfileInfo with nonempty INPUT. Output: sorted unique lexical relative files, source_identities, config SHA, excluded and complete|known-empty. Honors recursion/patterns/exclusions/links; refuses unknown/unreadable coverage. Raises ConsumerInputError on absent/external/cyclic unsupported/nonregular input. Example: explicit src plus excluded skip.py returns every matching sibling.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def covered_sources(root,info):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][covered_sources][INIT] begin owned scoped operation')
    root=Path(root).resolve(); settings=info.settings
    logger.info('[IMP:4][covered_sources][INIT] complete configured population')
    if not settings.get('INPUT'):
        fail('covered_sources','missing-input')
    patterns=settings.get('FILE_PATTERNS',['*.py']); recursive=settings.get('RECURSIVE',['NO'])==['YES']
    exclude_links=settings.get('EXCLUDE_SYMLINKS',['NO'])==['YES']
    excludes=[contained(root,x).resolve() for x in settings.get('EXCLUDE',[])]
    output=contained(root,(settings.get('OUTPUT_DIRECTORY') or ['doxygen_output'])[0]).resolve()
    files={}; excluded=[]; visited=set()
    for value in settings['INPUT']:
        visit(root,settings,patterns,recursive,exclude_links,excludes,output,files,excluded,visited,contained(root,value),0)
    names=sorted(files.values()); identities=[dict(path=x,**identity(root/x)) for x in names]
    logger.info('[IMP:9][covered_sources][POPULATION_SUCCESS] files=%d',len(names))
    _trajectory_return = Population(names,hashlib.sha256(info.text.encode('utf-8')).hexdigest(),identities,'complete' if names else 'known-empty',sorted(set(excluded)),[]); logger.info('[IMP:9][covered_sources][POPULATION] included=%d excluded=%d status=%s',len(_trajectory_return.files),len(_trajectory_return.excluded),_trajectory_return.coverage_status); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_covered_sources


# region FUNC_repository_changes [DOMAIN(9): ConsumerPM; CONCEPT(9): RootBinding; TECH(8): Git]
## @purpose Read current modified paths only from the explicitly selected own repository root with safe Git settings.
## @uses subprocess.run, consumer_files.fail, pathlib.Path.resolve
## @io Input: root str|Path. Output: None for an evidenced nonrepository/ancestor root, else dict repository=true, changed list[str],
##   argv list[str], root str. Rename destination and original source retained, spaces preserved. Side effects: readonly Git child queries.
##   Guarantees: ambient GIT_* stripped, optional locks/fsmonitor/untracked-cache disabled; .git files supported.
##   Errors: ConsumerInputError on an own or indeterminate Git failure; no silent clean fallback.
##   Example: root/nested without own root binding returns None rather than ancestor changed files. Importance:9.
## @complexity 6
def repository_changes(root):
    # START_BLOCK_Validation
    logger.info('[IMP:4][repository_changes][INIT] begin owned scoped operation')
    root=Path(root).resolve();env={k:v for k,v in os.environ.items() if not k.startswith('GIT_')}
    command=['git','--no-optional-locks','-c','core.fsmonitor=false','-c','core.untrackedCache=false','-C',str(root)]
    logger.info('[IMP:7][repository_changes][ROOT_LOOKUP] actual repository top-level')
    try: top=subprocess.run(command+['rev-parse','--show-toplevel'],env=env,capture_output=True)
    except OSError: fail('repository_changes','git-unavailable')
    if top.returncode:
        if (root/'.git').exists() or b'not a git repository' not in top.stderr: fail('repository_changes','root-binding-unavailable')
        logger.info('[IMP:9][repository_changes][NOT_REPOSITORY] measured root absence');_trajectory_return = None; logger.debug('[IMP:3][repository_changes][RETURN] owned result evaluated'); return _trajectory_return
    if Path(os.fsdecode(top.stdout).strip()).resolve()!=root:
        logger.info('[IMP:9][repository_changes][ANCESTOR] project is not repository root');_trajectory_return = None; logger.debug('[IMP:3][repository_changes][RETURN] owned result evaluated'); return _trajectory_return
    logger.info('[IMP:9][repository_changes][ROOT_VALID] own repository bound')
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    try: result=subprocess.run(command+['status','--porcelain=v1','-z','--untracked-files=all'],env=env,capture_output=True)
    except OSError: fail('repository_changes','confirmed-status-unavailable')
    if result.returncode: fail('repository_changes','confirmed-status-unavailable')
    changed=[];entries=os.fsdecode(result.stdout).split('\0');i=0
    while i<len(entries):
        entry=entries[i]
        if len(entry)>=4:
            changed.append(entry[3:])
            if entry[:1] in 'RC' or entry[1:2] in 'RC':
                i+=1
                if i<len(entries) and entries[i]: changed.append(entries[i])
        i+=1
    logger.info('[IMP:9][repository_changes][RESULT] changed=%d',len(changed))
    _trajectory_return = {'repository':True,'changed':list(dict.fromkeys(changed)),'argv':command,'root':str(root)}; logger.debug('[IMP:3][repository_changes][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_repository_changes


# region FUNC_timestamp [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Validate an explicit real-shaped UTC timestamp against the actual clock.
## @uses datetime.datetime.fromisoformat, consumer_files.fail
## @io Input: value str ISO seconds/fraction with Z|+00:00; now timezone-aware UTC datetime or None uses actual UTC. Output: aware datetime<=now. Raises ConsumerInputError on wrong type/format/calendar/future. Example: 2020-01-01T00:00:00Z is accepted against2021 UTC.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def timestamp(value,now=None):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][timestamp][INIT] begin owned scoped operation')
    now=now or datetime.datetime.now(datetime.timezone.utc)
    if not isinstance(value,str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|\+00:00)',value):
        fail('timestamp','invalid-utc-clock')
    try:
        result=datetime.datetime.fromisoformat(value.replace('Z','+00:00'))
    except ValueError:
        fail('timestamp','invalid-utc-clock')
    if result>now:
        fail('timestamp','future-clock')
    logger.info('[IMP:9][timestamp][VALIDATION_SUCCESS] UTC nonfuture clock')
    _trajectory_return = result; logger.debug('[IMP:3][timestamp][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_timestamp


# region FUNC_provenance [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Validate selected nonfuture actor/channel fields without authenticating human consent.
## @uses consumer_files.timestamp, consumer_files.fail
## @io Input: record dict with by/at nonempty str, plus via nonempty str when gate bool true; now UTC datetime optional. Output: validated timestamp. Extra well-formed metadata retained; placeholders/fake claims refuse. Raises ConsumerInputError on missing/malformed/placeholder/future fields. Example: by=owner still requires independent authentic human source.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def provenance(record,now=None,gate=False):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][provenance][INIT] begin owned scoped operation')
    if not isinstance(record,dict) or not all(isinstance(record.get(k),str) and record[k].strip() for k in (('by','at','via') if gate else ('by','at'))):
        fail('provenance','missing-provenance')
    if any(isinstance(value,str) and re.search(r'[<>]|\{\{|placeholder|fake|invented|fixture grant',value,re.I) for value in record.values()):
        fail('provenance','placeholder-provenance')
    result=timestamp(record['at'],now)
    logger.info('[IMP:9][provenance][VALIDATION_SUCCESS] structural only, authority independently judged')
    _trajectory_return = result; logger.debug('[IMP:3][provenance][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_provenance


# region FUNC_block [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Consume one indentation-level mapping or scalar list from the validated metadata rows.
## @uses consumer_files.scalar, consumer_files.fail
## @io Input: items list[tuple[nonnegative even indent int, stripped row str]] already validated by parse_front_matter;  pos int valid items index and level nonnegative even indent in supplied items. Output: (dict|list,next_index int), consuming every row at level and nested children. Raises ConsumerInputError on mixed shapes/indentation/key duplicates. Example: two block-list rows return two values and index beyond both.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def block(items,pos,level):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][block][INIT] begin owned scoped operation')
    result=[] if items[pos][1].startswith('- ') else {}
    while pos<len(items) and items[pos][0]>=level:
        indent,line=items[pos]
        if indent!=level:
            fail('parse_front_matter','unexpected-indentation')
        if isinstance(result,list):
            if not line.startswith('- '):
                fail('parse_front_matter','mixed-list-map')
            result.append(scalar(line[2:])); pos+=1
            continue
        match=re.fullmatch(r'([A-Za-z_][\w-]*):\s*(.*)',line)
        if not match or match.group(1) in result:
            fail('parse_front_matter','invalid-or-duplicate-key')
        key,val=match.groups(); pos+=1
        if not val and pos<len(items) and items[pos][0]>level:
            if items[pos][0]!=level+2:
                fail('parse_front_matter','nested-indentation')
            val,pos=block(items,pos,level+2)
        else:
            val=scalar(val)
        result[key]=val
    _trajectory_return = result,pos; logger.debug('[IMP:3][block][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_block




# region FUNC_visit [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Visit one configured candidate under actual exclusion/link/recursive policy.
## @uses consumer_files.contained, consumer_files.read_text, fnmatch.fnmatch
## @io Input: root resolved Path, settings dict[str,list[str]], patterns list[str], recursive/exclude_links bool, excludes list[Path], output Path, files dict[Path,str], excluded list[str], visited set[Path] owned accumulators; internal covered_sources only;  path lexical contained Path; depth nonnegative int; supplied files/visited/excluded owned accumulators. Output: None; adds one resolved regular matching source once, or excluded path. Raises ConsumerInputError for escape/unreadable/broken/nonregular input. Example: contained directory cycle terminates through visited resolved directories.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def visit(root,settings,patterns,recursive,exclude_links,excludes,output,files,excluded,visited,path,depth):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][visit][INIT] begin owned scoped operation')
    rel=path.relative_to(root).as_posix()
    if path.is_symlink() and exclude_links:
        excluded.append(rel); _trajectory_return = None; logger.debug('[IMP:3][visit][RETURN] owned result evaluated'); return _trajectory_return
    resolved=contained(root,path).resolve()
    if resolved==root/'.git' or root/'.git' in resolved.parents or resolved==output or output in resolved.parents:
        excluded.append(rel); _trajectory_return = None; logger.debug('[IMP:3][visit][RETURN] owned result evaluated'); return _trajectory_return
    if any(resolved==x or x in resolved.parents for x in excludes) or any(fnmatch.fnmatch(value,pat) for pat in settings.get('EXCLUDE_PATTERNS',[]) for value in (str(path),rel,'/'+rel,path.name)):
        excluded.append(rel); _trajectory_return = None; logger.debug('[IMP:3][visit][RETURN] owned result evaluated'); return _trajectory_return
    if not path.exists():
        fail('covered_sources','missing-or-broken-input')
    if path.is_dir():
        if resolved in visited:
            _trajectory_return = None; logger.debug('[IMP:3][visit][RETURN] owned result evaluated'); return _trajectory_return
        visited.add(resolved)
        if not stat.S_IMODE(path.stat().st_mode)&0o444:
            fail('covered_sources','unreadable-directory')
        try:
            children=sorted(path.iterdir())
        except OSError:
            fail('covered_sources','directory-read')
        for child in children:
            if child.is_dir() and not recursive:
                continue
            visit(root,settings,patterns,recursive,exclude_links,excludes,output,files,excluded,visited,child,depth+1)
    elif path.is_file():
        if any(fnmatch.fnmatch(path.name,pat) for pat in patterns):
            if resolved not in files:
                files[resolved]=rel
                read_text(path)
    else:
        fail('covered_sources','nonregular-input')
    # END_BLOCK_BusinessLogic
# endregion FUNC_visit


