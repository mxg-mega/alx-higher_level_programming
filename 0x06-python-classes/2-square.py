#!/usr/bin/python3
"""The Square Class"""


class Square():
    """ DocString of the Square class
    Attributes:
        __size (int): size of the square
    Raises:
        ValueError: If the size value is less than 0.
        TypeError: If the size attribute is not an int.
    """
    def __init__(self, size=0):
		"""Initializes the Square instance with a given size.

        Args:
            size (int): Size of the square.

        Raises:
            ValueError: If the size value is less than 0.
            TypeError: If the size attribute is not an int.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
