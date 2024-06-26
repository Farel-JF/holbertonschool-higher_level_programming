#!/usr/bin/python3

"""Contains the Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the Square instance."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
