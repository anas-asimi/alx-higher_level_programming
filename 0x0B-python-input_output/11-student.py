#!/usr/bin/python3
"""module"""


class Student:
    """class"""

    def __init__(self, first_name, last_name, age):
        """function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """function"""
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
