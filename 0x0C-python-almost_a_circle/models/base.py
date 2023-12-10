#!/usr/bin/python3
""" Base """


import json


class Base:
    """ Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__
        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))
