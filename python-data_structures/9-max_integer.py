#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None

    max_value = my_list[0]
    max_index = 0

    for i in range(1, len(my_list)):
        if my_list[i] > max_value:
            max_value = my_list[i]
            max_index = i

    return max_value
