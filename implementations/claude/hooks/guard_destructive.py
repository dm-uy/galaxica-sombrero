# region MODULE_CONTRACT [DOMAIN(9): Safety, IrreversibleActions; CONCEPT(8): PermissionGate, StopBeforeDestructive, ReadOnlyJudge, Precision; TECH(7): Claude Code PreToolUse hook, shlex, git]
## @modulecontract
## @purpose Keep the owner's confirmation in front of every shell command that would destroy something that cannot be recovered, keep read-only judge agents from changing the tree or the git state they verify, and stay silent for everything else, so that an agent running autonomously inside an approved scope stops only where a stop is worth the owner's time. The neutral owners process/safety.md (preservation, ownership and unknown effects) and roles/qa.md (an independent judge that does not change what it judges) state the rules; this hook is the Claude Code mechanism that enforces the part of them a command line makes recognizable.
## @scope Claude Code PreToolUse hook for the Bash tool, active whenever the methodology-claude plugin is loaded (loading the plugin is the opt-in; METHODOLOGY_GUARD_SCOPE=off switches it off). It splits the command into simple commands, follows cd and variable assignments, sets heredoc bodies aside, classifies each simple command, and for a destructive one answers with a permission decision. It is a tripwire for the common irreversible moves, not a sandbox.
## @input Hook payload on stdin: JSON with tool_name, tool_input.command, cwd and, only inside a subagent, agent_type. Environment: CLAUDE_PROJECT_DIR; METHODOLOGY_GUARD_MODE (ask or deny); METHODOLOGY_GUARD_SCOPE (all, the default, or off); METHODOLOGY_GUARD_SAFE_PREFIXES (path-separator separated scratch roots that replace the defaults); METHODOLOGY_GUARD_READONLY_AGENTS (comma separated agent types that replace the default list qa, reviewer, searcher and their methodology-claude namespaced forms); METHODOLOGY_HOOK_LOG (opt-in stderr trace).
## @output For a destructive command: one JSON object with hookSpecificOutput, permissionDecision (ask by default, deny when METHODOLOGY_GUARD_MODE is deny) and permissionDecisionReason. For a tree-changing command of a read-only agent: the same object with deny. Otherwise no output. Exit status 0 in every case.
## @links [USES_API(8): Claude Code hooks PreToolUse hookSpecificOutput permissionDecision; USES_API(6): subprocess.run for git status, clean -n, worktree list and rev-parse probes; USES_API(7): shlex.shlex; READS_DATA_FROM(7): environment CLAUDE_PROJECT_DIR, TMPDIR, HOME, METHODOLOGY_GUARD_MODE, METHODOLOGY_GUARD_SCOPE, METHODOLOGY_GUARD_SAFE_PREFIXES, METHODOLOGY_GUARD_READONLY_AGENTS, METHODOLOGY_HOOK_LOG; READS_DATA_FROM(6): git state of the project repository; neutral owners process/safety.md and roles/qa.md]
## @invariants
## - The hook never blocks a command it does not recognise as destructive.
## - The hook never fails the session: on any internal error it stays silent, exits 0 and, only when METHODOLOGY_HOOK_LOG is set, traces the error class to stderr.
## - The reason names the rule that matched and at most three paths, never the full command text.
## - Heredoc bodies are data: they are never classified as commands, except the SQL a heredoc feeds to the SQL client of its own command.
## - Every git worktree of the project's repository counts as inside the project.
## - Cache and build artefacts (the REGENERABLE set) are deleted silently wherever they are.
## - A read-only agent is denied, never asked: the owner is not interrupted for a judge that tried to write.
## - In the read-only agent (judge) rules for git branch, git config and the GNU file commands (chmod, chown, chgrp, truncate, ln, install, cp, mv, sed) a long option is judged by the option it names, never by its spelling: git and the GNU tools accept any unambiguous prefix, so the guard expands a prefix against the real option table of the verb first, and for git branch and git config a long option that is neither a known name nor a unique prefix of one counts as a change.
## - The owner ask path (_git_rule and check_rm) is NOT covered by the invariant above: it matches the exact spellings it lists, does not expand an abbreviated long option and does not combine separate short flags. Its known limits are named in the rationale and in the purpose of _git_rule.
## @rationale
## Q: Why ask only when a git command would really lose uncommitted work?
## A: An ask that is almost always noise trains the owner to approve without reading. Cache clean-up in a sibling worktree, a heredoc body and an SQL string written into a test file are false alarms; a checkout of a path over uncommitted edits is a real loss. Precision is what keeps the gate meaningful.
## Q: Why is the guard active whenever the plugin is loaded?
## A: Loading the plugin is the owner's opt-in to the methodology; a second per-project declaration would leave a loaded plugin silently unguarded. METHODOLOGY_GUARD_SCOPE=off remains for the owner who wants none.
## Q: Why ask by default and not deny?
## A: The owner must be able to approve a destructive step that the task really needs. An ask decision reaches the owner even in an autonomous permission mode; deny is the hardened choice.
## Q: Why is a failing git probe silent?
## A: On a known directory it fails because the directory is not a repository; the destructive git command fails there as well and loses nothing. Only an unknown directory asks.
## Q: Why a tokenizer and not a full shell parser?
## A: It is a tripwire for the common irreversible moves, not a sandbox. Targets it cannot resolve (unknown variables, command substitution, xargs input) are left alone on purpose.
## Q: Why expand abbreviated long options, and why does an unknown one fail closed for git branch and git config?
## A: Measured with git 2.54: git branch with the all flag and the mov prefix renames a branch, and git config with the rem prefix removes a section, because git takes any unambiguous prefix of a long option; an exact-spelling table lets both through. The expansion uses the complete option table of the verb. An ambiguous or unknown prefix makes git itself fail, but the table is a copy of a moving target, so for the two verbs where a miss would change the repository the judge is denied instead of trusted. The GNU file commands get the same expansion; an unknown prefix there stays a plain flag, because the tool rejects it.
## Q: Why does the owner ask path not expand abbreviated options as the judge rules do?
## A: The ask path is a tripwire for the common spellings of the irreversible moves, not a sandbox: it matches the exact spellings it lists, does not expand an abbreviation of a long option and does not combine separate short flags. Known limits, all silent: git reset --ha, git clean --f, git push --de, --mir or --forc, git checkout --forc, git switch --disc, git restore --staged --work, git rm --forc, rm --rec --for, and a forced branch deletion made of separate flags or long options (git branch -d -f, -df, --delete --force), because the branch rule asks only for a short cluster that contains the letter D. Closing them needs the complete option table of each verb on this path and is left open in this version.
## Q: Which git verbs does the read-only agent rule intercept?
## A: Exactly the verbs named in the purpose of classify_readonly. Any other git verb that can change the tree, the index, refs or the object store is not intercepted (they are listed there as a known limit); the orchestrator's before and after git status comparison of the tree is the backstop for them.
## @changes
## LAST_CHANGE: [1.0.4 - Fourth debug pass. Text changes without a change of behavior: the abbreviated long option invariant is scoped to the read-only agent (judge) rules for git branch, git config and the GNU file commands, and the exact spellings matched by the owner ask path (_git_rule, check_rm) are stated with their known limits in the contract and in the purpose of _git_rule; the purpose of classify_readonly states the exact git verbs it recognizes and names the verbs it does not intercept, with the before and after git status comparison as the backstop. Code change: the files of a sed in-place call for a read-only agent come from _sed_files (the option scan of _parse_options): the first operand is dropped as the script only when no expression or script file option was given in any spelling, so a script attached to the expression option (sed -i -e's/1/2/', sed -Ei -e's/1/2/', --expression=s/1/2/ in either position, -i.bak -es/1/2/) no longer hides the file, and the rest of a word that carries the in-place letter is its backup suffix (_parse_options short_suffix), so a suffix such as tmpl does not swallow the script word.]
## - 1.0.3 - Long options are judged by the option they name: _expand_long_option expands any unambiguous prefix against the real option table of the verb before it is classified. For a read-only agent git branch (the mov, cop, del, mo prefixes after the all or remotes flag) and git config (the rem, unset-a prefixes) are no longer silent; a long option of git branch or git config that is neither a known name nor a unique prefix of one counts as a change. The all and remotes flags (-a, -r) no longer select the list mode of git branch (git branch -a name is a branch name); the list option, the options that imply listing and the letter l do. The listing forms stay silent, abbreviated or not. The same expansion covers the GNU file commands (chmod, chown, chgrp reference, truncate, ln, install, cp, mv target-directory) through _parse_options, and sed is recognised as an in-place edit in a cluster (-Ei, -ni) or in the long form (_sed_in_place), cp and mv honour the target directory option (_copy_move_operands).
## - 1.0.2 - The helpers added in 1.0.1 (_parse_options, _perl_in_place_files, _written_operands, _touches_project) trace their own verdicts. A read-only agent keeps the listing forms of git branch (list, all, remotes, verbose, contains, merged, no-merged, points-at, sort, format, show-current), judged by _git_branch_changes; branch creation, deletion, rename, copy, force and upstream changes stay denied. Every git fetch stays denied to a read-only agent, the dry run included: a dry run still adds objects to the object store and a judge has no need to fetch (roles/qa.md QA-204). The judge scratch rule is pinned: a write outside the project and its worktrees is silent, the same write anywhere inside them (the evidence directory of the project included) is denied, and a scratch prefix never exempts a project path.
## - 1.0.1 - Read-only agents are also denied git worktree changes, update-ref, fetch, config writes and chmod, chown, chgrp, truncate, perl -i, dd of=, ln and install on project paths; the general path also asks for git rm -f over uncommitted changes and for remote ref deletion by push. Read-only git queries and scratch roots stay silent.
## - 1.0.0 - Adapted for the methodology-claude plugin: active whenever loaded, METHODOLOGY_GUARD environment names, read-only agents qa, reviewer and searcher with their namespaced forms, opt-in stderr trace, full semantic markup and an owned log trajectory.
## @modulemap
## FUNC 2[Attach full module documentation with no runtime effects] => guard_destructive._module_contract
## FUNC 7[Set heredoc bodies aside and return the command lines and the bodies] => guard_destructive.split_heredocs
## FUNC 4[Tokenize shell text with punctuation kept apart] => guard_destructive._tokens
## FUNC 7[Split command text into simple commands, dropping redirection targets] => guard_destructive.simple_commands
## CLASS 8[Where the command runs: project roots, worktrees, effective directory, variables, git probes] => guard_destructive.Context
## FUNC 8[Recursive deletion outside the project, or of the project itself] => guard_destructive.check_rm
## FUNC 7[find -delete or -exec rm over a start path outside the project] => guard_destructive.check_find
## FUNC 9[Git commands that lose uncommitted work or rewrite history] => guard_destructive.check_git
## FUNC 9[The git rules themselves, one verdict per simple command] => guard_destructive._git_rule
## FUNC 6[DROP or TRUNCATE sent to a SQL client] => guard_destructive.check_sql
## FUNC 9[Return the rule a whole command matches, or None] => guard_destructive.classify
## FUNC 8[Turn an abbreviated long option into the option it names, or nothing when ambiguous or unknown] => guard_destructive._expand_long_option
## FUNC 5[Split command words into option flags, option values and operands] => guard_destructive._parse_options
## FUNC 8[Tell a git config write from a git config read] => guard_destructive._git_config_writes
## FUNC 8[Tell a git branch call that changes a ref from one that only lists] => guard_destructive._git_branch_changes
## FUNC 6[Files a perl in-place edit rewrites] => guard_destructive._perl_in_place_files
## FUNC 8[Operands the judged file commands write: chmod, chown, chgrp, truncate, perl, dd, ln, install] => guard_destructive._written_operands
## FUNC 7[Whether a sed call rewrites in place, in any spelling of the switch] => guard_destructive._sed_in_place
## FUNC 8[Files a sed in-place call rewrites: the script is dropped only when no expression or script file option was given] => guard_destructive._sed_files
## FUNC 8[Operands a cp or mv call writes, the target directory option included] => guard_destructive._copy_move_operands
## FUNC 8[Whether a written operand lands in the project] => guard_destructive._touches_project
## FUNC 8[Changes a read-only agent must not make to the tree it verifies] => guard_destructive.classify_readonly
## FUNC 5[Decide whether the guard is switched off by the owner] => guard_destructive.guard_active
## FUNC 5[Name the agent types that are read-only for this run] => guard_destructive.readonly_agents
## FUNC 4[Attach the opt-in stderr trace handler] => guard_destructive._configure_logging
## FUNC 9[Hook entry point: read the payload, answer with a permission decision] => guard_destructive.main
## @usecases
## - [main]: Claude Code (PreToolUse, Bash) -> git checkout of a path over an edited file -> the owner is asked first.
## - [main]: Claude Code (PreToolUse, Bash) -> cache clean-up in a sibling worktree -> silent.
## - [main]: Claude Code (PreToolUse, Bash) -> a qa, reviewer or searcher agent tries to change the project tree, a file mode or git state (worktree, ref, config, fetch) -> deny with a pointer to a scratch copy made without .git.
## - [main]: Claude Code (PreToolUse, Bash) -> a push that deletes a remote ref, or a git rm force over an edited file -> the owner is asked first.
## - [main]: Claude Code (PreToolUse, Bash) -> a qa, reviewer or searcher agent lists branches, or writes its report outside the project -> silent; the same agent writing into the project, its evidence directory included -> deny.
## - [main]: Claude Code (PreToolUse, Bash) -> a qa, reviewer or searcher agent writes a rename, copy, delete or configuration removal with an abbreviated long option (git branch -a --mov, git config --rem) -> deny; the same agent lists with an abbreviated option (git branch --li, git config --get-a) -> silent.
## - [main]: Claude Code (PreToolUse, Bash) -> a qa, reviewer or searcher agent edits a project file with sed in place and the script given by the expression option (sed -i -e's/1/2/' a.py, sed -i --expression=s/1/2/ a.py) -> deny naming the file; the same edit of a scratch file, or sed -n p a.py -> silent.
## @GREP_SUMMARY guard, destructive command, PreToolUse hook, permission decision, ask, deny, force push, reset hard, checkout discard, git clean, worktree remove, rm -rf scope, worktree, heredoc, DROP TABLE, sql client, precision, read-only agent, qa, reviewer, searcher, regenerable artefacts, git worktree, update-ref, git config, git fetch, chmod, chown, truncate, perl -i, dd, ln, install, git rm force, push delete, push mirror, git branch listing, abbreviated long option, unique prefix, getopt_long, option table, fail closed, sed in place, cp mv target directory, fetch denied in every form, judge scratch root, evidence directory, process/safety.md, roles/qa.md, sed expression option, sed script operand, backup suffix, ask path exact spelling, known limits, git verbs not intercepted
## @STRUCTURE ▶ ┌stdin JSON┐ → ◇ scope off? → ⚡ split_heredocs → ○ ∋simple command: 〈VAR= ? remember : cd ? move : rm|find|git|sql|sh -c〉 → ○ ∋long option: ⟦_expand_long_option: exact | unique prefix | ambiguous, unknown ⇒ change⟧ → ◇ git probe: would anything be lost? → 〈read-only agent ∧ (tree, mode or git-state change) ? deny : matched ? ⟦permissionDecision ask|deny + reason⟧ : silent〉 → ⎋ exit 0
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import json
import logging
import os
import re
import shlex
import subprocess
import sys

logger = logging.getLogger("guard_destructive")
logger.addHandler(logging.NullHandler())

HEREDOC_RE = re.compile(r"(?<!<)<<(?!<)(-?)\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\2")
VAR_RE = re.compile(r"\$\{?([A-Za-z_][A-Za-z0-9_]*)\}?")
ASSIGN_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
PUNCTUATION = ";&|<>()\n"
PREFIX_WORDS = {"sudo", "command", "builtin", "nohup", "time", "exec", "nice", "env", "export"}
SHELLS = {"sh", "bash", "zsh", "dash"}
SQL_CLIENTS = {"psql", "sqlite3", "mysql", "mariadb", "duckdb", "clickhouse", "clickhouse-client", "pgcli", "cockroach", "usql"}
SQL_RE = re.compile(r"\b(DROP\s+(TABLE|DATABASE|SCHEMA)|TRUNCATE\s+(TABLE\s+)?[A-Za-z_\"])", re.I)
DEFAULT_SAFE = ("/tmp", "/private/tmp", "/var/folders", "/private/var/folders")
REGENERABLE = {"__pycache__", "*.pyc", "*.pyo", ".pytest_cache", ".mypy_cache", ".ruff_cache", "node_modules",
               ".DS_Store", "build", "dist", "*.egg-info", ".tox", ".nox", ".coverage", "htmlcov", ".cache",
               "doxygen_output", ".next", ".turbo", ".parcel-cache"}
# BUG_FIX_CONTEXT: a judge could still move refs and the object store through fetch and update-ref, which the neutral owners (roles/qa.md QA-204, flow/delegation.md) count as git state; both have no accepted read-only form, so the whole verb is listed. The dry run of fetch was considered for an exemption in 1.0.2 and rejected: measured in a real clone it moves no ref but still writes objects into the object store, and a judge has no need to fetch, so fetch stays denied in every form.
# MUTATING_GIT is a closed list: a git verb outside it (bisect, symbolic-ref, update-index and the others named in the purpose of classify_readonly) is not intercepted for a judge.
MUTATING_GIT = {"commit", "checkout", "switch", "restore", "reset", "clean", "add", "rm", "mv", "merge", "rebase",
                "cherry-pick", "revert", "apply", "am", "pull", "push", "fetch", "update-ref"}
# BUG_FIX_CONTEXT: every git branch call with a bare word was denied to a judge, so the listing forms that take a word (a contains, merged or points-at commit, a list pattern, a sort key) were refused with the creation of a branch. The options are sorted into those that change a ref (a branch change flag wins over everything), those that select the list mode (a bare word is then a pattern or a value), and the two long options that take the next word as their value; with none of them a bare word is a branch name.
# BUG_FIX_CONTEXT: git (every command that uses its option parser) and the GNU tools (getopt_long) accept any unambiguous prefix of a long option, so a guard that compares the exact spelling is bypassed by an abbreviation: git branch with the all flag and the mov prefix of the move option really renames a branch, and git config with the rem prefix removes a section, while both were silent for a judge. Measured in a real clone with git 2.54. Every long option is therefore expanded against the full option table of its verb before it is classified (_expand_long_option), and a long option that is neither a known name nor a unique prefix of one fails closed for git branch and git config, because the judge cannot know that it does not change anything. The same measurement showed that the all and remotes flags are filters, not the list mode: git branch -a name dies with an error and git branch -a --mov a b renames, so only the list option (and the options that imply listing) selects the list mode, and a bare word after the all or remotes flag is a branch name. The verbose flag is no list selector either: git branch -v name creates a branch.
BRANCH_CHANGE_LONG = {"--delete", "--move", "--copy", "--force", "--edit-description", "--set-upstream-to", "--set-upstream", "--unset-upstream"}
BRANCH_CHANGE_LETTERS = "dDmMcCfu"
BRANCH_LIST_LONG = {"--list", "--show-current", "--contains", "--no-contains", "--merged", "--no-merged", "--points-at"}
BRANCH_LIST_LETTERS = "l"
BRANCH_VALUE_LONG = {"--sort", "--format", "--points-at"}
BRANCH_PLAIN_LONG = {"--all", "--remotes", "--verbose", "--quiet", "--track", "--color", "--abbrev", "--column", "--sort", "--format",
                     "--ignore-case", "--omit-empty", "--create-reflog", "--recurse-submodules", "--help"}
BRANCH_LONG_OPTIONS = frozenset(BRANCH_CHANGE_LONG | BRANCH_LIST_LONG | BRANCH_PLAIN_LONG
                                | {"--no-" + n[2:] for n in BRANCH_CHANGE_LONG | BRANCH_LIST_LONG | BRANCH_PLAIN_LONG if not n.startswith("--no-")})
# BUG_FIX_CONTEXT: worktree and config were missing from the judge rules; worktree has one read-only verb (list) and config has read forms, so they are matched by verb and by form, not by name alone.
WORKTREE_CHANGES = {"add", "remove", "prune", "move", "lock", "unlock", "repair"}
CONFIG_READ_FLAGS = {"--get", "--get-all", "--get-regexp", "--get-urlmatch", "--get-color", "--get-colorbool", "--list", "-l"}
CONFIG_WRITE_FLAGS = {"--add", "--unset", "--unset-all", "--replace-all", "--rename-section", "--remove-section", "--edit", "-e"}
CONFIG_WRITE_VERBS = {"set", "unset", "rename-section", "remove-section", "edit"}
CONFIG_READ_VERBS = {"get", "list"}
CONFIG_PLAIN_LONG = {"--global", "--system", "--local", "--worktree", "--file", "--blob", "--type", "--bool", "--int", "--bool-or-int",
                     "--bool-or-str", "--path", "--expiry-date", "--null", "--name-only", "--includes", "--show-origin", "--show-scope",
                     "--show-names", "--default", "--comment", "--fixed-value", "--all", "--regexp", "--value", "--url", "--append", "--help"}
CONFIG_LONG_OPTIONS = frozenset(CONFIG_PLAIN_LONG | {n for n in CONFIG_READ_FLAGS | CONFIG_WRITE_FLAGS if n.startswith("--")}
                                | {"--no-" + n[2:] for n in CONFIG_PLAIN_LONG | CONFIG_READ_FLAGS | CONFIG_WRITE_FLAGS
                                   if n.startswith("--") and not n.startswith("--no-")})
# The long options of the GNU tools whose operands the judge rules read (getopt_long takes any unambiguous prefix of them; there are no
# generated negations, the no- names listed are real options). BSD tools have none of these, so an unknown prefix there is simply a flag.
TRUNCATE_LONG = frozenset("--" + n for n in "no-create io-blocks reference size help version".split())
LN_LONG = frozenset("--" + n for n in ("backup directory force interactive logical no-dereference physical relative suffix symbolic "
                                       "target-directory no-target-directory verbose help version").split())
INSTALL_LONG = frozenset("--" + n for n in ("backup compare debug directory group mode owner preserve-context preserve-timestamps strip "
                                            "strip-program suffix target-directory no-target-directory verbose context unprivileged help version").split())
CHMOD_LONG = frozenset("--" + n for n in ("changes silent quiet verbose no-preserve-root preserve-root reference recursive dereference "
                                          "no-dereference from help version").split())
CP_MV_LONG = frozenset("--" + n for n in ("archive attributes-only backup copy-contents debug dereference force interactive link no-clobber "
                                          "no-dereference no-preserve no-target-directory one-file-system parents preserve recursive reflink "
                                          "remove-destination sparse strip-trailing-slashes suffix symbolic-link target-directory update "
                                          "verbose context keep-directory-symlink exchange no-copy help version").split())
SED_LONG = frozenset("--" + n for n in ("binary debug expression file follow-symlinks help in-place line-length null-data posix quiet "
                                        "regexp-extended sandbox separate silent unbuffered version zero-terminated").split())
# BUG_FIX_CONTEXT: file commands that change the tree or the file modes (the candidate digest includes modes) were not judged; each name maps to the operands it writes in _written_operands.
JUDGE_FILE_COMMANDS = {"chmod", "chown", "chgrp", "truncate", "perl", "dd", "ln", "install"}
OWNERSHIP_FLAGS_RE = re.compile(r"^-[RfvchHLP]+$")
DEFAULT_READONLY = ("qa", "reviewer", "searcher", "methodology-claude:qa", "methodology-claude:reviewer", "methodology-claude:searcher")
HOOK_LOG_ENV = "METHODOLOGY_HOOK_LOG"


# region FUNC_split_heredocs [DOMAIN(7): ShellParsing; CONCEPT(7): HeredocAsData; TECH(6): regex]
## @purpose Keep the text a heredoc carries from being read as commands, while keeping it at hand for the one case where it is executed as a statement: SQL fed to a SQL client.
## @uses guard_destructive.HEREDOC_RE
## @io Input: command str, any shell text. Output: tuple of (kept str, the command lines outside every heredoc body joined by newlines; bodies list of str, one per heredoc in order of appearance, an unterminated body included).
##   Side effects: a trace record only. Guarantees: no body line appears in kept; a quoted or unquoted delimiter and the dash form that strips tabs are recognised; here-strings are not heredocs. Raises: none for str input.
##   System importance: 7. Example: a cat command with a quoted EOF heredoc holding rm -rf returns the cat line as kept and the rm line as the only body.
## @complexity 5
def split_heredocs(command):
    # START_BLOCK_BusinessLogic
    kept, bodies, pending = [], [], []
    body, delimiter, strip_tabs = None, None, False
    for line in command.split("\n"):
        if delimiter is not None:
            probe = line.lstrip("\t") if strip_tabs else line
            if probe.strip() == delimiter:
                bodies.append("\n".join(body))
                delimiter = None
                if pending:
                    (strip_tabs, delimiter), pending = pending[0], pending[1:]
                    body = []
            else:
                body.append(line)
            continue
        kept.append(line)
        found = [(bool(m.group(1)), m.group(3)) for m in HEREDOC_RE.finditer(line)]
        if found:
            (strip_tabs, delimiter), pending = found[0], found[1:]
            body = []
    if delimiter is not None:
        bodies.append("\n".join(body))
    # END_BLOCK_BusinessLogic
    logger.debug("[IMP:3][split_heredocs][BODIES] bodies_set_aside=%d", len(bodies))
    return "\n".join(kept), bodies
# endregion FUNC_split_heredocs


# region FUNC__tokens [DOMAIN(6): ShellParsing; CONCEPT(6): Tokenizing; TECH(7): shlex punctuation_chars]
## @purpose Tokenize shell text so that semicolons, ampersands, pipes, redirections and newlines are tokens of their own even when glued to a word.
## @uses shlex.shlex
## @io Input: text str. Output: list of str tokens; whitespace separates words, a hash starts a comment, punctuation characters form their own tokens.
##   Side effects: none. Guarantees: deterministic for equal input. Raises: ValueError for unbalanced quotes, which simple_commands handles. System importance: 4. Example: the text a;b returns the three tokens a, semicolon and b.
## @complexity 2
def _tokens(text):
    lexer = shlex.shlex(text, posix=True, punctuation_chars=PUNCTUATION)
    lexer.whitespace = " \t\r"
    lexer.whitespace_split = True
    lexer.commenters = "#"
    return list(lexer)
# endregion FUNC__tokens


# region FUNC_simple_commands [DOMAIN(7): ShellParsing; CONCEPT(8): Segmentation; TECH(7): shlex]
## @purpose Cut a command line into the simple commands the shell will run, so that a rule only ever sees the arguments of its own command and never a neighbour's. A heredoc operator becomes a marker word of the form double-less-than, hash, index that points at the matching body.
## @uses guard_destructive._tokens, guard_destructive.PUNCTUATION
## @io Input: text str of kept command lines; with_redirects bool. Output: list of word lists, one per simple command; with with_redirects True a list of (word list, redirect target list) tuples. A redirect target is the word after a greater-than operator.
##   Side effects: a fallback trace record. Guarantees: separators (semicolon, newline, ampersand pairs, pipes, parentheses) end a command; a file descriptor digit before a redirection is dropped; here-string words are data. Unbalanced quotes are tokenized line by line instead of failing.
##   Raises: none for str input. System importance: 7. Example: the text cd d && rm -rf x returns two commands, the cd words and the rm words.
## @complexity 6
def simple_commands(text, with_redirects=False):
    # START_BLOCK_BusinessLogic
    text = text.replace("\\\n", " ")  # a line continuation joins the lines before tokenizing
    try:
        tokens = _tokens(text)
    except ValueError:
        # BUG_FIX_CONTEXT: an unbalanced quote (a quoted multi-line string around a heredoc) made shlex raise and the whole command went unchecked; lines that tokenize on their own are still checked.
        logger.info("[IMP:7][simple_commands][FALLBACK] unbalanced quotes: tokenizing line by line")
        tokens = []
        for line in text.split("\n"):
            try:
                tokens += _tokens(line)
            except ValueError:
                pass
            tokens.append("\n")
    commands, current, skip_next, heredoc_index = [], [], False, 0
    redirects, current_redirects, capture = [], [], False
    for token in tokens:
        if skip_next:
            skip_next = False
            if capture:
                current_redirects.append(token)
                capture = False
            continue
        punct = bool(token) and all(ch in PUNCTUATION for ch in token)
        if punct and (any(ch in token for ch in ";|\n()") or token in ("&", "&&")):
            if current or current_redirects:
                commands.append(current)
                redirects.append(current_redirects)
            current, current_redirects = [], []
        elif punct and token.startswith("<<<"):
            skip_next = True  # a here-string: its word is data
        elif punct and token.startswith("<<"):
            current.append("<<#%d" % heredoc_index)
            heredoc_index += 1
            skip_next = True  # the delimiter word
        elif punct:
            skip_next = True  # a redirection: the next word is its target, not an argument
            capture = ">" in token and token not in (">&", "<&")
            if current and current[-1].isdigit():
                current.pop()  # the file descriptor of a numbered redirection is not an argument
        else:
            current.append(token)
    if current or current_redirects:
        commands.append(current)
        redirects.append(current_redirects)
    # END_BLOCK_BusinessLogic
    logger.info("[IMP:5][simple_commands][RESULT] simple_commands=%d", len(commands))
    return list(zip(commands, redirects)) if with_redirects else commands
# endregion FUNC_simple_commands


# region CLASS_Context [DOMAIN(8): Safety; CONCEPT(8): ProjectScope, EffectiveDirectory; TECH(6): os.path, git]
## @purpose Answer "is this path part of the project" and "would git lose work here" for one command, following cd and variable assignments and counting every worktree of the repository as the project.
class Context:
    # region METHOD___init__ [DOMAIN(6): Safety; CONCEPT(6): Anchor; TECH(5): os.path]
    ## @purpose Anchor the project directory, the directory the command starts in and the scratch roots.
    ## @uses guard_destructive.DEFAULT_SAFE, os.path.realpath
    ## @io Input: project_dir str (may be empty); cwd str or None (defaults to the project directory). Output: None; sets project, cwd, vars, safe and the lazy roots cache.
    ##   Side effects: reads METHODOLOGY_GUARD_SAFE_PREFIXES and TMPDIR from the environment. Guarantees: the environment value replaces the default scratch roots entirely and TMPDIR is added only to the defaults; every root is a real path.
    ##   Raises: none for str input. System importance: 6. Example: with the prefix variable set to one directory, only that directory counts as scratch.
    ## @complexity 3
    def __init__(self, project_dir, cwd=None):
        self.project = os.path.realpath(project_dir) if project_dir else ""
        self.cwd = os.path.realpath(cwd) if cwd else self.project
        self.vars = {}
        self._roots = None
        env_safe = os.environ.get("METHODOLOGY_GUARD_SAFE_PREFIXES")
        prefixes = env_safe.split(os.pathsep) if env_safe is not None else list(DEFAULT_SAFE)
        tmpdir = os.environ.get("TMPDIR")
        if env_safe is None and tmpdir:
            prefixes.append(tmpdir)
        self.safe = [os.path.realpath(p) for p in prefixes if p]
    # endregion METHOD___init__

    # region METHOD_git [DOMAIN(6): Git; CONCEPT(6): Probe; TECH(6): subprocess]
    ## @purpose Run a read-only git probe in a known directory; None when git is missing, fails or times out.
    ## @uses subprocess.run
    ## @io Input: args list of str git arguments; cwd str directory. Output: stdout str on exit status 0, otherwise None.
    ##   Side effects: one git child process with a 3 second timeout; a trace record naming the first git words and the exit status. Guarantees: never raises for OSError or a subprocess error. Raises: none.
    ##   System importance: 7. Example: probing status in a repository returns the porcelain text; probing outside a repository returns None.
    ## @complexity 3
    def git(self, args, cwd):
        try:
            done = subprocess.run(["git", "-C", cwd] + list(args), capture_output=True, text=True, timeout=3)
        except (OSError, subprocess.SubprocessError) as error:
            logger.info("[IMP:7][Context.git][PROBE_FAILURE] kind=%s", type(error).__name__)
            return None
        logger.info("[IMP:7][Context.git][PROBE] git %s exit=%d", " ".join(args[:2]), done.returncode)
        return done.stdout if done.returncode == 0 else None
    # endregion METHOD_git

    # region METHOD_roots [DOMAIN(8): Safety; CONCEPT(8): WorktreesAreProject; TECH(6): git worktree list]
    ## @purpose The project directory plus every worktree of its repository, computed once.
    ## @uses guard_destructive.Context.git, os.path.realpath
    ## @io Input: none. Output: sorted list of unique real path str; empty when the project directory is unknown.
    ##   Side effects: one git probe on the first call, cached afterwards. Guarantees: the project directory is always included when known. Raises: none. System importance: 8.
    ##   Example: a project with one sibling worktree returns both directories.
    ## @complexity 3
    def roots(self):
        if self._roots is None:
            roots = [self.project] if self.project else []
            listing = self.git(["worktree", "list", "--porcelain"], self.project) if self.project else None
            for line in (listing or "").splitlines():
                if line.startswith("worktree "):
                    roots.append(os.path.realpath(line[len("worktree "):]))
            self._roots = sorted(set(roots))
            logger.info("[IMP:5][Context.roots][SCOPE] roots=%d", len(self._roots))
        return self._roots
    # endregion METHOD_roots

    # region METHOD_expand [DOMAIN(6): ShellParsing; CONCEPT(6): Variables; TECH(5): regex]
    ## @purpose Substitute variables assigned earlier in the command, then the environment's.
    ## @uses guard_destructive.VAR_RE
    ## @io Input: word str. Output: str with every known variable replaced; an unknown variable stays as written.
    ##   Side effects: none. Guarantees: command assignments win over the environment. Raises: none. System importance: 5. Example: after S=/x was assigned, the word S in dollar form expands to /x.
    ## @complexity 2
    def expand(self, word):
        return VAR_RE.sub(lambda m: self.vars.get(m.group(1), os.environ.get(m.group(1), m.group(0))), word)
    # endregion METHOD_expand

    # region METHOD_resolve [DOMAIN(7): Paths; CONCEPT(7): Resolution; TECH(6): os.path]
    ## @purpose Turn a shell word into an absolute real path, or None when it cannot be known statically.
    ## @uses guard_destructive.Context.expand, os.path.expanduser, os.path.realpath
    ## @io Input: word str. Output: absolute real path str, or None for an empty word, a command substitution, an unknown variable or a relative word without a known directory.
    ##   Side effects: none. Guarantees: a leading home marker expands through the HOME environment. Raises: none. System importance: 7. Example: a relative word resolves against the effective directory.
    ## @complexity 4
    def resolve(self, word):
        if not word or "$(" in word or "`" in word:
            return None
        word = os.path.expanduser(self.expand(word))
        if "$" in word:
            return None
        if not os.path.isabs(word):
            if not self.cwd:
                return None
            word = os.path.join(self.cwd, word)
        return os.path.realpath(word)
    # endregion METHOD_resolve

    # region METHOD_inside [DOMAIN(8): Safety; CONCEPT(8): Scope; TECH(5): path prefix]
    ## @purpose True for a path in the project, one of its worktrees, or a scratch area.
    ## @uses guard_destructive.Context.roots
    ## @io Input: path str real path. Output: bool. Side effects: may trigger the cached roots probe. Guarantees: a sibling directory sharing a name prefix is not inside. Raises: none. System importance: 8.
    ##   Example: a file under a scratch root returns True; a directory beside the project returns False.
    ## @complexity 3
    def inside(self, path):
        for root in self.roots() + self.safe:
            if path == root or path.startswith(root.rstrip(os.sep) + os.sep):
                return True
        return False
    # endregion METHOD_inside

    # region METHOD_in_project [DOMAIN(8): Safety; CONCEPT(8): TreeScope; TECH(5): path prefix]
    ## @purpose True for a path in the project or one of its worktrees; scratch areas do not count.
    ## @uses guard_destructive.Context.roots
    ## @io Input: path str real path. Output: bool. Side effects: may trigger the cached roots probe. Guarantees: scratch roots never count. Raises: none. System importance: 8. Example: a path in a sibling worktree returns True.
    ## @complexity 2
    def in_project(self, path):
        return any(path == root or path.startswith(root.rstrip(os.sep) + os.sep) for root in self.roots())
    # endregion METHOD_in_project

    # region METHOD_is_project_or_above [DOMAIN(8): Safety; CONCEPT(8): WholeProjectDeletion; TECH(5): path prefix]
    ## @purpose True for the project itself, a worktree root, or any directory that contains one.
    ## @uses guard_destructive.Context.roots
    ## @io Input: path str real path. Output: bool. Side effects: may trigger the cached roots probe. Guarantees: a deeper directory inside the project is not matched. Raises: none. System importance: 8. Example: the parent directory of the project returns True.
    ## @complexity 2
    def is_project_or_above(self, path):
        for root in self.roots():
            if root == path or root.startswith(path.rstrip(os.sep) + os.sep):
                return True
        return False
    # endregion METHOD_is_project_or_above
# endregion CLASS_Context


# region FUNC_check_rm [DOMAIN(9): Safety; CONCEPT(8): DeletionScope; TECH(6): glob prefix]
## @purpose Ask before a recursive deletion that reaches outside the project or removes the project itself; cleaning a build or cache directory anywhere inside the project or its worktrees stays silent.
## @uses guard_destructive.Context.resolve, guard_destructive.Context.inside, guard_destructive.Context.is_project_or_above, guard_destructive.REGENERABLE
## @io Input: words list of str, the rm command words; ctx Context. Output: rule str naming up to three risky operands, or None. Only recursive flags (r, R or the long form) are judged.
##   Side effects: a trace record on a match. Guarantees: regenerable names and unresolvable operands are skipped; a glob is judged by the directory before it, and a project-wide glob (a bare star) counts as the project. Raises: none. System importance: 8.
##   Example: rm -rf with an operand outside every project root returns a rule text; rm -rf build returns None.
## @complexity 6
def check_rm(words, ctx):
    # START_BLOCK_BusinessLogic
    flags = [w for w in words[1:] if w.startswith("-") and w != "--"]
    recursive = any(w == "--recursive" or (not w.startswith("--") and re.search(r"[rR]", w)) for w in flags)
    if not recursive:
        logger.info("[IMP:5][check_rm][NOT_RECURSIVE] no recursive flag")
        return None
    risky, after_dashdash = [], False
    for word in words[1:]:
        if word == "--":
            after_dashdash = True
            continue
        if word.startswith("-") and not after_dashdash:
            continue
        if os.path.basename(word.rstrip("/")) in REGENERABLE:
            continue
        glob_at = min([i for i, ch in enumerate(word) if ch in "*?["] or [len(word)])
        is_glob = glob_at < len(word)
        head = word[:glob_at]
        directory = (head.rsplit("/", 1)[0] or "/") if "/" in head else ""
        path = ctx.resolve(directory or ".") if is_glob else ctx.resolve(word)
        if path is None:
            continue
        pattern = word[len(directory.rstrip("/")) + 1:] if directory else word
        if not ctx.inside(path):
            risky.append(word)
        elif ctx.is_project_or_above(path) and (not is_glob or pattern in ("*", ".*", "*.*")):
            risky.append(word)
    # END_BLOCK_BusinessLogic
    if risky:
        logger.info("[IMP:9][check_rm][MATCH] recursive deletion outside the project or of it: operands=%d", len(risky))
        return "recursive deletion outside the project or of the project itself (%s)" % ", ".join(risky[:3])
    logger.info("[IMP:5][check_rm][CLEAR] no risky operand")
    return None
# endregion FUNC_check_rm


# region FUNC_check_find [DOMAIN(8): Safety; CONCEPT(7): DeletionScope; TECH(5): find]
## @purpose Ask before find with -delete or -exec rm over a start path outside the project, unless every name filter selects a regenerable artefact.
## @uses guard_destructive.Context.resolve, guard_destructive.Context.inside, guard_destructive.REGENERABLE
## @io Input: words list of str, the find command words; ctx Context. Output: rule str naming up to three start paths, or None.
##   Side effects: a trace record on a match. Guarantees: a find that deletes nothing, or whose name filters are all regenerable, returns None; a missing start path means the current directory. Raises: none. System importance: 7.
##   Example: find over a directory outside the project with -name star.csv -delete returns a rule text.
## @complexity 4
def check_find(words, ctx):
    # START_BLOCK_BusinessLogic
    deletes = "-delete" in words or any(
        w in ("-exec", "-execdir", "-ok") and i + 1 < len(words) and os.path.basename(words[i + 1]) == "rm"
        for i, w in enumerate(words))
    if not deletes:
        logger.info("[IMP:5][check_find][NO_DELETE] find does not delete")
        return None
    names = [words[i + 1] for i, w in enumerate(words[:-1]) if w in ("-name", "-iname")]
    if names and all(n in REGENERABLE for n in names):
        logger.info("[IMP:5][check_find][REGENERABLE] every name filter selects a regenerable artefact")
        return None
    starts = []
    for word in words[1:]:
        if word.startswith("-") or word in ("(", "!"):
            break
        starts.append(word)
    risky = []
    for start in starts or ["."]:
        path = ctx.resolve(start)
        if path is not None and not ctx.inside(path):
            risky.append(start)
    # END_BLOCK_BusinessLogic
    if risky:
        logger.info("[IMP:9][check_find][MATCH] deleting find outside the project: start_paths=%d", len(risky))
        return "find deleting outside the project (%s)" % ", ".join(risky[:3])
    logger.info("[IMP:5][check_find][CLEAR] start paths are inside the project")
    return None
# endregion FUNC_check_find


# region FUNC__git_rule [DOMAIN(9): Safety; CONCEPT(9): LossOfUncommittedWork, HistoryRewrite; TECH(7): git probes]
## @purpose Decide, for one git command, whether it loses work: overwriting edited files, cleaning untracked files, hard resets, force pushes, remote ref deletion by push, history rewrites, dropped stashes, forced branch and worktree removal, a forced git rm over edited files. Commands that would lose nothing on the current tree get no rule. The rules match the exact spellings they list: this ask path does not expand an abbreviated long option and does not combine separate short flags, unlike the judge rules. Known limits, all silent: git reset --ha, git clean --f, git push --de, --mir or --forc, git checkout --forc, git switch --disc, git restore --staged --work, git rm --forc, and a forced branch deletion spelled as separate flags or as long options (git branch -d -f, -df, --delete --force), because the branch rule asks only for a short cluster that contains the letter D.
## @uses guard_destructive.Context.git, guard_destructive.Context.resolve
## @io Input: words list of str, the git command words; ctx Context. Output: rule str (with up to three affected paths where a probe found them), or None.
##   Side effects: read-only git probes (status, clean -n, rev-parse). Guarantees: a failing probe on a known directory is silent; an unknown directory asks for the commands that need a probe. Raises: none. System importance: 9.
##   Example: a checkout of a path whose file has uncommitted edits returns a rule naming that file; the same checkout on a clean tree returns None. A push with the delete flag, a refspec that starts with a colon, the mirror flag or the prune flag returns a remote ref deletion rule; a forced git rm asks only over a path that has uncommitted entries and not with the cached flag or a dry run.
## @complexity 10
def _git_rule(words, ctx):
    # START_BLOCK_Validation
    args, git_dir = list(words[1:]), ctx.cwd
    while args and args[0].startswith("-"):
        option = args.pop(0)
        if option == "-C" and args:
            git_dir = ctx.resolve(args.pop(0))
        elif option in ("-c", "--git-dir", "--work-tree") and args:
            args.pop(0)
    if not args:
        return None
    sub, rest = args[0], args[1:]
    # END_BLOCK_Validation

    # START_BLOCK_BusinessLogic
    def dirty(paths=None, untracked=False, where=None):
        # Uncommitted entries under the given paths in the given (or effective) directory.
        where = where or git_dir
        if not where:
            return ["(unknown directory)"]
        extra = [] if untracked else ["--untracked-files=no"]
        out = ctx.git(["status", "--porcelain"] + extra + ["--"] + list(paths or []), where)
        # BUG_FIX_CONTEXT: a failing probe used to ask; outside a repository the command fails as well and loses nothing, so a failing probe on a known directory is silent.
        return [line[3:] for line in (out or "").splitlines() if line.strip()]

    if sub == "push" and any(w in ("--force", "-f", "--force-with-lease") or w.startswith("--force-with-lease=")
                             or (w.startswith("+") and len(w) > 1) for w in rest):
        return "force push"
    # BUG_FIX_CONTEXT: only a force push was asked about, yet a push can also delete remote refs without --force (the delete flag, a refspec that starts with a colon, or a mirror or prune push that removes every remote ref the local repository lacks); a deleted remote branch is not recoverable from the local clone, so the owner is asked. The ordinary push, a push of HEAD to a named ref and a dry run stay silent.
    if sub == "push":
        refspecs = [w for w in rest if not w.startswith("-")][1:]  # the first word is the remote
        if any(w == "--delete" or (w.startswith("-") and not w.startswith("--") and "d" in w) for w in rest):
            return "remote ref deletion (%s)" % ", ".join(refspecs[:3]) if refspecs else "remote ref deletion"
        gone = [w[1:] for w in refspecs if w.startswith(":") and len(w) > 1]
        if gone:
            return "remote ref deletion (%s)" % ", ".join(gone[:3])
        if "--mirror" in rest or "--prune" in rest:
            return "push that deletes the remote refs the local repository lacks"
    if sub in ("filter-repo", "filter-branch") and not any(w in ("--version", "--help", "-h") for w in rest):
        return "history rewrite"
    # BUG_FIX_CONTEXT: git rm without -f refuses a file with uncommitted changes, but git rm -f removes it from the index and the working tree and the edits are lost; only a force over a path with uncommitted entries asks, and --cached or a dry run keeps the file, so they stay silent.
    if sub == "rm" and any(w == "--force" or (w.startswith("-") and not w.startswith("--") and "f" in w) for w in rest):
        keeps = any(w in ("--cached", "--dry-run") or (w.startswith("-") and not w.startswith("--") and "n" in w) for w in rest)
        targets = rest[rest.index("--") + 1:] if "--" in rest else [w for w in rest if not w.startswith("-")]
        lost = [] if keeps or not targets else dirty(targets)
        return ("git rm --force discarding uncommitted changes (%s)" % ", ".join(lost[:3])) if lost else None
    if sub == "branch" and any(w.startswith("-") and not w.startswith("--") and "D" in w for w in rest):
        return "branch deletion with force"
    if sub == "stash" and rest and rest[0] in ("drop", "clear"):
        return "stash %s" % rest[0]
    if sub == "worktree" and rest and rest[0] == "remove" and any(w in ("-f", "--force") for w in rest):
        targets = [w for w in rest[1:] if not w.startswith("-")]
        where = ctx.resolve(targets[0]) if targets else None
        if where is None:
            return "forced worktree removal (unknown path)"
        lost = dirty(untracked=True, where=where) if os.path.isdir(where) else []
        return ("forced worktree removal discarding changes (%s)" % ", ".join(lost[:3])) if lost else None
    if sub == "reset" and "--hard" in rest:
        targets = [w for w in rest if not w.startswith("-")]
        lost = dirty()
        if lost or (targets and targets[0] not in ("HEAD", "@")):
            return "hard reset" + ((" over uncommitted changes (%s)" % ", ".join(lost[:3])) if lost else " to another commit")
        return None
    if sub == "clean" and any((w.startswith("-") and not w.startswith("--") and "f" in w) or w == "--force" for w in rest):
        if not git_dir:
            return "git clean in an unknown directory"
        probe = [w.replace("f", "") for w in rest if w.startswith("-") and not w.startswith("--")]
        probe = [w for w in probe if w not in ("-", "")]
        out = ctx.git(["clean", "-n"] + probe, git_dir)
        victims = [line.replace("Would remove ", "") for line in (out or "").splitlines() if line.strip()]
        if victims:
            return "git clean removing untracked files (%s)" % ", ".join(victims[:3])
        return None
    if sub in ("checkout", "restore", "switch"):
        if sub == "restore" and "--staged" in rest and not any(w in ("--worktree", "-W") for w in rest):
            return None
        force = any(w in ("-f", "--force", "--discard-changes") for w in rest)
        if "--" in rest:
            paths = rest[rest.index("--") + 1:]
        elif sub == "restore":
            paths = [w for w in rest if not w.startswith("-")]
        elif sub == "checkout":
            paths = []
            for w in (w for w in rest if not w.startswith("-")):
                is_ref = bool(git_dir) and ctx.git(["rev-parse", "--verify", "--quiet", "%s^{commit}" % w], git_dir) is not None
                if not is_ref and (w == "." or (git_dir and os.path.exists(os.path.join(git_dir, w)))):
                    paths.append(w)
        else:
            paths = []
        if paths:
            lost = dirty(paths)
            if lost:
                return "git %s discarding uncommitted changes (%s)" % (sub, ", ".join(lost[:3]))
            return None
        if force:
            lost = dirty()
            if lost:
                return "git %s --force discarding uncommitted changes (%s)" % (sub, ", ".join(lost[:3]))
    return None
    # END_BLOCK_BusinessLogic
# endregion FUNC__git_rule


# region FUNC_check_git [DOMAIN(9): Safety; CONCEPT(9): LossOfUncommittedWork; TECH(7): git probes]
## @purpose Ask before git commands that lose work, with an owned trace of the verdict.
## @uses guard_destructive._git_rule
## @io Input: words list of str, the git command words; ctx Context. Output: rule str or None, exactly as the git rule function decides.
##   Side effects: the probes of the rule function and one trace record. Guarantees: the verdict is unchanged by tracing. Raises: none. System importance: 9. Example: a plain git status returns None.
## @complexity 2
def check_git(words, ctx):
    rule = _git_rule(words, ctx)
    if rule:
        logger.info("[IMP:9][check_git][MATCH] git command loses or rewrites work")
    else:
        logger.info("[IMP:5][check_git][CLEAR] git command loses nothing on the current tree")
    return rule
# endregion FUNC_check_git


# region FUNC_check_sql [DOMAIN(8): Safety; CONCEPT(7): DestructiveSQL; TECH(5): regex]
## @purpose Ask before DROP or TRUNCATE sent to a SQL client, as an argument or through the command's own heredoc; the same words written into a file or a test stay silent.
## @uses guard_destructive.SQL_CLIENTS, guard_destructive.SQL_RE
## @io Input: words list of str, the command words; bodies list of str, the heredoc bodies of the whole command. Output: the str destructive SQL, or None.
##   Side effects: a trace record on a match. Guarantees: only a command that names a known SQL client is judged, and only its own heredoc bodies (markers in its words) are read. Raises: none. System importance: 6.
##   Example: a sqlite3 command fed a heredoc holding a table drop returns the rule; a cat command with the same heredoc returns None.
## @complexity 3
def check_sql(words, bodies):
    # START_BLOCK_BusinessLogic
    if not any(os.path.basename(w) in SQL_CLIENTS for w in words):
        return None
    own = [bodies[int(w[3:])] for w in words if w.startswith("<<#") and int(w[3:]) < len(bodies)]
    text = " ".join(w for w in words if not w.startswith("<<#")) + "\n" + "\n".join(own)
    # END_BLOCK_BusinessLogic
    if SQL_RE.search(text):
        logger.info("[IMP:9][check_sql][MATCH] destructive SQL sent to a SQL client")
        return "destructive SQL"
    logger.info("[IMP:5][check_sql][CLEAR] SQL client without a destructive statement")
    return None
# endregion FUNC_check_sql


# region FUNC_classify [DOMAIN(9): Safety; CONCEPT(9): DestructiveClassifier; TECH(7): segmentation]
## @purpose Name the destructive rule a whole command matches, so that the owner sees what is at stake.
## @uses guard_destructive.split_heredocs, guard_destructive.simple_commands, guard_destructive.Context, guard_destructive.check_rm, guard_destructive.check_find, guard_destructive.check_git, guard_destructive.check_sql
## @io Input: command str; project_dir str; cwd str or a Context (a nested shell string reuses the parent context); _depth int nesting guard. Output: rule str for the first destructive simple command, or None.
##   Side effects: git probes through the checks and a trace record on a match. Guarantees: assignments update the context variables, cd moves the effective directory, shell -c strings are classified to depth 2, prefix words such as sudo are skipped. Raises: none for str input. System importance: 9.
##   Example: the text cd sibling-worktree && git checkout -- a.py over an edited a.py returns a checkout rule; the text git status returns None.
## @complexity 7
def classify(command, project_dir, cwd=None, _depth=0):
    # START_BLOCK_BusinessLogic
    ctx = cwd if isinstance(cwd, Context) else Context(project_dir, cwd)
    text, bodies = split_heredocs(command)
    for words in simple_commands(text):
        i = 0
        while i < len(words) and (ASSIGN_RE.match(words[i]) or words[i] in PREFIX_WORDS):
            i += 1
        if i == len(words):
            for word in words:
                name, sep, value = word.partition("=")
                if sep and ASSIGN_RE.match(word):
                    ctx.vars[name] = ctx.expand(value)
            continue
        words = words[i:]
        name = os.path.basename(words[0])
        if name == "cd":
            target = words[1] if len(words) > 1 else os.environ.get("HOME", "")
            ctx.cwd = ctx.resolve(target) if target and target != "-" else None
            continue
        if name in SHELLS and "-c" in words and _depth < 2:
            index = words.index("-c")
            if index + 1 < len(words):
                rule = classify(words[index + 1], project_dir, ctx, _depth + 1)
                if rule:
                    return rule
            continue
        rule = None
        if name == "rm":
            rule = check_rm(words, ctx)
        elif name == "find":
            rule = check_find(words, ctx)
        elif name == "git":
            rule = check_git(words, ctx)
        rule = rule or check_sql(words, bodies)
        if rule:
            logger.info("[IMP:9][classify][MATCH] a destructive rule matched at depth %d", _depth)
            return rule
    # END_BLOCK_BusinessLogic
    logger.info("[IMP:5][classify][CLEAR] no destructive rule matched at depth %d", _depth)
    return None
# endregion FUNC_classify


# region FUNC__expand_long_option [DOMAIN(8): ShellParsing; CONCEPT(9): AbbreviatedLongOption; TECH(5): prefix match]
## @purpose Turn a long option as typed into the option it names, because git and the GNU tools accept any unambiguous prefix of a long option and a guard that compares the exact spelling is bypassed by an abbreviation (the mov prefix of the move option really renames a branch).
## @uses none
## @io Input: name str, a long option without any equals value (it starts with a double dash); known collection of str, the complete long option names of the verb or tool. Output: str canonical option name, or None when name is ambiguous (it prefixes several names and equals none) or unknown (it prefixes none).
##   Side effects: one trace record with the resolution (exact, prefix, ambiguous or unknown) and the candidate count, never the word. Guarantees: an exact name wins even when it prefixes a longer name (unset against unset-all, strip against strip-program); a prefix that matches exactly one name is that name; a bare double dash is ambiguous; the match is case sensitive, as in git and in GNU tools. Completeness of the table matters in one direction only: a name missing from it can make an unknown option of the tool look unknown here, which the callers treat as a change.
##   Raises: none for str input. System importance: 8. Example: the prefix mov in the branch table returns the move option; the prefix co returns None because it prefixes color, column, contains and copy.
## @complexity 3
def _expand_long_option(name, known):
    # START_BLOCK_BusinessLogic
    if name in known:
        resolution, candidates = "exact", [name]
    else:
        candidates = [option for option in known if option.startswith(name)]
        resolution = "prefix" if len(candidates) == 1 else "ambiguous" if candidates else "unknown"
    # END_BLOCK_BusinessLogic
    logger.info("[IMP:4][_expand_long_option][VERDICT] resolution=%s candidates=%d", resolution, len(candidates))
    return candidates[0] if resolution in ("exact", "prefix") else None
# endregion FUNC__expand_long_option


# region FUNC__parse_options [DOMAIN(6): ShellParsing; CONCEPT(6): OptionSplit; TECH(5): argument scan]
## @purpose Split the words of one command into option flags, option values and operands, so that a rule judges only the operands a command writes and never the value of an option such as a size, a mode or a reference file.
## @uses guard_destructive._expand_long_option
## @io Input: words list of str, the command words including the command name; short_values str of short option letters that take a value; long_values tuple of long option names that take a value; known_long collection of str with the complete long option names of the tool, or None; short_suffix str of short option letters whose attached rest is an optional argument and not further switches (the in-place letter of sed, whose attached rest is the backup suffix), empty by default. Output: tuple of (flags set of str, values list of (option, value) tuples, operands list of str).
##   Side effects: one trace record with the three counts and no word, plus one per long option when known_long is given. Guarantees: a value is the rest of the same word or the next word; a long option may carry its value after an equals sign; a lone dash and every word after a double dash are operands; a short cluster is read letter by letter and ends at the first letter that takes a value or at a letter named in short_suffix (the rest of the word is then neither a switch nor an operand); with known_long every long option is expanded to its canonical name first (so an abbreviated value option still takes its value), and an ambiguous or unknown long option stays in the flags as typed, which is how a caller finds it.
##   Raises: none for str input. System importance: 5. Example: for the words truncate, -s, 0, f the flags hold -s, the values hold the pair (-s, 0) and the operands hold f; with known_long the words ln, --target-d, d, a give the pair (--target-directory, d) and the operand a.
## @complexity 6
def _parse_options(words, short_values="", long_values=(), known_long=None, short_suffix=""):
    flags, values, operands = set(), [], []
    index, options_ended = 1, False
    while index < len(words):
        word = words[index]
        index += 1
        if options_ended or not word.startswith("-") or word == "-":
            operands.append(word)
        elif word == "--":
            options_ended = True
        elif word.startswith("--"):
            name, equals, value = word.partition("=")
            if known_long is not None:
                name = _expand_long_option(name, known_long) or name
            flags.add(name)
            if name in long_values:
                if equals:
                    values.append((name, value))
                elif index < len(words):
                    values.append((name, words[index]))
                    index += 1
        else:
            for position, letter in enumerate(word[1:], 1):
                flags.add("-" + letter)
                if letter in short_values:
                    rest = word[position + 1:]
                    if rest:
                        values.append(("-" + letter, rest))
                    elif index < len(words):
                        values.append(("-" + letter, words[index]))
                        index += 1
                    break
                if letter in short_suffix:
                    break
    logger.info("[IMP:4][_parse_options][RESULT] flags=%d values=%d operands=%d", len(flags), len(values), len(operands))
    return flags, values, operands
# endregion FUNC__parse_options


# region FUNC__git_config_writes [DOMAIN(8): Git; CONCEPT(8): ConfigWriteVersusRead; TECH(6): option scan]
## @purpose Tell a git config call that writes configuration from one that only reads it, because the judge may query the configuration but a write changes how the judged repository behaves.
## @uses guard_destructive._parse_options, guard_destructive.CONFIG_LONG_OPTIONS, guard_destructive.Context.resolve, guard_destructive.Context.in_project
## @io Input: rest list of str, the words after the config verb; ctx Context. Output: bool, True when the call writes into a configuration file that is not a scratch file named by the file option.
##   Side effects: trace records, among them one for a long option that could not be resolved. Guarantees: every long option is expanded by unique prefix against the real option table of git config first (the rem prefix of the remove-section option is that option); the read flags (get forms, list), the get and list verbs and a single bare key are reads; the write flags, the set, unset, rename-section, remove-section and edit verbs and a key with a value are writes; a write flag wins over a read flag; a long option that is neither a known name nor a unique prefix of one (an ambiguous or unknown prefix) is a write, because the judge cannot know otherwise; a file option that resolves outside every project root makes the write harmless.
##   Raises: none for str input. System importance: 8. Example: key and value return True; the get flag with a key returns False; the unset-a prefix with a key returns True; the get-a prefix with a key returns False.
## @complexity 7
def _git_config_writes(rest, ctx):
    # START_BLOCK_BusinessLogic
    flags, values, positionals = _parse_options(["config"] + list(rest), short_values="f",
                                                long_values=("--file", "--blob", "--type", "--default", "--comment"),
                                                known_long=CONFIG_LONG_OPTIONS)
    if any(flag.startswith("--") and flag not in CONFIG_LONG_OPTIONS for flag in flags):
        writes = True
        logger.info("[IMP:5][_git_config_writes][UNKNOWN_OPTION] a long option that is neither known nor a unique prefix: a write is assumed")
    elif flags & CONFIG_WRITE_FLAGS:
        writes = True
    elif flags & CONFIG_READ_FLAGS:
        writes = False
    elif positionals and positionals[0] in CONFIG_WRITE_VERBS:
        writes = True
    elif positionals and positionals[0] in CONFIG_READ_VERBS:
        writes = False
    else:
        writes = len(positionals) >= 2
    if writes:
        for option, value in values:
            if option in ("--file", "-f"):
                path = ctx.resolve(value)
                if path and not ctx.in_project(path):
                    logger.info("[IMP:5][_git_config_writes][SCRATCH_FILE] config write goes to a file outside the project")
                    return False
    # END_BLOCK_BusinessLogic
    logger.info("[IMP:5][_git_config_writes][VERDICT] writes=%s", writes)
    return writes
# endregion FUNC__git_config_writes


# region FUNC__git_branch_changes [DOMAIN(8): Git; CONCEPT(8): BranchListVersusChange; TECH(6): option scan]
## @purpose Tell a git branch call that creates, deletes, renames, copies or re-points a branch from one that only lists branches, because the judge may look at the branches it verifies but any other form moves a ref.
## @uses guard_destructive._expand_long_option, guard_destructive.BRANCH_LONG_OPTIONS, guard_destructive.BRANCH_CHANGE_LONG, guard_destructive.BRANCH_CHANGE_LETTERS, guard_destructive.BRANCH_LIST_LONG, guard_destructive.BRANCH_LIST_LETTERS, guard_destructive.BRANCH_VALUE_LONG
## @io Input: rest list of str, the words after the branch verb. Output: bool, True when the call can change a ref.
##   Side effects: one trace record with the mode and the operand count, never a word, plus the records of the option expansion. Guarantees: every long option is expanded by unique prefix against the real option table of git branch first (the mov prefix is the move option); an option that changes a ref (delete, move, copy, force, edit-description, set-upstream-to, unset-upstream, or the letters d, D, m, M, c, C, f, u anywhere in a short cluster) always wins; a long option that is neither a known name nor a unique prefix of one (ambiguous or unknown) also makes the call a change, because the judge cannot know otherwise; otherwise an option that selects the list mode (list, show-current, contains, no-contains, merged, no-merged, points-at, or the letter l) makes every bare word a pattern or a value; the all, remotes and verbose flags and the filter and display options do not select the list mode, so a bare word after them is a branch name; the sort, format and points-at options take the next word as their value; with none of these a bare word is a branch name and the call changes a ref. A word after a double dash and a lone dash are bare words.
##   Raises: none for str input. System importance: 8. Example: the contains option and a commit return False; a branch name alone returns True; the verbose flag with a name returns True; the all flag with the mov prefix and two names returns True; the all flag with a name returns True.
## @complexity 7
def _git_branch_changes(rest):
    # START_BLOCK_BusinessLogic
    changes_flag, lists, unresolved, operands, options_ended, takes_value = False, False, False, 0, False, False
    for word in rest:
        if takes_value:
            takes_value = False
        elif options_ended or not word.startswith("-") or word == "-":
            operands += 1
        elif word == "--":
            options_ended = True
        elif word.startswith("--"):
            name, equals, _ = word.partition("=")
            canonical = _expand_long_option(name, BRANCH_LONG_OPTIONS)
            if canonical is None:
                unresolved = True
                continue
            changes_flag = changes_flag or canonical in BRANCH_CHANGE_LONG
            lists = lists or canonical in BRANCH_LIST_LONG
            takes_value = canonical in BRANCH_VALUE_LONG and not equals
        else:
            changes_flag = changes_flag or any(letter in BRANCH_CHANGE_LETTERS for letter in word[1:])
            lists = lists or any(letter in BRANCH_LIST_LETTERS for letter in word[1:])
    if changes_flag:
        changes, mode = True, "change-option"
    elif unresolved:
        changes, mode = True, "unknown-option"
    elif lists:
        changes, mode = False, "list-option"
    elif operands:
        changes, mode = True, "branch-name"
    else:
        changes, mode = False, "no-operand"
    # END_BLOCK_BusinessLogic
    logger.info("[IMP:5][_git_branch_changes][VERDICT] changes=%s mode=%s operands=%d", changes, mode, operands)
    return changes
# endregion FUNC__git_branch_changes


# region FUNC__perl_in_place_files [DOMAIN(7): ShellParsing; CONCEPT(7): InPlaceEdit; TECH(5): switch cluster scan]
## @purpose Find the files a perl in-place edit rewrites, so that a judge is kept from editing the tree with perl as it is kept from doing so with sed.
## @uses none
## @io Input: words list of str, the perl command words. Output: list of str file operands when perl runs with the in-place switch, otherwise None.
##   Side effects: one trace record with the verdict and the file count. Guarantees: switch clusters are read letter by letter, so a module switch such as the strict module does not look like the in-place switch; the scan ends at the first word that is not a switch, which is then the script file unless a code switch was given. Raises: none for str input.
##   System importance: 6. Example: the words perl, -pi, -e, a script, a file return the file; the words perl, -ne, a script return None.
## @complexity 6
def _perl_in_place_files(words):
    # START_BLOCK_BusinessLogic
    in_place, has_code, index = False, False, 1
    while index < len(words):
        word = words[index]
        if word == "--":
            index += 1
            break
        if not word.startswith("-") or word == "-":
            break
        index += 1
        if word.startswith("--"):
            continue
        for position, letter in enumerate(word[1:], 1):
            if letter == "i":
                in_place = True
                break
            if letter in "eE":
                has_code = True
                if position == len(word) - 1:
                    index += 1  # the code is the next word
                break
            if letter in "MmIFdDCVxX":
                break  # the rest of the word is an argument of this switch
    # END_BLOCK_BusinessLogic
    if not in_place:
        logger.info("[IMP:5][_perl_in_place_files][VERDICT] in_place=False files=0")
        return None
    rest = list(words[index:])
    files = rest if has_code else rest[1:]
    logger.info("[IMP:5][_perl_in_place_files][VERDICT] in_place=True files=%d", len(files))
    return files
# endregion FUNC__perl_in_place_files


# region FUNC__written_operands [DOMAIN(8): Safety; CONCEPT(8): WrittenOperands, ReadOnlyJudge; TECH(6): option scan]
## @purpose Name, for the file commands a judge must not run on the project, the operands each command writes: the files whose mode, owner or content changes and the places where a link or an installed file appears.
## @uses guard_destructive._parse_options, guard_destructive._expand_long_option, guard_destructive._perl_in_place_files, guard_destructive.OWNERSHIP_FLAGS_RE
## @io Input: name str, the command name; words list of str, the command words. Output: list of str operands the command writes (possibly empty), or None when the name is not one of the judged file commands or perl runs without the in-place switch.
##   Side effects: one trace record with the writing flag, the command name when it writes and the operand count, never an operand. Guarantees: the mode or owner word of chmod, chown and chgrp is not an operand and a reference option makes every operand a target; the size and reference values of truncate are not targets; dd gives its of values; ln and install give the destination (the target directory option, the last operand, or the current directory for a single link operand; every operand for install with the directory flag). The long options of the GNU tools are expanded by unique prefix first (the ref prefix of the reference option, the target prefix of the target-directory option), because getopt_long accepts any unambiguous prefix; an ambiguous or unknown prefix stays a plain flag, since the tool itself rejects it.
##   Raises: none for str input. System importance: 8. Example: chmod with a mode and one file returns that file; ln with a target and a link name returns the link name.
## @complexity 8
def _written_operands(name, words):
    # START_BLOCK_BusinessLogic
    operands = None
    if name in ("chmod", "chown", "chgrp"):
        written, skip_next, reference = [], False, False
        for word in words[1:]:
            if skip_next:
                skip_next = False
            elif word.startswith("--") and _expand_long_option(word.partition("=")[0], CHMOD_LONG) == "--reference":
                reference, skip_next = True, "=" not in word
            elif not (word.startswith("--") or OWNERSHIP_FLAGS_RE.match(word)):
                written.append(word)
        operands = written if reference else written[1:]  # without a reference the first word is the mode or the owner
    elif name == "truncate":
        operands = _parse_options(words, short_values="sr", long_values=("--size", "--reference"), known_long=TRUNCATE_LONG)[2]
    elif name == "perl":
        operands = _perl_in_place_files(words)
    elif name == "dd":
        operands = [word[3:] for word in words[1:] if word.startswith("of=") and len(word) > 3]
    elif name == "ln":
        _, values, written = _parse_options(words, short_values="St", long_values=("--suffix", "--target-directory"), known_long=LN_LONG)
        directory = [value for option, value in values if option in ("-t", "--target-directory")]
        if directory:
            operands = directory[-1:]
        else:
            operands = written[-1:] if len(written) > 1 else (["."] if written else [])
    elif name == "install":
        flags, values, written = _parse_options(words, short_values="mogt",
                                                long_values=("--mode", "--owner", "--group", "--target-directory", "--suffix", "--strip-program"),
                                                known_long=INSTALL_LONG)
        directory = [value for option, value in values if option in ("-t", "--target-directory")]
        if "-d" in flags or "--directory" in flags:
            operands = written
        else:
            operands = directory[-1:] if directory else written[-1:]
    # END_BLOCK_BusinessLogic
    logger.info("[IMP:5][_written_operands][VERDICT] writing=%s command=%s operands=%d",
                operands is not None, name if operands is not None else "-", len(operands or []))
    return operands
# endregion FUNC__written_operands


# region FUNC__sed_in_place [DOMAIN(7): ShellParsing; CONCEPT(8): InPlaceEdit, AbbreviatedLongOption; TECH(5): option scan]
## @purpose Tell a sed call that rewrites its files in place from one that only prints, so that a judge is kept from editing the tree with sed in any spelling of the switch.
## @uses guard_destructive._parse_options, guard_destructive.SED_LONG
## @io Input: words list of str, the sed command words. Output: bool, True when the call carries the in-place switch.
##   Side effects: one trace record with the verdict and the records of the option scan. Guarantees: a short cluster is read letter by letter and ends at the first letter that takes a value (e, f, l), so the switch is found inside a cluster (Ei, ni, nEi) and a letter i inside a script, a script file or a value is not the switch; the long form is found abbreviated (the in prefix of in-place). Raises: none for str input.
##   System importance: 7. Example: the words sed, -Ei, a script, a file return True; the words sed, -n, a script that holds the letter i, a file return False.
## @complexity 3
def _sed_in_place(words):
    # BUG_FIX_CONTEXT: the judge rule tested the text of each word (starts with the dash and the letter i), so a cluster such as -Ei or -ni and the long in-place form, abbreviated or not, rewrote project files without a decision; the scan is the cluster scan of _parse_options.
    flags, _, _ = _parse_options(words, short_values="efl", long_values=("--expression", "--file", "--line-length"), known_long=SED_LONG)
    in_place = "-i" in flags or "--in-place" in flags
    logger.info("[IMP:5][_sed_in_place][VERDICT] in_place=%s", in_place)
    return in_place
# endregion FUNC__sed_in_place


# region FUNC__sed_files [DOMAIN(8): ShellParsing; CONCEPT(9): OperandSelection, InPlaceEdit; TECH(5): option scan]
## @purpose Name the files a sed in-place call rewrites, so that the judge rule looks at the files and never at the script: the first word that is not an option is the script only when the script was not given by an expression or a script file option, in any spelling of that option (attached to the short letter, after a cluster, the long form attached or separate, the long form abbreviated).
## @uses guard_destructive._parse_options, guard_destructive.SED_LONG
## @io Input: words list of str, the sed command words. Output: list of str, the operands that are files (possibly empty).
##   Side effects: one trace record with the script flag and the operand count, never a word, plus the records of the option scan. Guarantees: the values of the expression, script file and line length options are never files; the rest of a word that carries the in-place letter is its backup suffix, so a suffix that holds a value letter of sed (a suffix such as tmpl) does not swallow the next word; without an expression or script file option the first operand is the script and is dropped; with one every operand is a file; every word after a double dash is an operand. An empty suffix word of the BSD form stays the first operand and is dropped as the script word.
##   Raises: none for str input. System importance: 8. Example: the words sed, -i, an expression option with an attached script and a file give the file; the words sed, -i, a script and a file give the file.
## @complexity 3
def _sed_files(words):
    # BUG_FIX_CONTEXT: the judge rule took the first word that does not start with a dash for the script and dropped it, so with the script attached to the expression option (-e's/1/2/', -Ei -es/1/2/, --expression=s/1/2/, in either position) the first word was the file itself, the file was dropped and the in-place edit passed silently. The operands now come from the option scan of _parse_options, which consumes the value of the expression, script file and line length options, and the first operand is dropped as the script only when none of the expression or script file options was given. The in-place letter ends its cluster (short_suffix) because the rest of the word is the backup suffix: without that, a suffix such as tmpl would take the script word as the value of its trailing value letter and the file would again be dropped as the script.
    flags, _, operands = _parse_options(words, short_values="efl", long_values=("--expression", "--file", "--line-length"),
                                        known_long=SED_LONG, short_suffix="i")
    script_given = bool(flags & {"-e", "-f", "--expression", "--file"})
    files = operands if script_given else operands[1:]
    logger.info("[IMP:5][_sed_files][VERDICT] script_given=%s operands=%d", script_given, len(files))
    return files
# endregion FUNC__sed_files


# region FUNC__copy_move_operands [DOMAIN(8): Safety; CONCEPT(8): WrittenOperands, TargetDirectory; TECH(6): option scan]
## @purpose Name the operands a cp or mv call writes, so that the target directory option (short or long, abbreviated or not) is never mistaken for a source: cp writes its last operand or the target directory, mv removes every source and writes the target directory.
## @uses guard_destructive._parse_options, guard_destructive.CP_MV_LONG
## @io Input: name str, cp or mv; words list of str, the command words. Output: list of str operands the call writes.
##   Side effects: one trace record with the command name and the operand count, never an operand. Guarantees: with the target directory option cp writes only that directory (the sources are read) and mv writes every operand and that directory; without it cp writes its last operand and mv every operand; the long option is expanded by unique prefix first; words after a double dash are operands.
##   Raises: none for str input. System importance: 8. Example: cp with -t, a directory and a file returns the directory; mv with the same words returns the file and the directory.
## @complexity 4
def _copy_move_operands(name, words):
    # BUG_FIX_CONTEXT: the rule took the last non-option word of a cp as its destination and ignored the target directory option, so cp with -t or the long form (abbreviated or not) wrote into the project while the destination looked like the source; a mv with the attached long form lost its directory.
    _, values, operands = _parse_options(words, short_values="St", long_values=("--suffix", "--target-directory"), known_long=CP_MV_LONG)
    directory = [value for option, value in values if option in ("-t", "--target-directory")][-1:]
    written = (directory or operands[-1:]) if name == "cp" else operands + directory
    logger.info("[IMP:5][_copy_move_operands][VERDICT] command=%s operands=%d", name, len(written))
    return written
# endregion FUNC__copy_move_operands


# region FUNC__touches_project [DOMAIN(8): Safety; CONCEPT(8): TreeScope; TECH(5): path resolution]
## @purpose Decide whether a written operand lands in the project or one of its worktrees, looking at the entry itself and, for a link or an installed file, at the directory that receives it.
## @uses guard_destructive.Context.resolve, guard_destructive.Context.in_project
## @io Input: name str, the command name; operand str; ctx Context. Output: bool, True when the operand resolves into the project. An operand that cannot be resolved statically counts as outside.
##   Side effects: one trace record with the command name and the verdict, never the path. Guarantees: for ln and install the entry is also judged by its parent directory and file name, so replacing a symbolic link that points outside the project still counts as a write into the project. Raises: none for str input.
##   System importance: 8. Example: a link name in the current project directory returns True; a link name under a scratch root returns False.
## @complexity 4
def _touches_project(name, operand, ctx):
    paths = []
    resolved = ctx.resolve(operand)
    if resolved:
        paths.append(resolved)
    if name in ("ln", "install"):
        entry = operand.rstrip("/")
        parent = ctx.resolve(os.path.dirname(entry) or ".")
        if parent and os.path.basename(entry):
            paths.append(os.path.join(parent, os.path.basename(entry)))
    touches = any(not path.startswith("/dev/") and ctx.in_project(path) for path in paths)
    logger.info("[IMP:5][_touches_project][VERDICT] command=%s touches=%s", name, touches)
    return touches
# endregion FUNC__touches_project


# region FUNC_classify_readonly [DOMAIN(9): Safety; CONCEPT(9): ReadOnlyJudge, StateMutation; TECH(7): segmentation]
## @purpose Keep a read-only agent (a judge) from changing the tree or the git state it judges: the git commands of the recognized verbs that move the index, the working tree or refs, exactly these: the verbs of the closed list MUTATING_GIT (commit, checkout, switch, restore, reset, clean, add, rm, mv, merge, rebase, cherry-pick, revert, apply, am, pull, push, fetch, update-ref; every fetch is denied, the dry run included), and by form worktree add, remove, prune, move, lock, unlock and repair, config writes, stash (bare, or with any verb except list and show), branch creation, deletion, rename, copy, force and upstream changes, and tag creation and deletion; writes by redirection, rm, mv, cp (the target directory option included), tee, touch or sed in place (in any spelling: -i, a cluster such as -Ei, the long form abbreviated or not, the script given by an expression or script file option included) on project paths, and chmod, chown, chgrp, truncate, perl in-place edits, dd of=, ln and install into the project (the candidate digest includes file modes). The same commands in a scratch copy, a redirect, tee or cp of the judge's own report or log into a scratch root outside the project, read-only git queries (config get and list, worktree list, branch listing, status, log, diff) and cache clean-up, stay allowed. Only the project and its worktrees count: any path outside them is silent for this rule whether or not it is under a scratch prefix, and no scratch prefix exempts a path inside them. The guard cannot tell a granted evidence root that lies inside the project (the evidence directory of the project included) from project files, so a write there is still denied. Known limit: the git verbs outside the list above are NOT intercepted, although some of them change the tree, the index, refs or the object store: bisect, symbolic-ref, update-index, checkout-index, read-tree, notes add, remote add and remove, reflog expire, gc, prune, pack-refs, sparse-checkout set, submodule update, replace, maintenance run, hash-object -w, format-patch -o and archive -o; the orchestrator's before and after git status comparison of the tree is the backstop for them.
## @uses guard_destructive.split_heredocs, guard_destructive.simple_commands, guard_destructive.Context.in_project, guard_destructive.check_find, guard_destructive._git_config_writes, guard_destructive._git_branch_changes, guard_destructive._written_operands, guard_destructive._sed_in_place, guard_destructive._sed_files, guard_destructive._copy_move_operands, guard_destructive._touches_project, guard_destructive.MUTATING_GIT, guard_destructive.WORKTREE_CHANGES, guard_destructive.JUDGE_FILE_COMMANDS, guard_destructive.REGENERABLE
## @io Input: command str; project_dir str; cwd str or a Context; _depth int nesting guard. Output: str naming the first tree-changing action found (for example the git verb or the redirection target), or None.
##   Side effects: git probes for the project roots and a trace record on a match. Guarantees: only paths inside the project or its worktrees count; /dev targets and regenerable names are allowed; shell -c strings are examined to depth 2; a git verb that runs in a directory outside the project (a scratch copy) is allowed. Raises: none for str input. System importance: 9.
##   Example: a redirection that writes a file inside the project returns a rule text; the same redirection into a scratch directory returns None.
## @complexity 10
def classify_readonly(command, project_dir, cwd, _depth=0):
    # START_BLOCK_BusinessLogic
    ctx = cwd if isinstance(cwd, Context) else Context(project_dir, cwd)
    text, _ = split_heredocs(command)
    for words, targets in simple_commands(text, with_redirects=True):
        i = 0
        while i < len(words) and (ASSIGN_RE.match(words[i]) or words[i] in PREFIX_WORDS):
            i += 1
        if i == len(words):
            for word in words:
                name, sep, value = word.partition("=")
                if sep and ASSIGN_RE.match(word):
                    ctx.vars[name] = ctx.expand(value)
        for target in targets:
            path = ctx.resolve(target)
            if path and not path.startswith("/dev/") and ctx.in_project(path):
                logger.info("[IMP:9][classify_readonly][MATCH] write by redirection into the project")
                return "writing %s by redirection" % target
        words = words[i:]
        if not words:
            continue
        name = os.path.basename(words[0])
        if name == "cd":
            target = words[1] if len(words) > 1 else os.environ.get("HOME", "")
            ctx.cwd = ctx.resolve(target) if target and target != "-" else None
            continue
        if name in SHELLS and "-c" in words and _depth < 2:
            index = words.index("-c")
            rule = classify_readonly(words[index + 1], project_dir, ctx, _depth + 1) if index + 1 < len(words) else None
            if rule:
                return rule
            continue
        if name == "git":
            args, git_dir = list(words[1:]), ctx.cwd
            while args and args[0].startswith("-"):
                option = args.pop(0)
                if option == "-C" and args:
                    git_dir = ctx.resolve(args.pop(0))
                elif option in ("-c", "--git-dir", "--work-tree") and args:
                    args.pop(0)
            if not args:
                continue
            sub_, rest = args[0], args[1:]
            # BUG_FIX_CONTEXT: worktree add, remove, prune and move, and config writes, changed git state a judge must not touch (roles/qa.md QA-204 and QA-205, flow/delegation.md DELEG-301) and passed silently; the read forms (worktree list, config get and list, a bare key) stay allowed, so these two verbs are judged by form and the rest by verb. Branch joined them in 1.0.2: the listing forms (list, contains, merged, no-merged, points-at, show-current, and with no name the all, remotes, verbose, sort, format and display options) were denied by the verb alone and are read-only checks a judge needs; creation, deletion, rename, copy, force and upstream changes stay denied. In 1.0.3 the long options of branch and config are expanded by unique prefix first (git takes any unambiguous prefix, so the all flag with the mov prefix renamed a branch and the rem prefix of git config removed a section while both were silent), an unknown or ambiguous long option of either verb is a change, and the all and remotes flags (-a, -r) are no longer taken for the list mode. Fetch is NOT judged by form: the dry run still writes objects, so the verb is denied whole (MUTATING_GIT).
            mutates = (sub_ in MUTATING_GIT
                       or (sub_ == "worktree" and bool(rest) and rest[0] in WORKTREE_CHANGES)
                       or (sub_ == "config" and _git_config_writes(rest, ctx))
                       or (sub_ == "stash" and (not rest or rest[0] not in ("list", "show")))
                       or (sub_ == "branch" and _git_branch_changes(rest))
                       or (sub_ == "tag" and not any(w in ("-l", "--list", "-n", "--contains", "--points-at") for w in rest)
                           and any(not w.startswith("-") or w in ("-d", "-a", "-s", "-f") for w in rest)))
            if mutates and (git_dir is None or ctx.in_project(git_dir)):
                logger.info("[IMP:9][classify_readonly][MATCH] tree-changing git verb in the project")
                return "git %s" % sub_
            continue
        if name in ("rm", "mv", "cp", "tee", "touch") or (name == "sed" and _sed_in_place(words)):
            if name in ("cp", "mv"):
                operands = _copy_move_operands(name, words)
            elif name == "sed":
                # BUG_FIX_CONTEXT: the first non-dash word was dropped as the script, which dropped the file when the script was attached to the expression option; _sed_files drops it only when no expression or script file option was given.
                operands = _sed_files(words)
            else:
                operands = [w for w in words[1:] if not w.startswith("-")]
            for operand in operands:
                if os.path.basename(operand.rstrip("/")) in REGENERABLE:
                    continue
                path = ctx.resolve(operand)
                if path and ctx.in_project(path):
                    logger.info("[IMP:9][classify_readonly][MATCH] file command on a project path")
                    return "%s %s" % (name, operand)
        # BUG_FIX_CONTEXT: chmod, chown, chgrp, truncate, perl -i, dd of=, ln and install changed the tree or the file modes (the candidate digest includes modes) and were not judged, while rm, mv, cp, tee, touch and sed -i were; the operands each command writes come from _written_operands, so a mode, a size or a reference file is never taken for a target, and a scratch root outside the project stays allowed.
        if name in JUDGE_FILE_COMMANDS:
            for operand in _written_operands(name, words) or []:
                if os.path.basename(operand.rstrip("/")) in REGENERABLE:
                    continue
                if _touches_project(name, operand, ctx):
                    logger.info("[IMP:9][classify_readonly][MATCH] %s writes a project path", name)
                    return {"dd": "dd of=%s", "perl": "perl -i %s"}.get(name, name + " %s") % operand
        if name == "find" and check_find(words, ctx) is None and ("-delete" in words or "rm" in words):
            names = [words[k + 1] for k, w in enumerate(words[:-1]) if w in ("-name", "-iname")]
            starts = [w for w in words[1:] if not w.startswith("-")][:1] or ["."]
            path = ctx.resolve(starts[0])
            if not (names and all(n in REGENERABLE for n in names)) and path and ctx.in_project(path):
                logger.info("[IMP:9][classify_readonly][MATCH] deleting find in the project")
                return "find deleting in the project"
    # END_BLOCK_BusinessLogic
    logger.info("[IMP:5][classify_readonly][CLEAR] no tree-changing action at depth %d", _depth)
    return None
# endregion FUNC_classify_readonly


# region FUNC_guard_active [DOMAIN(7): Scope; CONCEPT(7): OwnerSwitch; TECH(5): environment]
## @purpose Let the owner switch the whole guard off with one environment value; otherwise the guard is active whenever the plugin is loaded.
## @uses os.environ
## @io Input: none (reads METHODOLOGY_GUARD_SCOPE). Output: bool; False exactly when the value, compared case-insensitively, is off. Any other value, including unset, all and unknown words, keeps the guard on.
##   Side effects: a trace record. Guarantees: an unrecognised value never disables the guard. Raises: none. System importance: 7. Example: the value OFF returns False; no value returns True.
## @complexity 2
def guard_active():
    scope = os.environ.get("METHODOLOGY_GUARD_SCOPE", "all").strip().lower()
    if scope == "off":
        logger.info("[IMP:6][guard_active][SWITCHED_OFF] METHODOLOGY_GUARD_SCOPE is off")
        return False
    return True
# endregion FUNC_guard_active


# region FUNC_readonly_agents [DOMAIN(8): Safety; CONCEPT(8): ReadOnlyJudge; TECH(5): environment]
## @purpose Name the agent types that are read-only for this run: the judges qa, reviewer and searcher in plain and plugin-namespaced form, unless the owner replaced the list.
## @uses guard_destructive.DEFAULT_READONLY, os.environ
## @io Input: none (reads METHODOLOGY_GUARD_READONLY_AGENTS). Output: set of lower-case agent type str. A set variable, even an empty one, replaces the defaults entirely; entries are comma separated, trimmed and lower-cased.
##   Side effects: none. Guarantees: the default set holds six names. Raises: none. System importance: 8. Example: unset returns the six defaults; the value auditor returns a set holding only auditor.
## @complexity 2
def readonly_agents():
    configured = os.environ.get("METHODOLOGY_GUARD_READONLY_AGENTS")
    if configured is None:
        return set(DEFAULT_READONLY)
    return {name.strip().lower() for name in configured.split(",") if name.strip()}
# endregion FUNC_readonly_agents


# region FUNC__configure_logging [DOMAIN(5): Diagnostics; CONCEPT(5): OptInTrace; TECH(5): logging, stderr]
## @purpose Keep the hook silent on stderr by default and attach a plain trace handler only when the owner asks for it.
## @uses logging.StreamHandler, logging.getLevelName
## @io Input: environ mapping; METHODOLOGY_HOOK_LOG selects the level by name and any other nonempty value means INFO. Output: the attached logging.Handler, or None when the variable is unset or empty.
##   Side effects: attaches one handler writing bare messages to stderr and sets the logger level. Guarantees: unset means no output at all, because the module logger carries a null handler. Raises: none. System importance: 5. Example: the value DEBUG attaches a handler at DEBUG.
## @complexity 3
def _configure_logging(environ):
    setting = environ.get(HOOK_LOG_ENV, "")
    if not setting:
        return None
    level = logging.getLevelName(setting.upper())
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)
    logger.setLevel(level if isinstance(level, int) else logging.INFO)
    return handler
# endregion FUNC__configure_logging


# region FUNC_main [DOMAIN(8): Hooks; CONCEPT(9): PermissionDecision, NeverFailSession; TECH(6): json, stdin]
## @purpose Read the hook payload and answer with a permission decision for a destructive command or for a tree-changing command of a read-only agent; stay silent otherwise and never fail the session.
## @uses guard_destructive.guard_active, guard_destructive.readonly_agents, guard_destructive.classify, guard_destructive.classify_readonly, guard_destructive._configure_logging, json.loads, json.dumps
## @io Input: stdin text stream (default sys.stdin) holding the hook JSON; stdout text stream (default sys.stdout). Output: int 0 always; at most one JSON line with hookSpecificOutput, hookEventName PreToolUse, permissionDecision and permissionDecisionReason.
##   Side effects: git probes through the classifiers, one stdout line on a decision, an opt-in stderr trace; the attached handler is removed at the end. Guarantees: other tools, invalid payloads, a switched-off guard and internal errors give no output; a read-only agent is denied, never asked; the reason never contains the command text.
##   Raises: none; every error is caught and traced at IMP:10 when tracing is on. System importance: 9. Example: a payload with a force push returns 0 after writing an ask decision.
## @complexity 6
def main(stdin=None, stdout=None):
    handler = _configure_logging(os.environ)
    stream = sys.stdout if stdout is None else stdout
    try:
        # START_BLOCK_Validation
        payload = json.loads((sys.stdin if stdin is None else stdin).read() or "{}")
        if payload.get("tool_name") != "Bash":
            return 0
        command = (payload.get("tool_input") or {}).get("command", "")
        project_dir = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or ""
        if not guard_active():
            return 0
        # END_BLOCK_Validation
        # START_BLOCK_BusinessLogic
        agent_type = str(payload.get("agent_type") or "").lower()
        if agent_type in readonly_agents():
            mutation = classify_readonly(command, project_dir, payload.get("cwd") or project_dir)
            if mutation:
                reason = ("Read-only agent (%s) must not change the tree it verifies (%s). Run any check that writes in your granted "
                          "scratch root, on a copy without .git (rsync -a --exclude .git SRC/ SCRATCH/, or "
                          "git archive HEAD | tar -x -C SCRATCH)." % (agent_type, mutation))
                stream.write(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                                                "permissionDecisionReason": reason}}) + "\n")
                logger.info("[IMP:9][main][DECISION] deny read-only agent %s", agent_type)
                return 0
        rule = classify(command, project_dir, payload.get("cwd") or project_dir)
        if not rule:
            logger.info("[IMP:5][main][ALLOW] no destructive rule matched")
            return 0
        decision = "deny" if os.environ.get("METHODOLOGY_GUARD_MODE", "ask").lower() == "deny" else "ask"
        reason = ("Destructive command (%s). The owner confirms irreversible actions (neutral process/safety.md); "
                  "state the intent before running it." % rule)
        stream.write(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": decision,
                                                        "permissionDecisionReason": reason}}) + "\n")
        logger.info("[IMP:9][main][DECISION] %s", decision)
        # END_BLOCK_BusinessLogic
    # START_BLOCK_ErrorHandling
    except Exception as error:  # the hook must never break a session
        logger.error("[IMP:10][main][FAIL] kind=%s", type(error).__name__)
    # END_BLOCK_ErrorHandling
    finally:
        if handler is not None:
            logger.removeHandler(handler)
    return 0
# endregion FUNC_main


if __name__ == "__main__":
    sys.exit(main())
