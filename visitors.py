# pyastest:
#   a command line tool to parse, modify, and compare Python ASTs
# 
# visitors.py:
#   utility/helper functions for interacting with source code/ASTs
#   subclassing the ast.Visitor class
#   
# @jwiaduck 6 March 2022
#

import ast

# Visitor Class for First Pass
# Counts number of each node type
class MyVisitor(ast.NodeVisitor):
    """Visitor Class"""
    def __init__(self):
        self.counts = {}

    def get_count(self):
        print("\n---NODE TYPE SUMMARY---")
        for key in sorted(self.counts):
            print("{}: {}".format(key, self.counts[key]))
        print()
        print(f"total unique: {len(self.counts)}")
        print(f"total total: {sum(self.counts.values())}")

    def visit(self, node):
            name = type(node).__name__
            if name in self.counts:
                self.counts[name] += 1
            else:
                self.counts[name] = 1
            ast.NodeVisitor.visit(self, node)

        