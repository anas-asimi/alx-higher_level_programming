#!/usr/bin/python3
""" Base """


import json
import csv


class Base:
    """ Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__
        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string """
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ create """
        r = cls(**dictionary)
        return (r)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file """
        if list_objs is None:
            pass
        elif type(list_objs) is list and len(list_objs) > 0:
            file_name = cls.__name__ + '.json'
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(cls.to_json_string((list_dictionaries)))

    @classmethod
    def load_from_file(cls):
        """ load_from_file """
        file_name = cls.__name__ + '.json'
        try:
            with open(file_name, 'r') as f:
                json_string = f.read()
                list_dictionaries = cls.from_json_string(json_string)
                list_objs = [cls.create(**dictionary)
                             for dictionary in list_dictionaries]
                return (list_objs)
        except FileNotFoundError as err:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save_to_file_csv """
        if list_objs is None:
            pass
        elif type(list_objs) is list and len(list_objs) > 0:
            file_name = cls.__name__ + '.csv'
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            rows = []
            for dictionary in list_dictionaries:
                row = [dictionary['id']]
                if len(dictionary) == 4:
                    row.append(dictionary['size'])
                else:
                    row.extend([dictionary['width'], dictionary['height']])
                row.extend([dictionary['x'], dictionary['y']])
                rows.append(row)

            with open(file_name, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        """ load_from_file_csv """
        file_name = cls.__name__ + '.csv'
        try:
            with open(file_name, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                rows = []
                for row in csvreader:
                    rows.append([int(x) for x in row])
            list_dictionaries = []
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            for row in rows:
                dictionary = dict([fieldnames[i], row[i]]
                                  for i in range(len(fieldnames)))
                list_dictionaries.append(dictionary)
            list_objs = [cls.create(**dictionary)
                         for dictionary in list_dictionaries]
            return (list_objs)
        except FileNotFoundError:
            return ([])


class Object(object):
    """ helper class """
    pass
