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
        for row in range(self.height):
            print('#' * self.width)

    def __str__(self):
        """ __str__ """
        return ('[Rectangle] ({}) {}/{} - {}/{}'
                .format(self.id, self.x, self.y, self.width, self.height))
