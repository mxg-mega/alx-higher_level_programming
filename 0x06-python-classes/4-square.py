#!/usr/bin/python3
"""Square Class
    Attributes:
        __size (int): the size of the square
"""


class Square():
    """__init__ initalizes the class
    Args:
        size: the size of square
    Raises:
        ValueError: if value is less than 0
        TypeError: if not an integer
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise
        if size < 0:
            raise
        self.__size = size

    """Area - calculates the area of a square
    Args:
        non
    Returns:
        int: the area of a square
    """
    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        """Getter Method
        Returns:
            int: the value of __size
        """
        return (self.__size)

    @size.setter
    def size(self, size):
        """Setter Method
        Args:
            size (int): the new size of square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
