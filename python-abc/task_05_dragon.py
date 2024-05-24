#!/usr/bin/env python3
"""
This module contains classes representing Mystical Dragon.
"""

# SwimMixin class for adding swimming functionality
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# FlyMixin class for adding flying functionality
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Dragon class inherits from both SwimMixin and FlyMixin
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

# Instantiate a Dragon object
draco = Dragon()

# Demonstrate abilities
draco.swim()
draco.fly()
draco.roar()


