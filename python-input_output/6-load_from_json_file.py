#!/usr/bin/python3
"""
This module contains a function that returns an object (Python data structure)
represented by a JSON string

"""
import json


def load_from_json_file(filename):
    """
    Loads and returns a Python object from a JSON file.

    Args:
        filename (str): The name of the file containing the JSON string.

    Returns:
        Any: The Python object represented by the JSON string in the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
