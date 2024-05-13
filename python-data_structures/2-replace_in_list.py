#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
   if idx < 0 and idx >= len(my_list):
      return None
   else:
     my_list[3] = element
     return my_list[idx]