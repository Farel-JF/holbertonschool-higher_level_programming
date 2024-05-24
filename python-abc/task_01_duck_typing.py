#!/usr/bin/env python3
"""abs class """

from abc import ABC, abstractmethod
import math

# def Shape abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# def Cirle class
class Cercle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius **2
    def perimeter(self):
        return 2 * math.pi * self.radius

# def Rectange class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Def the shape_info
def shape_info(Shape):
    print("Area: {}".format(Shape.area()))
    print("Perimeter: {}".format(Shape.perimeter()))

# Test cases
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle info:")
    shape_info(circle)
    print()

    print("Rectangle info:")
    shape_info(rectangle)
