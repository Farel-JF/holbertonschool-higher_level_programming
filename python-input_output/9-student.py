#!/usr/bin/python3
"""this file contain the class student"""


class Student:
    """class of student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dictionary description of object"""
        return self.__dict__
