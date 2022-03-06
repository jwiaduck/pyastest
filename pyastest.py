# pyastest:
#   a command line tool to parse, modify, and compare Python ASTs
# 
# pyastest.py
#   main/driver for pyastest
#
# @jwiaduck 3 March 2022
#

from cli import parse_arguments

###
### Main(s) .-.
###

def main():

    args = parse_arguments()

    print("Starting...\n")
    args.func(args)
    print("Finished!")
    exit(0)
        

if __name__ == '__main__':
    main()



