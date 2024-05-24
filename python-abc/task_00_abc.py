#!/usr/bin/env python3

from abc import ABC, abstractmethod

# Abstract base class
class animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# dog subclass
class dog(animal):
    def sound(self):
        print("Bark")

# cat subclass
class cat(animal):
    def sound(self):
        print("Meow")
