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
            raise TypeError('size must be an integer')
            return

        if size < 0:
            raise ValueError('size must be >= 0')
            return

        self.__size = size
