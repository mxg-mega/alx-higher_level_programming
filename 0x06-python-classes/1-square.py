#!/usr/bin/python3
"""Exceptions are documented in the same way as classes.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the __init__ method and be consistent with it.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        size (int): size of the square

    Attributes:
        __size (int): size of the square

    """


class Square():
    def __init__(self, size):
        self.__size = size
