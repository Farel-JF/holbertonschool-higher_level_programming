#!/usr/bin/python3
"""
This module contains a function to return a JSON representation of
an object (string)

"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Args:
        my_obj (Any): The Python object to convert to JSON.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
