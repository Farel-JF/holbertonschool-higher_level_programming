#!/usr/bin/python3
"""
This script appends command-line arguments to a list stored in a JSON file.
If the file does not exist, it creates a new list. The updated list is saved
back to the file.
"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        items = load_from_json_file('add_itemjson')
    except FileNotFoundError:
        items = []

    for i in range(1, len(sys.argv)):
        items.extend(sys.argv[i])
    save_to_json_file(items, "add_item.json")
