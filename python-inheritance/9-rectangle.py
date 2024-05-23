#!/usr/bin/python3
""" Module that defines a Rectangle class inheriting from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inheriting from BaseGeometry """
    def __init__(self, width, height):
        """ Initializes a Rectangle instance with width and height """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculates the area of the rectangle """
        return self.__width * self.__height
    def __str__(self):
        """ Returns the rectangle description """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
