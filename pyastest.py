# pyastest:
#   a command line tool to parse, modify, and compare Python ASTs
# 
# pyastest.py
#   main/driver for pyastest
#
# @jwiaduck 3 March 2022
#

from ast_helpers import ast_diff
from cli import parse_arguments

###
### Main(s) .-.
###

def main():

    args = parse_arguments() 

    print("Starting...\n")

    ast_diff(args)

    print("Finished!")
    exit(1)


if __name__ == '__main__':
    main()



