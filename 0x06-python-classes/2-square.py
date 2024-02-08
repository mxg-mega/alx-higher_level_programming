#!/usr/bin/python3
"""The Square Class

    Attributes:
        __size (int): size of the square
"""


class Square():
    """ __init__ initializes the square class 
    Args:
        size (int): size of the sqaure
    Raises:
        ValueError: If the size value is less than 0.
        TypeError: If the size attribute is not an int.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
