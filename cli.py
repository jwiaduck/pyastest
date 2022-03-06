# pyastest:
#   a command line tool to parse, modify, and compare Python ASTs
#
# cli.py:
#   parsing functions for cli arguments
#
# @jwiaduck 6 March 2022
#

import argparse
import os

from ast_helpers import ast_diff


# command line argument parsing
def parse_arguments():
    # create top-level parser
    parser = argparse.ArgumentParser(prog='pyastest',
                                     description='a command line tool to parse, modify, and compare Python ASTs',
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--version', action='version', version='%(prog)s v0.1')

    subparsers = parser.add_subparsers(title='Subcommands',
                                        description='Valid Subcommands',
                                        help='''current subcommands: diff
                                        ''')
    
    # create the parser for the "diff" command
    parser_diff = subparsers.add_parser('diff', help='''diff check the ASTs of two files\nusage: pyastest diff path/to/ORIGINAL.py path/to/CHANGED.py
                                        ''', formatter_class=argparse.RawTextHelpFormatter, description='diff the ASTs of two Python source code files\n', usage='pyastest diff [-h] ORIGINAL CHANGED')
    parser_diff.add_argument('diff', metavar = 'ORIGINAL, CHANGED', nargs=2, type=argparse.FileType('r', encoding='UTF-8'), 
                                help='paths to files to be diff\'d\nusage: pyastest diff path/to/ORIGINAL.py path/to/CHANGED.py')

    # if `diff`, set args.func to ast_diff (this works so we can have others set their fxns respectively)
    parser_diff.set_defaults(func=ast_diff)

    # parse the args and return Namespace object
    args = parser.parse_args()
    # print(vars(args))

    # if args Namespace object is empty, print help and exit(1) (essentially calling pyatest -h)
    # TODO: #1 see if theres a more elegant way to do this?
    if len(vars(args)) == 0:
        parser.print_help()
        exit(1)

    return args