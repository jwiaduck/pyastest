# pyastest:
#   a command line tool to parse, modify, and compare Python ASTs
# 
# @jwiaduck 3 March 2022
#

import argparse
import ast
import sys
import os


###
### Helpers
###

# parses source code to AST
def parse_ast(source):
    tree = ast.parse(source)
    ast.fix_missing_locations(tree)
    return tree

# compiles and executes AST
def exec_co_ast(tree_in):
    exec(compile(tree_in, filename="<ast>", mode="exec"))

# ast.py unparse method
def unparse_ast(tree_in):
    print(ast.unparse(tree_in))

# agg. fxn to call AST helpers - namely, get_ast (and return tree)
def get_ast(source):
    tree = parse_ast(source)
    print("Got AST!")
    return tree

# checks that file is read/write-able
def r_w_file(file):
    if os.path.exists(file):
        if os.access(file, os.W_OK and os.R_OK):
            return file
        else:
            print('The file is not readable and/or writable')
            exit(0)
    else:
        print('The specified file does not exist')
        exit(0)

# command line argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(prog='pyastest')
    parser.add_argument('original', metavar='FILE_1', type=r_w_file,
                        help='Original: path/to/<source1>.py\n')
    parser.add_argument('changed', metavar='FILE_2', type=r_w_file,
                        help='Changed: path/to/<source2>.py\n')
    parser.add_argument('--version', action='version', version='%(prog)s v0.1')

    args = parser.parse_args()

    # Normalize the path
    args.original = os.path.abspath(args.original)
    args.changed = os.path.abspath(args.changed)

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
    tree_1 = get_ast(src1)
    tree_2 = get_ast(src2)

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



