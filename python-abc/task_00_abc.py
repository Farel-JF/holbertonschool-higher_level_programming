#!/usr/bin/env python3
"""
This module contains classes representing different animals.
"""

from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# Subclass Dog from the animal
class Dog(Animal):

    def sound(self):
        return "Bark"


# Subclass cat from the animal
class Cat(Animal):

    def sound(self):
        return "Meow"
