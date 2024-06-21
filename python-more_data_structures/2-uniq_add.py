#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    get_element = set(my_list)
    for sum in get_element:
        result += sum
    return result
