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
    print("Got AST!")
    return tree