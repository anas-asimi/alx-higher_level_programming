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
        """ to_json_string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file """
        if list_objs is None:
            pass
        elif type(list_objs) is list and len(list_objs) > 0:
            file_name = list_objs[0].__class__.__name__ + '.json'
            list_dicts = [x.to_dictionary() for x in list_objs]
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(cls.to_json_string((list_dicts)))
