# pyastest:
#   a command line tool to parse, modify, and compare Python ASTs
# 
# @jwiaduck 3 March 2022
#

import ast
import sys


###
### Visitor Subclass
###

class MyVisitor(ast.NodeVisitor):

    def generic_visit(self, node):
        # print("Visitor sees a node: ", ast.dump(node) ))
        # print(f'Nodetype: {type(node).__name__:{16}} {node}')
        ast.NodeVisitor.generic_visit(self, node)


###
### Helpers
###

def parseAst(source):
    tree = ast.parse(source)
    ast.fix_missing_locations(tree)
    return tree

def compileAst(tree_in):
    exec(compile(tree_in, filename="<ast>", mode="exec"))

def unparseAst(tree_in):
    print(ast.unparse(tree_in))

def getAst(source):
    tree = parseAst(source)
    print("Got AST!\n")
    return tree


###
### Mains .-.
###

def main():

    if len(sys.argv) != 3:
        print("Usage: python3 pyatest.py path/to/file1 path/to/file2.")
        exit(0)

    print("Starting...\n")

    file_1 = sys.argv[1]
    with open(file_1, encoding='utf-8') as f:
        src1 = f.read()
    f.close()

    file_2 = sys.argv[2]
    with open(file_2, encoding='utf-8') as f:
        src2 = f.read()
    f.close()

    tree_1 = getAst(src1)
    tree_2 = getAst(src2)
    
    if ast.dump(tree_1) == ast.dump(tree_2):
        print("True: ASTs are equal!")
    else:
        print("False: Not equal.")
    print("Done!")
    exit(1)


if __name__ == '__main__':
    main()



