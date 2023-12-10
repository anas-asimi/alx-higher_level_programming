#!/usr/bin/python3
""" Base """


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
