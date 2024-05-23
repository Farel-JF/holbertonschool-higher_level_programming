#!/usr/bin/python3
"""BaseGeometry class"""

class BaseGeometry:
    """BaseGeometry class empty"""

    def area(self):
        """Method to calculate the area of a geometric shape"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate integer values"""

        if type(name) is chr:
            return
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
