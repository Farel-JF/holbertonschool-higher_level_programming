#!/usr/bin/python3
"""
This module contains a function that returns an object (Python data structure)
represented by a JSON string

"""
import json

def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a file in JSON format.

    Args:
        my_obj (Any): The Python object to be serialized and saved.
        filename (str): The name of the file where the object will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
