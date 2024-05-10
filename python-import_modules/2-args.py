#!/usr/bin/python3
if __name__ == "__main__":
  import sys
  if (len(sys.argv) - 1) == 0:
    print("{} arguments.".format((len(sys.argv) - 1)), end="\n")
  elif (len(sys.argv) - 1) == 1:
    print("{} argument:".format(len(sys.argv) - 1), end="\n")
  else:
    print("{} arguments:".format((len(sys.argv) - 1)), end="\n")
  for i, arg in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(i, arg))
