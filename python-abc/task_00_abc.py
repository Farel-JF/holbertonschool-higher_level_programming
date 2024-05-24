#!/usr/bin/env python3

from abc import ABC, abstractmethod

# Abstract base class
class animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# subclass dog from the animal
class dog(animal):
    def sound(self):
        print("Bark")

# subclass cat from the animal
class cat(animal):
    def sound(self):
        print("Meow")
