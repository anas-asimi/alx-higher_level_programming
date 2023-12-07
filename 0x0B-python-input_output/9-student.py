#!/usr/bin/python3
"""module"""


class Student:
    """class"""

    def __init__(self, first_name, last_name, age):
        """function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function"""
        return self.__dict__
