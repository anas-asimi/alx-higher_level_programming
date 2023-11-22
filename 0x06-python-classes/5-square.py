#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """

    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """returns the current square area
        Args: None
        Returns: area of square
        """
        return (self.__size**2)

    def my_print(self):
        """prints in stdout the square with the character #
        Args: None
        Returns: None
        """
        if self.__size == 0:
            print('')
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print()

    @property
    def size(self):
        """getter of __size
        Args: None
        Returns: None
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter of __size
        Args: value (int): size of a side of the square
        Returns: None
        """
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
