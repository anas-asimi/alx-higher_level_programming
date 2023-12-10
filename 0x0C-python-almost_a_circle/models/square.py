#!/usr/bin/python3
""" Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square """

    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__
        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y)

    def __str__(self):
        """ __str__ """
        return ('[Square] ({}) {}/{} - {}'
                .format(self.id, self.x, self.y, self.width))

    # ========= size ========= #
    @property
    def size(self):
        """getter for the private instance attribute size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for the private instance attribute size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """ update """
        keys = ['size', 'x', 'y']
        if args and len(args) > 0:
            if args[0] is None:
                self.__init__(self.size, self.x, self.y)
            else:
                self.id = args[0]
            for i in range(0, min(len(args) - 1, 3)):
                setattr(self, keys[i], args[i + 1])
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ to_dictionary """
        return ({
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        })
