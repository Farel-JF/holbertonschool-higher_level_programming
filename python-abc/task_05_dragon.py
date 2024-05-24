#!/usr/bin/env python3
"""
This module contains classes representing Mystical Dragon.
"""

#  swim
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# FlyMixin  method
class FlyMixin:
    def fly(self):
        print("The creature flies!")


# Dragon class inherit
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

draco = Dragon()


draco.swim()
draco.fly()
draco.roar()
