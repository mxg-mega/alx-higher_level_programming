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
        TypeError: if position is not a tuple with 2
        Natural numbers
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(p, int) and p >= 0 for p in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter Method
        Returns:
            int: the value of __size
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter Method
        Args:
            size (int): the new size of square
        Raises:
            TypeError: if size is not an integer
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(p, int) and p >= 0 for p in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """my_print - function prints #
    in a sqaure shape of size X size
    """
    def my_print(self):
        if self.__size == 0:
            print()

        if self.__position[1] > 0:
            for i in range(0, self.__position[1]):
                print()

        for i in range(0, self.__size):
            if self.__position[0] > 0:
                print(" " * self.__position[0], end='')
            print("#" * self.__size)
