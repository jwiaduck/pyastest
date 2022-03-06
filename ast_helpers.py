# pyastest:
#   a command line tool to parse, modify, and compare Python ASTs
# 
# helpers.py:
#   utility/helper functions for interacting with source code/ASTs
#   
# @jwiaduck 6 March 2022
#

import ast

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
    # print("Got AST!")
    return tree

# diff two asts from orginal and changed source codes
def ast_diff(args):
    # Get FileType objects (opened and ready to read)
    args.original = args.diff[0].read()
    args.changed = args.diff[1].read()

    args.diff[0].close()
    args.diff[1].close()

    src1 = args.original
    src2 = args.changed

    print(f"Original Source: {args.diff[0].name}\nChanged Source: {args.diff[1].name}")
    tree_1 = get_ast(src1)
    tree_2 = get_ast(src2)

    # simple diff check
    if ast.dump(tree_1) == ast.dump(tree_2):
        print("\nTrue: ASTs are equal!")
    else:
        print("\nFalse: Not equal.")

    
# get the info from a source code file
def ast_info(args):
        print("INFOOOOooooOOOooooooOOO!\n")