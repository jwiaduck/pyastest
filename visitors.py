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
class InfoVisitor(ast.NodeVisitor):
    """Visitor Class"""
    def __init__(self):
        self.counts = {}
        self.assignments = {}

    def print_summary(dict):
        for key in sorted(dict):
            print("{}: {}".format(key, dict[key]))
        print()
        print(f"total unique: {len(dict)}")
        print(f"total total: {sum(dict.values())}")

    def get_counts(self):
        print("\n---NODE TYPE SUMMARY---")
        InfoVisitor.print_summary(self.counts)

    def get_compares(self):
        compares = {'Compare': 0, 'Eq': 0, 'NotEq': 0, 'Lt': 0, 'LtE': 0, 'Gt': 0, 
            'GtE': 0, 'Is': 0, 'IsNot': 0, 'In': 0, 'NotIn': 0}
        for key in compares:
            if key in self.counts:
                compares[key] = self.counts.get(key, 0)
        compares = {key: val for key, val in compares.items() if val > 0}
        print("\n---COMPARISON TYPE SUMMARY---")
        InfoVisitor.print_summary(compares)
        # return compares

    def get_assignments(self):
        assignments = {key: val for key, val in self.assignments.items() if val > 0}
        print("\n---ASSIGNMENT TYPE SUMMARY---")
        InfoVisitor.print_summary(assignments)

    def get_binary(self):
        binary = {'BinOp': 0, 'Add': 0, 'Sub': 0, 'Mult': 0, 'Div': 0, 'FloorDiv': 0,
            'BoolOp': 0, 'And': 0, 'Or': 0}
        for key in binary:
            if key in self.counts:
                binary[key] = self.counts.get(key, 0)
        binary = {key: val for key, val in binary.items() if val > 0}

        print("\n---BINARY TYPE SUMMARY---")
        InfoVisitor.print_summary(binary)
        # return binary

    def visit(self, node):
            name = type(node).__name__
            if name in self.counts:
                self.counts[name] += 1
            else:
                self.counts[name] = 1
            ast.NodeVisitor.visit(self, node)

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Name):
            if node.targets[0].id in self.assignments:
                self.assignments[node.targets[0].id] += 1
            else:
                self.assignments[node.targets[0].id] = 1
        ast.NodeVisitor.generic_visit(self, node)

        