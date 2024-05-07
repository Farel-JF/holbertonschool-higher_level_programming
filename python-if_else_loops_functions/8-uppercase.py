#!/usr/bin/env python3
def uppercase(str):
  uppercase_char=""
  for char in str:
    if 97 <= ord(char) <= 122:
      uppercase_char += chr(ord(char) - 32)
    else:
      uppercase_char += char
    uppercase_char += "\n"
    print("{}".format(uppercase_char), end="")

