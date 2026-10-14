# region MODULE_CONTRACT [DOMAIN(10): Safeguards; CONCEPT(10): Authority, EffectScope; TECH(8): Python, PreToolUse]
## @modulecontract
## @purpose Refuse recognized ungranted effects under an explicitly pinned session-wide policy.
## @scope Source-stage deterministic guard only; host interception, trust, continuation and fault confinement are unproven AC7.
## @input Explicit policy and handler SHA256 argv; bounded synthetic or future host PreToolUse event JSON.
## @output Fixed deny or no-veto kernel result; process deny JSON or exit2, never native allow or approval.
## @links [USES_API(8): json, pathlib, shlex, hashlib, logging, subprocess; READS_DATA_FROM(9): explicitly pinned policy and definition files]
## @invariants
## - No candidate command, SQL, patch, model or installation is executed by the classifier.
## - Input cannot grant authority or change session profile; parent authenticates literal invocation provenance.
## - Binding objects and entry parents remain protected; no global regenerable or temporary-directory exemptions.
## - Fixed diagnostics never contain raw command, path, patch, fingerprint or secret payload.
## @rationale
## Q: Why deny unknown effects rather than inherit donor silence?
## A: Classification silence is not authority; finite supported syntax leaves explicit denials outside its scope.
## Q: Why session-wide rather than role labels?
## A: Tool metadata has no authenticated per-subagent identity in the approved source stage.
## @changes
## LAST_CHANGE: [2.3.0 - C3 source-stage pinned policy and finite conservative effect recognition; native AC7 held.]
## @modulemap
## FUNC 10[Refuse duplicate nested JSON fields] => guard_destructive._unique_pairs
## FUNC 9[Refuse a failed caller-owned invariant with a fixed safe cause.] => guard_destructive.require
## FUNC 9[Decode one bounded UTF8 object while refusing duplicate security fields.] => guard_destructive.strict_json
## FUNC 9[Resolve one normalized absolute path without following linked entries.] => guard_destructive.canonical
## FUNC 9[Compare canonical path containment on directory boundaries.] => guard_destructive.inside
## FUNC 9[Verify regular metadata and pinned bytes, requiring single-link binding objects.] => guard_destructive.regular
## FUNC 9[Reject Git-linked scratch and linked descendant resources.] => guard_destructive.git_free
## FUNC 9[Validate explicit parent pins, complete policy grammar and immutable protected entries.] => guard_destructive.load_policy
## FUNC 9[Check every addressed effect against binding objects, protected roots and exact grant.] => guard_destructive.resolve_path
## FUNC 9[Verify a closed Git read request using fixed sanitized store-discovery probes.] => guard_destructive.git_read
## FUNC 9[Separate finite shell syntax with quoted heredocs retained as consuming-command data.] => guard_destructive.shell_segments
## FUNC 9[Validate every finite shell effect or exact parent-bound opaque check.] => guard_destructive.classify_shell
## FUNC 9[Return a session-wide deny or no-veto for actual supported event shapes.] => guard_destructive.classify_event
## FUNC 9[Deliver safe native denial or empty no-veto at the actual standalone process boundary.] => guard_destructive.main
## @usecases
## - [main]: Parent -> immutable invocation and permitted scratch event -> empty stdout without an added veto.
## - [classify_event]: Judge -> foreign or protected effect -> safe denial before any candidate command runs.
## @GREP_SUMMARY guard, authority, immutable binding, protected inode, session policy, shell, patch, Git, partial native proof
## @STRUCTURE ▶ explicit pins → ◇ load_policy → ○ classify_event → ◇ all effects granted? → ⎋ no-veto or deny
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import hashlib
import json
import logging
import os
from pathlib import Path
import re
import shlex
import stat
import subprocess
import sys

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())
LIMIT = 65536
OPS = {'read', 'create', 'write', 'delete', 'mode'}
POLICY_KEYS = {'version', 'profile', 'grant', 'session_id', 'source_roots', 'protected_roots', 'git_roots', 'worker_write_roots', 'effects', 'scratch_roots', 'evidence_roots', 'binding', 'checks'}
BINDING_KEYS = {'policy_path', 'policy_mode', 'handler_path', 'handler_mode', 'definition_path', 'definition_mode', 'definition_sha256', 'entries'}
HEX = re.compile(r'[0-9a-f]{64}\Z')


# region FUNC_require [DOMAIN(9): Safeguards; CONCEPT(9): BoundedValidation; TECH(7): Python]
## @purpose Refuse a failed caller-owned invariant with a fixed safe cause.
## @uses guard_destructive.require, pathlib.Path, logging.Logger.info
## @io Input: condition truth value, owner fixed function identifier and reason fixed class. Output/guarantees/errors/side effects/complexity: None on truth; ValueError after owning importance10 refusal otherwise; safe stderr logger only; O(1).
##   System importance:9. Example: require(True, owner, fixed_cause) returns None.
## @complexity 2
def require(condition, owner, reason):
    # START_BLOCK_ValidationAndEffects
    if not condition:
        LOGGER.error('[IMP:10][%s][REFUSE] %s', owner, reason)
        raise ValueError(reason)
    # END_BLOCK_ValidationAndEffects
# endregion FUNC_require


# region FUNC__unique_pairs [DOMAIN(9): JSON; CONCEPT(10): UniqueSecurityFields; TECH(7): json]
## @purpose Reject duplicate fields at every nested JSON object boundary.
## @uses guard_destructive.require
## @io Input: ordered key/value pairs. Output: unique dict; ValueError on duplicate after owning refusal10; no I/O; O(n), importance10. Example: two identical keys refuse.
## @complexity 2
def _unique_pairs(items):
    # START_BLOCK_UniqueFields
    result = {}
    for key, value in items:
        require(key not in result, '_unique_pairs', 'duplicate-field')
        result[key] = value
    LOGGER.info('[IMP:9][_unique_pairs][VALID] unique object fields')
    return result
    # END_BLOCK_UniqueFields
# endregion FUNC__unique_pairs


# region FUNC_strict_json [DOMAIN(9): Safeguards; CONCEPT(9): BoundedValidation; TECH(7): Python]
## @purpose Decode one bounded UTF8 object while refusing duplicate security fields.
## @uses guard_destructive._unique_pairs, json.loads, guard_destructive.require
## @io Input: raw bytes at most65536. Output/guarantees/errors/side effects/complexity: dict with exact JSON values; ValueError/UnicodeError on malformed, duplicate or nonobject; no target effects; O(n).
##   System importance:9. Example: a valid empty object decodes to dict.
## @complexity 1
def strict_json(raw):
    # START_BLOCK_ValidationAndEffects
    require(type(raw) is bytes and len(raw) <= LIMIT, 'strict_json', 'input-size')
    value = json.loads(raw.decode('utf-8'), object_pairs_hook=_unique_pairs,
                       parse_constant=lambda value: require(False, 'strict_json', 'number-shape'))
    require(type(value) is dict, 'strict_json', 'object-shape')
    LOGGER.info('[IMP:9][strict_json][VALID] object decoded')
    return value
    # END_BLOCK_ValidationAndEffects
# endregion FUNC_strict_json


# region FUNC_canonical [DOMAIN(9): Safeguards; CONCEPT(9): BoundedValidation; TECH(7): Python]
## @purpose Resolve one normalized absolute path without following linked entries.
## @uses guard_destructive.require, pathlib.Path, logging.Logger.info
## @io Input: path str, existing bool. Output/guarantees/errors/side effects/complexity: Path; ValueError on absent-required, link, noncanonical or relative input; metadata reads only; O(depth).
##   System importance:9. Example: an existing absolute directory resolves unchanged.
## @complexity 2
def canonical(path, existing=False):
    # START_BLOCK_ValidationAndEffects
    require(type(path) is str and bool(path) and os.path.isabs(path) and os.path.normpath(path) == path,
            'canonical', 'path-shape')
    node = Path(path)
    for part in (node,) + tuple(node.parents):
        require(not part.is_symlink(), 'canonical', 'linked-path')
    require(not existing or node.exists(), 'canonical', 'missing-path')
    require(str(node.resolve()) == path, 'canonical', 'unresolved-path')
    LOGGER.info('[IMP:9][canonical][VALID] canonical path')
    return node
    # END_BLOCK_ValidationAndEffects
# endregion FUNC_canonical


# region FUNC_inside [DOMAIN(9): Safeguards; CONCEPT(9): BoundedValidation; TECH(7): Python]
## @purpose Compare canonical path containment on directory boundaries.
## @uses guard_destructive.require, pathlib.Path, logging.Logger.info
## @io Input: path str and root str. Output/guarantees/errors/side effects/complexity: bool; no I/O/errors for strings; exact equality or slash boundary; O(n).
##   System importance:9. Example: a sibling with a shared prefix is false.
## @complexity 1
def inside(path, root):
    # START_BLOCK_ValidationAndEffects
    return path == root or path.startswith(root.rstrip('/') + '/')
    # END_BLOCK_ValidationAndEffects
# endregion FUNC_inside


# region FUNC_regular [DOMAIN(9): Safeguards; CONCEPT(9): BoundedValidation; TECH(7): Python]
## @purpose Verify regular metadata and pinned bytes, requiring single-link binding objects.
## @uses guard_destructive.require, pathlib.Path, logging.Logger.info
## @io Input: absolute path, optional numeric mode and lowercase SHA256, single_link bool defaultTrue (False only for pinned read-only recipe inputs). Output/guarantees/errors/side effects/complexity: stat result; ValueError/OSError on type/mode/content failure; bounded trusted source reads; O(file bytes).
##   System importance:9. Example: matching source digest passes.
## @complexity 2
def regular(path, mode=None, digest=None, single_link=True):
    # START_BLOCK_ValidationAndEffects
    node = canonical(path, True)
    info = node.lstat()
    require(type(single_link) is bool and stat.S_ISREG(info.st_mode) and (not single_link or info.st_nlink == 1), 'regular', 'file-type')
    require(mode is None or (type(mode) is int and stat.S_IMODE(info.st_mode) == mode), 'regular', 'file-mode')
    if digest is not None:
        require(type(digest) is str and HEX.fullmatch(digest), 'regular', 'digest-shape')
        require(hashlib.sha256(node.read_bytes()).hexdigest() == digest, 'regular', 'file-identity')
    LOGGER.info('[IMP:9][regular][VALID] regular identity')
    return info
    # END_BLOCK_ValidationAndEffects
# endregion FUNC_regular


# region FUNC_git_free [DOMAIN(9): Safeguards; CONCEPT(9): BoundedValidation; TECH(7): Python]
## @purpose Reject Git-linked scratch and linked descendant resources.
## @uses guard_destructive.require, pathlib.Path, logging.Logger.info
## @io Input: existing canonical directory. Output/guarantees/errors/side effects/complexity: None if no .git in ancestry or descendants; ValueError/OSError otherwise; filesystem reads only; O(tree).
##   System importance:9. Example: a new isolated temporary directory passes.
## @complexity 3
def git_free(path):
    # START_BLOCK_ValidationAndEffects
    node = canonical(path, True)
    require(node.is_dir(), 'git_free', 'scratch-type')
    for parent in (node,) + tuple(node.parents):
        require(not (parent / '.git').exists() and not (parent / '.git').is_symlink(), 'git_free', 'git-linked-scratch')
    for directory, names, files in os.walk(str(node), followlinks=False):
        require('.git' not in names + files, 'git_free', 'git-linked-scratch')
        require(not any((Path(directory) / name).is_symlink() for name in names + files), 'git_free', 'linked-scratch')
    LOGGER.info('[IMP:9][git_free][VALID] git-free scratch')
    # END_BLOCK_ValidationAndEffects
# endregion FUNC_git_free


# region FUNC_load_policy [DOMAIN(9): Safeguards; CONCEPT(9): BoundedValidation; TECH(7): Python]
## @purpose Validate explicit parent pins, complete policy grammar and immutable protected entries.
## @uses guard_destructive.require, guard_destructive.resolve_path
## @io Input: policy_path absolute str; policy_sha256 and handler_sha256 lowercase64hex. Output/guarantees/errors/side effects/complexity: validated dict; ValueError/OSError/UnicodeError on malformed/tampered/ungranted binding; filesystem reads only, no policy writes; O(policy and resources).
##   System importance:9. Example: unchanged readonly policy with exact entry inventory validates.
## @complexity 11
def load_policy(policy_path, policy_sha256, handler_sha256):
    # START_BLOCK_ValidationAndEffects
    owner = 'load_policy'
    LOGGER.info('[IMP:7][load_policy][READ] validate explicit binding')
    require(type(policy_sha256) is str and HEX.fullmatch(policy_sha256) and type(handler_sha256) is str and HEX.fullmatch(handler_sha256), owner, 'missing-pins')
    info = regular(policy_path, digest=policy_sha256)
    require(not stat.S_IMODE(info.st_mode) & 0o222 and info.st_size <= LIMIT, owner, 'policy-protection')
    policy = strict_json(Path(policy_path).read_bytes())
    require(set(policy) == POLICY_KEYS and type(policy['version']) is int and policy['version'] == 1, owner, 'policy-shape')
    require(policy['profile'] in ('readonly', 'writable') and all(type(policy[k]) is str and bool(policy[k].strip()) for k in ('grant', 'session_id')), owner, 'policy-authority')
    for key in ('source_roots', 'protected_roots', 'git_roots', 'worker_write_roots', 'scratch_roots', 'evidence_roots'):
        roots = policy[key]
        require(type(roots) is list and all(type(x) is str for x in roots) and len(set(roots)) == len(roots), owner, 'root-shape')
        for root in roots:
            canonical(root, True)
    binding = policy['binding']
    require(type(binding) is dict and set(binding) == BINDING_KEYS, owner, 'binding-shape')
    require(binding['policy_path'] == policy_path and binding['handler_path'] == str(Path(__file__).resolve()), owner, 'binding-path')
    for key, digest in (('policy', policy_sha256), ('handler', handler_sha256), ('definition', binding['definition_sha256'])):
        regular(binding[key + '_path'], binding[key + '_mode'], digest)
    entries = binding['entries']
    require(type(entries) is list and bool(entries), owner, 'entry-shape')
    paths = []
    for entry in entries:
        require(type(entry) is dict and set(entry) == {'path', 'type', 'mode', 'device', 'inode'}, owner, 'entry-shape')
        p = canonical(entry['path'], True); st = p.lstat()
        require(entry['type'] in ('file', 'directory') and all(type(entry[k]) is int for k in ('mode', 'device', 'inode')), owner, 'entry-shape')
        require((stat.S_ISREG(st.st_mode) if entry['type'] == 'file' else stat.S_ISDIR(st.st_mode)) and stat.S_IMODE(st.st_mode) == entry['mode'] and st.st_dev == entry['device'] and st.st_ino == entry['inode'], owner, 'entry-identity')
        paths.append(str(p))
    expected = {binding[k + '_path'] for k in ('policy', 'handler', 'definition')}
    expected |= {str(Path(p).parent) for p in tuple(expected)}
    require(set(paths) == expected and len(paths) == len(expected), owner, 'entry-population')
    for root in policy['worker_write_roots']:
        require(not any(inside(p, root) or inside(root, p) for p in (binding[k + '_path'] for k in ('policy', 'handler', 'definition'))), owner, 'binding-overlap')
        require(not any(inside(root, p) or inside(p, root) for p in policy['protected_roots'] + policy['git_roots']), owner, 'protected-overlap')
    for root in policy['scratch_roots'] + policy['evidence_roots']:
        require(any(inside(root, w) for w in policy['worker_write_roots']), owner, 'resource-root')
        git_free(root)
    require(type(policy['effects']) is list and type(policy['checks']) is list, owner, 'effect-shape')
    for effect in policy['effects']:
        require(type(effect) is dict and set(effect) == {'path', 'operations', 'recursive'} and type(effect['recursive']) is bool, owner, 'effect-shape')
        canonical(effect['path'])
        require(type(effect['operations']) is list and bool(effect['operations']) and all(type(x) is str and x in OPS for x in effect['operations']) and len(set(effect['operations'])) == len(effect['operations']), owner, 'operation-shape')
        require(any(inside(effect['path'], w) for w in policy['worker_write_roots']), owner, 'effect-root')
        require(not any(inside(p, effect['path']) for p in expected), owner, 'binding-ancestor')
    for check in policy['checks']:
        require(type(check) is dict and set(check) == {'command', 'cwd', 'files', 'effects'} and type(check['command']) is str and type(check['files']) is list and bool(check['files']) and type(check['effects']) is list, owner, 'check-shape')
        canonical(check['cwd'], True)
        for pin in check['files']:
            require(type(pin) is dict and set(pin) == {'path', 'sha256', 'mode'}, owner, 'check-pin')
            regular(pin['path'], pin['mode'], pin['sha256'], single_link=False)
        for effect in check['effects']:
            require(type(effect) is dict and set(effect) == {'path', 'operation'}, owner, 'check-effect')
            resolve_path(effect['path'], check['cwd'], effect['operation'], policy)
    LOGGER.info('[IMP:9][load_policy][VALID] immutable binding validated')
    return policy
    # END_BLOCK_ValidationAndEffects
# endregion FUNC_load_policy


# region FUNC_resolve_path [DOMAIN(9): Safeguards; CONCEPT(9): BoundedValidation; TECH(7): Python]
## @purpose Check every addressed effect against binding objects, protected roots and exact grant.
## @uses guard_destructive.require, pathlib.Path, logging.Logger.info
## @io Input: word str, cwd absolute str, operation from OPS, validated policy, recursive bool. Output/guarantees/errors/side effects/complexity: canonical path str only for permitted effect; ValueError/OSError on foreign/unknown/linked/protected/ungranted effect; metadata reads only; O(entries plus bounded recursive tree1024).
##   System importance:9. Example: granted scratch write passes while foreign sibling refuses.
## @complexity 11
def resolve_path(word, cwd, operation, policy, recursive=False):
    # START_BLOCK_ValidationAndEffects
    owner = 'resolve_path'
    require(type(word) is str and bool(word) and not any(c in word for c in ('$', '`', '~', '*', '?', '[', '\\', '\x00', '\n')), owner, 'unknown-path')
    require(operation in OPS, owner, 'unknown-operation')
    path = str(canonical(word if os.path.isabs(word) else os.path.normpath(os.path.join(cwd, word))))
    # Binding entry names and hard-link object identities are protected independently.
    for entry in policy['binding']['entries']:
        require(path != entry['path'] and not (operation != 'read' and recursive and inside(entry['path'], path)), owner, 'protected-binding')
        if os.path.lexists(path):
            info = os.lstat(path)
            require((info.st_dev, info.st_ino) != (entry['device'], entry['inode']), owner, 'protected-alias')
    require(not any(inside(path, p) or (recursive and inside(p, path)) for p in policy['protected_roots'] + policy['git_roots']), owner, 'protected-resource')
    if recursive and os.path.isdir(path):
        population = 0
        for directory, names, files in os.walk(path, followlinks=False):
            population += len(names) + len(files)
            require(population <= 1024 and '.git' not in names + files, owner, 'recursive-population')
            for name in names + files:
                child = Path(directory) / name
                require(not any(inside(str(child), p) for p in policy['protected_roots'] + policy['git_roots']) and str(child) not in {e['path'] for e in policy['binding']['entries']}, owner, 'recursive-protected')
                require(not child.is_symlink() and (not child.is_file() or child.stat().st_nlink == 1), owner, 'recursive-alias')
    if os.path.exists(path) and Path(path).is_file():
        require(os.stat(path).st_nlink == 1, owner, 'hardlinked-resource')
    if operation == 'read' and any(inside(path, p) for p in policy['source_roots'] + policy['scratch_roots'] + policy['evidence_roots']):
        LOGGER.info('[IMP:9][resolve_path][VALID] bounded read')
        return path
    require(policy['profile'] != 'readonly' or not any(inside(path, p) or (recursive and inside(p, path)) for p in policy['source_roots']), owner, 'readonly-source')
    require(any(inside(path, p) for p in policy['worker_write_roots']), owner, 'foreign-resource')
    required_operations = {operation}
    if operation == 'write' and not os.path.exists(path): required_operations.add('create')
    require(not any(inside(path, root) and '.git' in Path(path).relative_to(root).parts for root in policy['scratch_roots'] + policy['evidence_roots']), owner, 'git-scratch-effect')
    permitted = all(any(op in e['operations'] and (path == e['path'] or (e['recursive'] and inside(path, e['path']))) and (not recursive or e['recursive']) for e in policy['effects']) for op in required_operations)
    require(permitted, owner, 'ungranted-effect')
    if operation in ('write', 'create'):
        parent = Path(path).parent
        while not parent.exists():
            resolve_path(str(parent), cwd, 'create', policy)
            parent = parent.parent
    LOGGER.info('[IMP:9][resolve_path][VALID] granted effect')
    return path
    # END_BLOCK_ValidationAndEffects
# endregion FUNC_resolve_path


# region FUNC_git_read [DOMAIN(9): Safeguards; CONCEPT(9): BoundedValidation; TECH(7): Python]
## @purpose Verify a closed Git read request using fixed sanitized store-discovery probes.
## @uses guard_destructive.require, pathlib.Path, logging.Logger.info
## @io Input: words list, canonical cwd and validated policy. Output/guarantees/errors/side effects/complexity: None on declared store/read shape; ValueError/OSError on unknown mutation/options/store or probe failure; one fixed git child timeout3, never candidate execution; O(output max65536).
##   System importance:9. Example: git status in declared source repository passes; fetch refuses.
## @complexity 6
def git_read(words, cwd, policy):
    # START_BLOCK_ValidationAndEffects
    owner = 'git_read'
    args = list(words[1:]); where = cwd; explicit = []
    while args and args[0].startswith('-'):
        option = args.pop(0)
        if option == '-C':
            require(bool(args), owner, 'git-shape'); where = str(canonical(args.pop(0), True))
        elif option in ('--git-dir', '--work-tree'):
            require(bool(args), owner, 'git-shape'); explicit.append(str(canonical(args.pop(0), True)))
        elif option.startswith(('--git-dir=', '--work-tree=')):
            explicit.append(str(canonical(option.partition('=')[2], True)))
        else:
            require(False, owner, 'git-option')
    require(bool(args) and args[0] in ('status', 'diff', 'log', 'rev-parse', 'show'), owner, 'git-mutation')
    require(all(not w.startswith('-') or w in ('--short', '--porcelain', '--stat', '--name-only', '--oneline', '-1', '--show-toplevel', '--git-dir', '--git-common-dir', '--') for w in args[1:]), owner, 'git-option')
    require(not any(any(c in w for c in ('$','`','~','*','?','[')) for w in args), owner, 'git-expansion')
    env = {'PATH': os.defpath, 'HOME': '/nonexistent', 'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': os.devnull, 'GIT_OPTIONAL_LOCKS': '0', 'LC_ALL': 'C'}
    try:
        # Never execute candidate words: these three fixed probes alone discover addressed stores.
        probe = subprocess.run(['/usr/bin/git', '-C', where, 'rev-parse', '--absolute-git-dir', '--git-common-dir', '--show-toplevel'], env=env, capture_output=True, timeout=3)
    except (OSError, subprocess.SubprocessError):
        require(False, owner, 'git-probe')
    require(probe.returncode == 0 and len(probe.stdout) <= LIMIT and not probe.stderr, owner, 'git-probe')
    lines = probe.stdout.decode('utf-8').splitlines()
    require(len(lines) == 3, owner, 'git-probe')
    homes = [str(canonical(p if os.path.isabs(p) else os.path.normpath(os.path.join(where, p)), True)) for p in lines]
    require(all(any(inside(p, r) for r in policy['git_roots']) for p in homes[:2]), owner, 'git-store')
    require(all(p in homes for p in explicit), owner, 'git-address')
    require(any(inside(homes[2], r) for r in policy['source_roots'] + policy['scratch_roots']), owner, 'git-tree')
    # Local Git configuration can invoke fsmonitor, textconv, pager or external diff.
    # Discovery is necessary for an address claim but not proof of candidate purity.
    require(False, owner, 'git-read-recipe-required')
    # END_BLOCK_ValidationAndEffects
# endregion FUNC_git_read


# region FUNC_shell_segments [DOMAIN(9): Safeguards; CONCEPT(9): BoundedValidation; TECH(7): Python]
## @purpose Separate finite shell syntax with quoted heredocs retained as consuming-command data.
## @uses guard_destructive.require, pathlib.Path, logging.Logger.info
## @io Input: command str UTF8 at most65536. Output/guarantees/errors/side effects/complexity: list of token lists; ValueError on unknown punctuation, expansion, malformed quote/heredoc; no command execution; O(n).
##   System importance:9. Example: quoted cat heredoc SQL text never becomes a SQL command.
## @complexity 8
def shell_segments(command):
    # START_BLOCK_ValidationAndEffects
    require(type(command) is str and len(command.encode('utf-8')) <= LIMIT, 'shell_segments', 'shell-size')
    # Quoted heredocs are opaque data owned by a single consuming command.
    lines = command.splitlines(); kept = []; index = 0
    while index < len(lines):
        line = lines[index]; index += 1
        matches = list(re.finditer(r"<<\s*'([A-Za-z_][A-Za-z0-9_]*)'", line))
        if matches:
            require(len(matches) == 1, 'shell_segments', 'heredoc-shape')
            marker = matches[0]; delimiter = marker.group(1)
            require(marker.end() == len(line), 'shell_segments', 'heredoc-shape')
            kept.append(line[:marker.start()] + ' __GUARD_HEREDOC__')
            while index < len(lines) and lines[index] != delimiter:
                index += 1
            require(index < len(lines), 'shell_segments', 'heredoc-shape'); index += 1
        else:
            require('<<' not in line, 'shell_segments', 'heredoc-shape'); kept.append(line)
    text = '\n'.join(kept)
    require(not any(c in text for c in ('`', '$(', '<(', '>(', '\x00')), 'shell_segments', 'shell-expansion')
    lexer = shlex.shlex(text, posix=True, punctuation_chars=';&|<>()\n')
    lexer.whitespace = ' \t\r'; lexer.whitespace_split = True; lexer.commenters = '#'
    tokens = list(lexer); segments = []; current = []
    for token in tokens:
        if token in (';', '\n', '&&', '||'):
            require(bool(current) or token == '\n', 'shell_segments', 'shell-chain')
            if current: segments.append(current)
            current = []
        else:
            require(token not in ('|','&','(',')') and not all(c in ';&|()' for c in token), 'shell_segments', 'unsupported-shell')
            current.append(token)
    if current: segments.append(current)
    require(bool(segments), 'shell_segments', 'empty-shell')
    LOGGER.info('[IMP:9][shell_segments][VALID] segmented finite syntax')
    return segments
    # END_BLOCK_ValidationAndEffects
# endregion FUNC_shell_segments


# region FUNC_classify_shell [DOMAIN(9): Safeguards; CONCEPT(9): BoundedValidation; TECH(7): Python]
## @purpose Validate every finite shell effect or exact parent-bound opaque check.
## @uses guard_destructive.require, guard_destructive.resolve_path
## @io Input: command str, cwd absolute str, policy dict, depth integer0 to2. Output/guarantees/errors/side effects/complexity: None on complete granted effects; ValueError/OSError for unknown effects/options/depth/resources; metadata/fixed Git probes only, no candidate command; O(tokens and resources).
##   System importance:9. Example: quoted granted touch passes and foreign touch refuses.
## @complexity 29
def classify_shell(command, cwd, policy, depth=0):
    # START_BLOCK_ValidationAndEffects
    owner = 'classify_shell'
    require(depth <= 2, owner, 'shell-depth')
    for check in policy['checks']:
        if command == check['command'] and cwd == check['cwd']:
            for pin in check['files']: regular(pin['path'], pin['mode'], pin['sha256'], single_link=False)
            for effect in check['effects']: resolve_path(effect['path'], cwd, effect['operation'], policy)
            LOGGER.info('[IMP:9][classify_shell][VALID] explicit opaque recipe')
            return
    segments = shell_segments(command); conditional = '&&' in command or '||' in command
    for words in segments:
        redirects = []; args = []; index = 0
        while index < len(words):
            word = words[index]; index += 1
            if word in ('>', '>>'):
                require(index < len(words), owner, 'redirect-shape'); redirects.append(words[index]); index += 1
            else:
                require(not any(c in word for c in ('<','>')) or word == '__GUARD_HEREDOC__', owner, 'redirect-shape'); args.append(word)
        for target in redirects: resolve_path(target, cwd, 'write', policy)
        require(bool(args), owner, 'command-shape')
        require(not any('$' in word for word in args), owner, 'shell-expansion')
        require(not re.match(r'^[A-Za-z_][A-Za-z0-9_]*=', args[0]), owner, 'environment-authority')
        name = args[0]
        require(not any('$' in a or '`' in a or any(c in a for c in ('*','?','[','~')) for a in args), owner, 'shell-expansion')
        if name == 'cd':
            require(len(args) == 2 and not conditional, owner, 'conditional-cwd'); cwd = str(canonical(os.path.normpath(os.path.join(cwd, args[1])), True)); continue
        if name in ('sh', 'bash'):
            require(len(args) == 3 and args[1] == '-c' and not redirects, owner, 'shell-flags')
            classify_shell(args[2], cwd, policy, depth + 1); continue
        if name in ('echo', 'printf'):
            require('__GUARD_HEREDOC__' not in args and all(not x.startswith('-') for x in args[1:]), owner, 'output-shape')
            require(name != 'printf' or (len(args) == 3 and args[1] == '%s'), owner, 'printf-shape')
            continue
        if name == 'git': git_read(args, cwd, policy); continue
        if name in ('psql','sqlite3','mysql','mariadb','duckdb','clickhouse','pgcli','usql'):
            require(False, owner, 'sql-resource')
        if name == 'find':
            require(len(args) >= 3 and args[2:] in (['-delete'], ['-exec','rm','-f','{}','+']), owner, 'find-shape')
            resolve_path(args[1], cwd, 'delete', policy, True)
            continue
        heredoc = '__GUARD_HEREDOC__' in args
        require(not heredoc or name == 'cat', owner, 'heredoc-owner')
        operands = args[1:]; options = []
        while operands and operands[0].startswith('-') and operands[0] != '--': options.append(operands.pop(0))
        if operands[:1] == ['--']: operands.pop(0)
        require(not any(x.startswith('-') for x in operands), owner, 'option-position')
        if name in ('cat','ls','stat','rg'):
            allowed = {'cat': {'-n'}, 'ls': {'-l','-a','-la'}, 'stat': set(), 'rg': {'-n','--files','-l','-F'}}[name]
            require(set(options) <= allowed, owner, 'read-option')
            if name == 'rg' and '--files' not in options:
                require(bool(operands), owner, 'read-shape'); operands = operands[1:]
            if heredoc: operands.remove('__GUARD_HEREDOC__')
            for path in operands or ([] if heredoc else ['.']):
                target = str(canonical(path if os.path.isabs(path) else os.path.normpath(os.path.join(cwd, path))))
                resolve_path(path, cwd, 'read', policy, Path(target).is_dir())
        elif name in ('touch','mkdir','tee','rm','chmod','cp','mv'):
            allowed = {'touch': set(), 'mkdir': {'-p'}, 'tee': {'-a'}, 'rm': {'-f','-r','-rf','-fr','--recursive','--force'}, 'chmod': set(), 'cp': {'-R','-r'}, 'mv': set()}[name]
            require(set(options) <= allowed and bool(operands), owner, 'write-option')
            recursive = name in ('cp','rm') and bool(set(options) & {'-r','-R','-rf','-fr','--recursive'})
            if name in ('cp','mv'):
                require(len(operands) == 2, owner, 'copy-shape')
                source = resolve_path(operands[0], cwd, 'read', policy)
                require(not Path(source).is_dir() and not options, owner, 'copy-directory-unsupported')
                destination = str(canonical(operands[1] if os.path.isabs(operands[1]) else os.path.normpath(os.path.join(cwd, operands[1]))))
                if Path(destination).is_dir(): destination = str(Path(destination) / Path(source).name)
                if name == 'mv': resolve_path(operands[0], cwd, 'delete', policy)
                resolve_path(destination, cwd, 'write', policy)
            elif name == 'chmod':
                require(len(operands) >= 2 and re.fullmatch(r'[0-7]{3,4}', operands[0]), owner, 'mode-shape')
                for path in operands[1:]: resolve_path(path, cwd, 'mode', policy)
            else:
                operation = {'touch':'write','mkdir':'create','tee':'write','rm':'delete'}[name]
                for path in operands: resolve_path(path, cwd, operation, policy, recursive or (name == 'mkdir' and '-p' in options))
        elif name == 'find':
            require(len(args) >= 3 and args[2:] in (['-delete'], ['-exec','rm','-f','{}','+']), owner, 'find-shape')
            resolve_path(args[1], cwd, 'delete', policy, True)
        else:
            require(False, owner, 'unknown-command')
    LOGGER.info('[IMP:9][classify_shell][VALID] complete effect population')
    # END_BLOCK_ValidationAndEffects
# endregion FUNC_classify_shell


# region FUNC_classify_event [DOMAIN(9): Safeguards; CONCEPT(9): BoundedValidation; TECH(7): Python]
## @purpose Return a session-wide deny or no-veto for actual supported event shapes.
## @uses guard_destructive.require, guard_destructive.resolve_path
## @io Input: event dict and fully validated policy. Output/guarantees/errors/side effects/complexity: dict with decision deny or no-veto and fixed reason; ordinary input/effect errors become deny; metadata/fixed Git probes only; O(event).
##   System importance:9. Example: foreign patch path yields deny without executing a patch.
## @complexity 8
def classify_event(event, policy):
    # START_BLOCK_ValidationAndEffects
    owner = 'classify_event'
    LOGGER.info('[IMP:4][classify_event][START] validate event and effects')
    try:
        required = {'hook_event_name','session_id','cwd','tool_name','tool_input'}
        optional = {'turn_id','tool_use_id','model','permission_mode','transcript_path'}
        require(type(event) is dict and required <= set(event) <= required | optional and all(type(event[k]) is str for k in (required-{'tool_input'}) | (set(event) & optional)), owner, 'event-shape')
        require(event['hook_event_name'] == 'PreToolUse' and event['session_id'] == policy['session_id'], owner, 'event-binding')
        cwd = str(canonical(event['cwd'], True)); require(Path(cwd).is_dir(), owner, 'cwd-type')
        data = event['tool_input']; require(type(data) is dict and type(data.get('command')) is str, owner, 'tool-shape')
        if event['tool_name'] == 'Bash':
            require(set(data) <= {'command','description','timeout_ms','workdir'} and all(type(data[k]) is str for k in set(data) & {'description','workdir'}) and ('timeout_ms' not in data or type(data['timeout_ms']) is int and data['timeout_ms'] > 0), owner, 'tool-shape')
            if 'workdir' in data: cwd = str(canonical(data['workdir'], True))
            classify_shell(data['command'], cwd, policy)
        elif event['tool_name'] == 'apply_patch':
            require(set(data) == {'command'}, owner, 'patch-shape')
            lines = data['command'].splitlines(); require(len(lines)>=3 and lines[0]=='*** Begin Patch' and lines[-1]=='*** End Patch', owner, 'patch-shape')
            active = False; count = 0
            for line in lines[1:-1]:
                match = re.fullmatch(r'\*\*\* (Add File|Delete File|Update File|Move to): (.+)', line)
                if match:
                    kind, path = match.groups(); require(kind != 'Move to' or active, owner, 'patch-shape')
                    resolve_path(path, cwd, 'delete' if kind=='Delete File' else 'write', policy)
                    if kind=='Update File': resolve_path(path, cwd, 'delete', policy)
                    active = kind=='Update File'; count += 1
                else:
                    require(count > 0 and (line.startswith(('+','-',' ','@@')) or line == '*** End of File'), owner, 'patch-shape')
            require(count > 0, owner, 'patch-shape')
        else: require(False, owner, 'unknown-tool')
        LOGGER.info('[IMP:9][classify_event][VALID] no added veto')
        return {'decision':'no-veto','reason':'granted-effects'}
    except (ValueError, OSError, UnicodeError, TypeError, KeyError):
        LOGGER.error('[IMP:10][classify_event][REFUSE] event-or-effect')
        return {'decision':'deny','reason':'event-or-effect'}
    # END_BLOCK_ValidationAndEffects
# endregion FUNC_classify_event


# region FUNC_main [DOMAIN(9): Safeguards; CONCEPT(9): BoundedValidation; TECH(7): Python]
## @purpose Deliver safe native denial or empty no-veto at the actual standalone process boundary.
## @uses guard_destructive.require, pathlib.Path, logging.Logger.info
## @io Input: argv exact six pin arguments; optional binary stdin and text stdout/stderr. Output/guarantees/errors/side effects/complexity: int0 with deny JSON or empty stdout, int2 with fixed diagnostic on input/binding/internal error; reads at most65537 event bytes; no target execution; O(event plus policy).
##   System importance:9. Example: missing argv returns2 without reflecting arguments.
## @complexity 3
def main(argv=None, stdin=None, stdout=None, stderr=None):
    # START_BLOCK_ValidationAndEffects
    stdin = sys.stdin.buffer if stdin is None else stdin
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    handler = logging.StreamHandler(stderr); handler.setFormatter(logging.Formatter('%(message)s'))
    LOGGER.addHandler(handler); LOGGER.setLevel(logging.INFO)
    try:
        args = list(sys.argv[1:] if argv is None else argv)
        require(len(args)==6 and args[::2]==['--policy','--policy-sha256','--handler-sha256'], 'main', 'invocation-shape')
        policy = load_policy(args[1], args[3], args[5])
        raw = stdin.read(LIMIT + 1); event = strict_json(raw)
        result = classify_event(event, policy)
        if result['decision'] == 'deny':
            stdout.write(json.dumps({'hookSpecificOutput':{'hookEventName':'PreToolUse','permissionDecision':'deny','permissionDecisionReason':result['reason']}})+'\n')
        LOGGER.info('[IMP:9][main][RESULT] %s', result['decision'])
        return 0
    except Exception:
        LOGGER.error('[IMP:10][main][REFUSE] input-or-binding')
        return 2
    finally:
        LOGGER.removeHandler(handler)
    # END_BLOCK_ValidationAndEffects
# endregion FUNC_main


if __name__ == '__main__':
    sys.exit(main())
