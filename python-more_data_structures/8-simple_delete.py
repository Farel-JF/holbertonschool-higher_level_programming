#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Remove a key from a dictionary if it exists.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to remove from the dictionary. Defaults to "".

    Returns:
        dict: The modified dictionary.
    """
    if key in a_dictionary:
        a_dictionary.pop(key)
    return a_dictionary
