#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Parameters:
    data (dict): The dictionary to serialize.
    filename (str): The filename of the output JSON file. If the file exists, it will be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load data from a JSON file and deserialize it to a Python dictionary.

    Parameters:
    filename (str): The filename of the input JSON file.

    Returns:
    dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
