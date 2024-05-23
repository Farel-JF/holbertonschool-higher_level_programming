#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""
    def __init__(self, size):
        """Initializes a Square instance with size"""
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size
