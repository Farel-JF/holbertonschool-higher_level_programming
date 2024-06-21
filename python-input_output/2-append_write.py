#!/usr/bin/python3
"""
This module contains a function for appending a string
to a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a given text to the end of the specified file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
