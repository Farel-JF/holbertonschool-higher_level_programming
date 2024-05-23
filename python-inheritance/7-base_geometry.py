#!/usr/bin/python3
"""def BaseGeometry class"""


class BaseGeometry:
    """def area"""
    def area(self):
        raise Exception("area() is not implemented")

    """def integer_validator"""

    def integer_validator(self, name, value):
        if type(name) is chr:
            return
        elif not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
