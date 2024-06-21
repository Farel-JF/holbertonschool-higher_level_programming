#!/usr/bin/python3
"""def is_kind_of_class"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is an instance of a class that inherited from a_class;
        otherwise False.
    """
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
