pyastest
===========================
a command line tool to parse, modify, and compare Python ASTs

sort of providing an interface to ast.py. initially to provide some better scripting capabilities, but it might evolve into a suite of tools.

# Quick Start
Note: Developed with Python 3.9.10!

Note: Rudimentally tested. Proceed with caution!

Currently, only Abstract Syntax Tree equality check between two files is supported.

```console
$ git clone <this repo>
$ cd pyastest
$ python3 pyastest.py diff <path/to/file1> <path/to/file2>
Starting...
...
True: ASTs are equal!
Finished!
```

# Documentation
## Options
Only one option must be specified.
### Diff
`diff` command, followed by the files to be diffed, `path/to/ORIGINAL.py` and `path/to/CHANGED.py`

`diff` will read in and generate an AST for each file, then do an equality check on the two ASTs.

Ex: `$ python3 pyastest.py diff ~/dev/source.py ~/dev/source_changed.py` 

### Info

`info` command, followed by one file to be analyzed, `path/to/SOURCE.py`

`info` will read in and generate an AST for the given file, then visit the AST to gather info on the nodes.
print a summary of node type information.

Ex: `$ python3 pyastest.py info ~/dev/source.py`
