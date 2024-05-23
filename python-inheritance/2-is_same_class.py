#!/usr/bin/python3
"""is_same_class"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is exactly an instance of a_class; otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
