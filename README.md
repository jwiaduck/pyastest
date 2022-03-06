pyastest
===========================
a command line tool to parse, modify, and compare Python ASTs

# Quick Start
Note: Developed with Python 3.9.10!

Note: Rudimentally tested. Proceed with caution!

Currently, only Abstract Syntax Tree equality check between two files is supported.

```console
$ git clone <this repo>
$ cd pyastest
$ python3 pyastest.py -d <path/to/file1> <path/to/file2>
Starting...
...
True: ASTs are equal!
Finished!
```

In this repo, I plan to build both this comparison tool as well as other tools utilizing Abstract Syntax Trees.

# Documentation
## Options
Only one option [-d, etc.] must be specified.
### Diff
`-d/--diff` must be specified, followed by `path/to/ORIGINAL path/to/CHANGED`

Ex: `python3.5 -d \~/dev/source.txt) \~/dev/source_)changed.txt)` 
