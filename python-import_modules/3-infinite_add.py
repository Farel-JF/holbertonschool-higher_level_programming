#!/usr/bin/python3
if __name__ == "__main__":
      import sys
      sum = 0
      result = sys.argv[1:]
      for arg in result:  
          sum += int(arg)
      print("{}".format(sum))
