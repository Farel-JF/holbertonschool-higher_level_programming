#!/usr/bin/python3
"""def is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of the specified class or a subclass.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is an instance of a_class or a subclass; otherwise False.
    """
    return isinstance(obj, a_class)
