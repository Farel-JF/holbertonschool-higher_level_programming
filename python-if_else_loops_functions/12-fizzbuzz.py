#!/usr/bin/env python3
def fizzbuzz():
  for i in range(1, 98):
    if i % 3 == 0 and i % 5 == 0:
      print(f"FizzBuzz")
    elif i % 3 == 0:
      print("Fizz ")
    elif i % 5 == 0:
      print(f"Buzz")
    else:
      print("{}".format(i))
    