#!/usr/bin/python3
"""Contient la classe student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        - attrs (list): A list of strings representing the attribute names
        to include in the dictionary.

        Returns:
        - dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            if isinstance(attrs, list) and all(isinstance(attr, str)
                                               for attr in attrs):
                return {attr: self.__dict__.get(attr) for attr in attrs
                        if attr in self.__dict__}
            else:
                return self.__dict__
