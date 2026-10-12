# Command Reference

Append `--verbose` to a command or pipeline to include execution metadata in
the API result.

## Commands

Use `help <command>` for full command-specific usage. Square brackets mark
optional arguments; angle brackets mark required arguments.

### Start and navigate

- `help [command]` — List commands or show usage for one command.
- `welcome` — Show the terminal introduction.
- `about` — Describe Vaultsh.
- `pwd` — Print the current virtual directory.
- `ls [-alR] [path]` — List files and directories.
- `cd [directory]` — Change the current virtual directory.
- `tree [-a] [-L depth] [path]` — Print a directory tree.

### Read and filter

- `cat [-n] [file]` — Print a file or pipeline input.
- `grep [-in] <pattern> [file]` — Filter lines with a regular expression.
- `head [-n count] [file]` — Print the first lines.
- `tail [-n count] [file]` — Print the last lines.
- `wc [-lwc] [file]` — Count lines, words, and bytes.
- `sort [-r] [file]` — Sort lines.

### Session

- `history` — List commands from the current session.
- `clear` — Clear the terminal.

### Search and status

- `search <query>` — Search portfolio content with Atlas.
- `metrics` — Show the Forge analytics summary.
- `dashboard [--window 24h|7d|30d|all] [--include-invalid]` — Show Forge
  analytics, service health, deployment, and Sentinel status. The default is
  24 hours. `all` covers every event Forge still retains. Unknown command
  names (exit code `127`) are omitted from the popular-commands list unless
  `--include-invalid` is set; request and error totals still include them.
- `deployments` — Show the latest production deployment.

```sh
dashboard --window all
dashboard --window 7d
dashboard --window all --include-invalid
```

### Profile

- `whoami` — Show Mateo's current role and focus.
- `contact` — Show contact links.

## Filesystem

Directories end with `/` in standard `ls` output. `ls -a` includes hidden
entries, `ls -l` includes read-only mode and byte size, and `ls -R` recursively
lists directories.

```sh
pwd
ls
ls -la /
ls /cv
tree
tree -a
tree -L 2 /
cd cv
cat experience.md
cd ..
```

Paths can be absolute or relative:

```sh
cat /cv/about.md
cat projects/vaultsh.md
cd /cv
cd ..
```

Quoted and escaped arguments are supported:

```sh
cat "file with spaces.md"
cat file\ with\ spaces.md
```

Number file or pipeline lines:

```sh
cat -n /cv/about.md
cat /cv/about.md | cat -n
```

## Pipelines

Each pipeline stage receives the previous stage's output. Execution stops when
a stage returns a non-zero exit code.

Show programming languages:

```sh
cat /cv/skills.md | grep "Languages"
```

Show the first three experience contributions:

```sh
cat /cv/experience.md | grep "^- " | head -n 3
```

Find the A1 role:

```sh
cat /cv/experience.md | grep "A1 Hrvatska"
```

Show numbered, case-insensitive matches:

```sh
cat /cv/skills.md | grep -in "python"
```

Display the five most recent history entries:

```sh
history | tail -n 5
```

Reverse-sort Vaultsh feature and decision bullets:

```sh
cat /projects/vaultsh.md | grep "^- [^*]" | sort -r
```

Commands that accept `[file]` can read a virtual file directly or consume
pipeline input:

```sh
head -n 5 /cv/skills.md
cat /cv/skills.md | head -n 5
```

More pipeline examples:

```sh
cat /cv/skills.md | grep "Languages"
cat /cv/experience.md | grep "ReversingLabs"
search "Technology" | grep "/projects/"
tree | grep ".md" | sort
```

## Keyboard Shortcuts

- `Tab`: complete commands and virtual filesystem paths; press again to leave the input
- `Shift+Tab`: move to the previous control; `Escape`: move to Commands
- `Ctrl+L`: run the backend-owned `clear` command

Autocomplete uses the current session directory:

```text
cat cv/exp<Tab>    -> cat cv/experience.md
cd cv
cat exp<Tab>       -> cat experience.md
```

## Exit Codes

- `0`: success
- `1`: command failure or no `grep` matches
- `2`: syntax, option, or usage error
- `126`: recognized but unsupported behavior
- `127`: command not found

## Planned Options

```sh
ls -lt
```
