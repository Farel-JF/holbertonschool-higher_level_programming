#!/usr/bin/env python3
"""abs class """

from abc import ABC, abstractmethod


# Shape abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Cirle class
class Cercle(Shape):
    def __init__(self, rayon):
        self.rayon = rayon

    def area(self):
        return self.rayon
    def perimeter(self):
        return self.rayon

# Rectange class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(Shape):
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
