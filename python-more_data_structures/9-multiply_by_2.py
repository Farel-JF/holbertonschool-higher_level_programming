#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Multiply each value in the dictionary by 2.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        dict: A new dictionary with values multiplied by 2.
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
