# pyastest:
#   a command line tool to parse, modify, and compare Python ASTs
# 
# pyastest.py
#   main/driver for pyastest
#
# @jwiaduck 3 March 2022
#
import ast
import argparse
import os

import cli
import helpers


###
### Helpers
###



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

class VerboseStore(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError('nargs not allowed')
        super(VerboseStore, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print('value(s) %r for the %r option' % (values, option_string))
        setattr(namespace, self.dest, values)

# command line argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(prog='pyastest',
                                     description='a command line tool to parse, modify, and compare Python ASTs',
                                     usage='%(prog)s.py [OPTIONS] ... ORIGINAL CHANGED')
    
    tool_group = parser.add_mutually_exclusive_group(required=True)
    tool_group.add_argument('-d', '--diff', action='store_true', help='diff the ASTs of two files')
    
    parser.add_argument('-o, --original', metavar='ORIGINAL', dest='original', type=r_w_file,
                        help='path/to/<source1>.py\n')
    parser.add_argument('-c, --changed', metavar='CHANGED', dest='changed', type=r_w_file,
                        help='path/to/<source2>.py\n')
    parser.add_argument('--version', action='version', version='%(prog)s v0.1')

    args = parser.parse_args()
    print(vars(args))

    # Normalize the path
    args.original = os.path.abspath(args.original)
    args.original = os.path.abspath(args.changed)

    return args


def ast_diff(args):
    file_1 = args.original
    with open(file_1, encoding='utf-8') as f:
        src1 = f.read()
    f.close()

    file_2 = args.changed
    with open(file_2, encoding='utf-8') as f:
        src2 = f.read()
    f.close()
    print(f"Src Original: {file_1}\nSrc Changed: {file_2}")
    tree_1 = helpers.get_ast(src1)
    tree_2 = helpers.get_ast(src2)

    if ast.dump(tree_1) == ast.dump(tree_2):
        print("\nTrue: ASTs are equal!")
    else:
        print("\nFalse: Not equal.")


###
### Mains .-.
###

def main():

    args = parse_arguments() 

    print("Starting...\n")

    ast_diff(args)

    exit(1)


if __name__ == '__main__':
    main()



