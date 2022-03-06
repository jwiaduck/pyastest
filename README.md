pyastest
===========================
a command line tool to parse, modify, and compare Python ASTs

sort of providing an interface to ast.py.

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

In this repo, I plan to build both this comparison tool as well as other tools utilizing Abstract Syntax Trees.

# Documentation
## Options
Only one option must be specified.
### Diff
`diff` command, followed by the files to be diffed, `path/to/ORIGINAL` and `path/to/CHANGED`

`diff` will read in and generate an AST for each file, then do an equality check on the two ASTs.

Ex: `$ python3.5 pyastest.py diff \~/dev/source.txt \~/dev/source_changed.txt` 
