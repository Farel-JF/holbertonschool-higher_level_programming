#!/usr/bin/python3
"""this file contain the class student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a Student instance.

        If attrs is a list of strings, only the attributes named in this list
        will be included in the dictionary.

        Args:
            attrs (list): A list of attribute names to include in
            the dictionary.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        Args:
            json (dict): A dictionary containing new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
