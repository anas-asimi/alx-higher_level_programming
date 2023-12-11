#!/usr/bin/python3
""" Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__
        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # ========= width ========= #
    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__width = value

    # ========= height ========= #
    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be > 0")
        self.__height = value

    # ========= x ========= #
    @property
    def x(self):
        """getter for the private instance attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the private instance attribute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise TypeError("x must be >= 0")
        self.__x = value

    # ========= y ========= #
    @property
    def y(self):
        """getter for the private instance attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the private instance attribute y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise TypeError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area """
        return self.height * self.width

    def display(self):
        """ display """
        for n in range(self.y):
            print()
        for row in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """ __str__ """
        return ('[Rectangle] ({}) {}/{} - {}/{}'
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ update """
        keys = ['width', 'height', 'x', 'y']
        if args and len(args) > 0:
            if args[0] is None:
                self.__init__(self.width, self.height, self.x, self.y)
            else:
                self.id = args[0]
            for i in range(0, min(len(args) - 1, 4)):
                setattr(self, keys[i], args[i + 1])
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ to_dictionary """
        return ({
            'x': self.x,
            'width': self.width,
            'id': self.id,
            'height': self.height,
            'y': self.y,
        })
