#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Return the key with the biggest integer value in the dictionary.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        str or None: The key with the biggest integer value, or None if the dictionary is empty.
    """
    if not a_dictionary:
        return None

    best_key = None
    max_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            best_key = key

    return best_key
