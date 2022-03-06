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

# checks that file is read/write-able
def r_w_file(file):
    if os.path.exists(file):
        if os.access(file, os.R_OK):
            return file
        else:
            print('The file is not readable and/or writable')
            exit(0)
    else:
        print('The specified file does not exist')
        exit(0)

# command line argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(prog='pyastest',
                                     description='a command line tool to parse, modify, and compare Python ASTs',
                                     formatter_class=argparse.RawTextHelpFormatter)
    
    tool_group = parser.add_mutually_exclusive_group(required=True)
    tool_group.add_argument('-d', '--diff', nargs=2, type=argparse.FileType('r', encoding='UTF-8'), 
                            help='''diff the ASTs of two files\nusage: pyastest -d path/to/ORIGINAL.py path/to/CHANGED.py
                                ''')
    
    parser.add_argument('--version', action='version', version='%(prog)s v0.1')

    args = parser.parse_args()
    # print(vars(args))

    # Get FileType objects (opened and ready to read)
    args.original = args.diff[0].read()
    args.changed = args.diff[1].read()

    args.diff[0].close()
    args.diff[1].close()

    return args