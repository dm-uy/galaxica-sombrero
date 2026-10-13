---
id: checks.conform
title: The conform tool
status: draft
---

# The conform tool

`conform` is the one command that says whether this repository is fit to publish and whether a harness's adapter keeps
the contract. It carries no norm: the norms it checks live in `FORMAT.md` (FMT-1 to FMT-39), and this file describes the
tool that checks them.

<!-- anchor: checks.conform.purpose -->

## What it is for

The tool answers two questions with a verdict a script can read.

1. **Is this repository sound and clean?** The `self` mode reads every neutral file and checks its format (cards,
   anchors, norms, capability and parameter calls, the version), then scans every text file of the repository for what
   must never be published: an absolute home path, a path from the home directory, an e-mail address, and any word of a
   private deny list the owner supplies.
2. **Does a harness's adapter keep the contract?** The `adapter` mode reads an adapter file and the copy of this
   repository it names, and checks that the adapter accounts for every neutral file, meets every capability, sets every
   parameter and states its overrides honestly.

The tool uses only the Python standard library. It reads files and never writes any, and it never sends anything
anywhere.

<!-- anchor: checks.conform.run -->

## How to run it

```
bin/conform self [--root DIR] [--deny-list FILE] [--json] [--log-level LEVEL]
bin/conform adapter ADAPTER [--json] [--log-level LEVEL]
```

| Argument | Meaning |
|---|---|
| `--root DIR` | The repository to check in the `self` mode. It defaults to the repository that holds the tool. |
| `--deny-list FILE` | A file of private words, one per line, kept outside this repository. There is no default: without it the `self` mode refuses to run. |
| `ADAPTER` | The adapter JSON file to check in the `adapter` mode. |
| `--json` | Print the report as one JSON object instead of the table. |
| `--log-level LEVEL` | Send the tool's own trace to standard error at `DEBUG`, `INFO`, `WARNING` or `ERROR` (case does not matter). Without it nothing goes to standard error. |

The launcher resolves the repository from its own real path, so the command works from any directory and through a
symbolic link. Running it with no subcommand, or with a wrong argument, is a refusal, not a crash: it prints a report
whose one row is `NOT RUN input.usage` and exits 2. The help option prints the argument summary and exits 0.

<!-- anchor: checks.conform.exit -->

## The exit contract

| Exit | Meaning |
|---|---|
| 0 | The run judged everything it was asked to judge and found no failure. Warnings and information rows may be present. |
| 1 | The run judged and found at least one failure. |
| 2 | The run could not judge: an argument, a file it needs, or the tool itself was at fault. |

A row that reads NOT RUN appears only with exit 2, and exit 2 has no row of any other failing status in front of it: a
refusal is one row that says what was missing and stops. A caller that sees exit 2 has learned nothing about the
repository and must fix the invocation first.

<!-- anchor: checks.conform.report -->

## The report

The report is a list of rows and a summary. Each row has a status, a rule, a subject and a detail.

| Status | Meaning |
|---|---|
| `PASS` | A rule was checked over its whole population and found nothing. The detail states the population. |
| `WARN` | Something to attend to that does not fail the run, for example an adapter whose recorded hash has gone stale. |
| `FAIL` | A finding. The run exits 1. |
| `INFO` | A fact worth knowing, for example a file the scan could not read as text. |
| `NOT RUN` | The run could not judge. Only with exit 2. |

The table prints one line per row: the status padded to seven characters, two spaces, the rule, two spaces, the
subject, two spaces, the detail. A subject of `*` means the whole population. Then comes the summary line:

```
SUMMARY  mode=self  exit=0  pass=24 warn=0 fail=0 info=0 not-run=0  population: neutral-files=65 ...  probes: scan.canary,card,...
```

The population lists what each probe looked at, so that a pass over nothing cannot pass unnoticed. The probes list names
the groups of rules that actually ran. On a refusal both read `none`.

The JSON form (`--json`) is one object with the keys `mode`, `exit`, `rows` and `summary`. Each row is an object with
`status`, `rule`, `subject` and `detail`; the summary holds `line` (the summary line above), `counts`, `population` (numbers
stay numbers) and `probes`. The rows of the JSON are the rows of the table, in the same order.

<!-- anchor: checks.conform.self -->

## The self rules

The `self` mode first refuses when it cannot start: the root is not a directory or holds no neutral file
(`input.root`), or the deny list is absent, unreadable, not UTF-8 or empty (`input.deny-list`). Then it runs the scan's
canary probe (see the next section), and then the format rules over the neutral files.

| Rule | Fails when |
|---|---|
| `card.present` | A file has no card, or a card that is not closed. |
| `card.flat` | A card line is not a `key: value` pair at the start of the line. |
| `card.keys` | A mandatory key is missing or empty, a key is unknown or repeated, or the skill keys are not a pair. |
| `card.id` | An id is not dotted lowercase, or two files share one. |
| `card.status` | A status is not `stub`, `draft` or `stable`. |
| `anchor.syntax` | A line that looks like an anchor is not exactly an anchor line with a valid id. |
| `anchor.unique` | An anchor id is used twice in the repository. |
| `norm.id` | A list item that opens with a level word has a bold id that is not a norm id. |
| `norm.level` | A norm's level is not one of the five, followed by a colon. |
| `norm.unique` | A norm id is used twice in the repository. |
| `norm.anchored` | A norm stands before the first anchor of its file. |
| `registry.present` | The capability registry or the parameter registry is missing. |
| `registry.syntax` | A declaration has a bad name, or carries the other registry's prefix. |
| `registry.meaning` | A declaration has no meaning. |
| `registry.unique` | A name is declared twice. |
| `call.syntax` | A text shaped like a capability or parameter call has a malformed name. |
| `call.resolves` | A call names a capability or parameter that no registry declares. |
| `version.semver` | The version file is missing, unreadable, or not one semantic-version line. |
| `version.changelog` | The changelog is missing or has no heading for the current version. |

Every rule that finds nothing prints one PASS row whose detail states how many files, anchors, norms or calls it covered.
The changelog rule prints an INFO row instead of a failure when the version itself is malformed, because the version rule
already failed for it.

<!-- anchor: checks.conform.scan -->

## The publication scan

The scan is what makes the repository safe to publish. It reads every text file under the root, in sorted order, and
skips only the `.git`, `doxygen_output`, `__pycache__` and `.pytest_cache` directories, the `.DS_Store` file and symbolic
links. A file with a NUL byte, or one that is not UTF-8, is not scanned: it gets an INFO row `scan.binary` and is counted
in the population as a binary file. File names are not scanned.

Four rules look at each line.

| Rule | Finds |
|---|---|
| `scan.home-path` | A path under a POSIX `Users` or `home` root, or under a Windows drive's `Users` root. |
| `scan.home-relative` | A path that starts with the tilde and a slash and has at least one segment. |
| `scan.email` | An e-mail address. |
| `scan.deny-token` | A word from the deny list, matched anywhere in a line without regard to case. |

**The deny list.** It is a text file, one word or phrase per line, that the owner keeps outside this repository and
passes with `--deny-list`. Blank lines and lines that start with a hash are ignored; the rest are the tokens. The tool
reads the file and never copies a token anywhere: not into a row, not into a log.

**Fingerprints.** A finding never shows what it matched. Its detail is the line number and a fingerprint of the match,
`fp=<length>:<eight hex digits>`, the length and the first eight hex digits of the SHA-256 of the match (lowercased for a
deny token). The owner finds the place from the file and the line, and compares the fingerprint to a known word by hashing
it. The summary line carries `deny-list=<count>` and `deny-list-fp=<twelve hex digits>`, a fingerprint of the sorted
list, so that two runs can be shown to have used the same list.

**The canary probe.** Before it scans, the tool builds from fragments one line for each of the four patterns, and one line
holding a deny token, and checks that each pattern and each token matches its canary. A scan whose pattern does not bite
would pass everything, so a failed canary is a refusal (`scan.canary`, `NOT RUN`, exit 2), not a pass; a passed one prints
`PASS scan.canary`. The source of the tool holds no text that matches its own patterns: the scan of this repository
includes the tool.

<!-- anchor: checks.conform.adapter -->

## The adapter rules

The `adapter` mode reads the adapter file, then the copy of this repository that the adapter's `spec_root` names, and
judges the one against the other. `spec_root`, every `via` and every vendored `path` are absolute or relative to the
directory of the adapter file, so the command gives the same verdict from any directory.

It refuses to run (`NOT RUN`, exit 2) when the adapter is missing, is a directory, is not UTF-8 or not JSON, or is not a
JSON object (`input.adapter`); when `spec_root` is absent, empty or not a directory, when the version file of the spec is
not one semantic version, when a registry is missing, or when the spec holds no neutral file (`input.spec-root`); and
when `runtime/adapter.schema.json` is missing, is not JSON, uses a keyword outside the small subset the tool understands,
or holds a reference that is not of the form `#/$defs/<name>` (`input.schema`). The tool validates the adapter with its
own standard-library code, not with a schema library; the schema is the single source of the structural rules.

| Rule | Status | Reported when |
|---|---|---|
| `adapter.schema` | FAIL | The adapter breaks the schema where no narrower rule below applies, for example a missing top-level key. The subject is the JSON pointer of the fault, or `*` for the whole adapter. |
| `adapter.spec-version` | PASS, WARN, FAIL | The version the adapter targets equals the spec's (PASS), is older (WARN) or is newer or not a semantic version (FAIL). |
| `adapter.parameter` | FAIL | A declared parameter has no value, has an empty value, or the adapter sets a name no registry declares. |
| `adapter.capability` | FAIL | A declared capability is missing, has neither a non-empty mechanism nor a non-empty fallback, or the adapter names one no registry declares. |
| `adapter.file-coverage` | FAIL | A neutral file has no entry, an entry names a path that is not a neutral file, or an entry has no mode or an unknown mode. |
| `adapter.reference` | PASS, FAIL | A reference entry names a `via` file that is missing or names neither the neutral file's id nor its path (the match is a plain substring), or the entry holds a key a reference does not have. |
| `adapter.vendored` | PASS, WARN, FAIL | The copy is missing, a section of the copy differs from the neutral section, or the recorded hash is stale (see below). |
| `adapter.override` | FAIL, INFO | An override names an anchor the neutral file lacks or names one twice; its `until` is not a calendar date or has passed; or it holds neither `until` nor `trigger`. An override with only a trigger gets an INFO row: the trigger is checked for presence only. |
| `adapter.not-applied` | PASS, FAIL | A not-applied entry has no reason. |

**Coverage.** Every neutral file has exactly one entry in `files`. The row `PASS adapter.file-coverage * <n> neutral files
accounted for` states how many.

**Rows per entry.** Each valid entry earns one PASS row whose detail names its mode. An entry that already has a schema
row is not judged a second time: the fault is reported once, where the schema found it.

**Vendored copies.** The adapter records the SHA-256 of the neutral file, taken over its bytes after every CRLF and CR
became LF. The tool compares the copy with the neutral file by anchor: the text before the first anchor is not compared,
each section is compared byte for byte, and a section that an override names is left out. A section that is missing in
the copy, unequal, repeated, or not in the neutral file is a difference. If the recorded hash equals the neutral file's
hash today, the copy was made from this neutral file and a difference is a FAIL. If the hash differs, the neutral file has
moved on since the copy: a difference is a WARN, and one more WARN row states that the hash is stale, with the first
twelve hex digits of the recorded and the current hash. A fresh copy without a difference earns the PASS row
`mode=vendored sections=<n> overrides=<m>`.

**Overrides.** An override lets a harness word one section its own way, for a stated reason, by a stated owner, until a
date or until a trigger. The date is checked against today; the trigger is only required to be present, because the tool
cannot know whether an event of the harness has happened.

**Population and probes.** The summary line of an adapter run lists these populations, in order: `neutral-files`,
`anchors`, `norms`, `capabilities`, `parameters`, `spec-version`, `adapter-files`, `adapter-parameters`,
`adapter-capabilities`. It lists the probes that ran, in the order `structure`, `spec-version`, `parameter`, `capability`,
`file-coverage`, `reference`, `vendored`, `override`, `not-applied`; a probe for a mode is listed only when the adapter has
an entry of that mode.

<!-- anchor: checks.conform.logs -->

## The trace

With `--log-level`, the tool writes its own trace to standard error, one line per event, in the Log Driven Development
form:

```
[IMP:<1-10>][<FUNCTION>][<BLOCK>] text
```

The importance runs from 1 to 3 for a trace of a step, 4 to 6 for the flow (a start, an end, a branch), 7 to 8 for a read
at a boundary (a file, the argument list), and 9 to 10 for a verdict, a finding or a failure. `DEBUG` shows all of them,
`INFO` shows 4 and above, `ERROR` only the failures. A line carries paths, counts, rule names and fingerprints, and
never a file's text, a matched value, a deny token or a value read from an adapter. The report is on standard output and
the trace on standard error, so `--json` output stays clean with the trace on.
