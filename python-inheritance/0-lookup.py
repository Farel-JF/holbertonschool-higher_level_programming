#!/usr/bin/python3
"""Lookup"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    obj: The object whose attributes and methods are to be listed.

    Returns:
    List of strings: A list containing the names of the attributes and methods.
    """
    return dir(obj)
