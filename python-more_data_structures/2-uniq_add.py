#!/usr/bin/python3

"""contain the function addition"""

def uniq_add(my_list=[]):

    """adds all unique integers in a list (only once for each integer)"""

    result = 0
    get_element = set(my_list)
    for sum in get_element:
        result += sum
    return result
