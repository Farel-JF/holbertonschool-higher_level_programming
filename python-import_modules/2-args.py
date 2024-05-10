#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_arguments = len(sys.argv) - 1
    arguments = sys.argv[1:]

    if num_arguments == 0:
        print("{} arguments.".format(num_arguments), end="\n\n")
    elif num_arguments == 1:
        print("{} argument:".format(num_arguments), end="\n")
        print("{}: {}".format(num_arguments ,arguments[0]), end="\n\n")
    else:
        print("{} arguments:".format(num_arguments), end="\n")
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))
