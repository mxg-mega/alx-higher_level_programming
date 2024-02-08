#!/usr/bin/python3
class Square():
    """ A class named Square
    Attributes:
        __size(int): the size of the square as a class

    methods:
        __init__: the initialization of the sqaure class
    """
    def __init__(self, size):
        """ __init__ is a method that initializes the instances of the class
        Args:
            size(int): integer to know the size of the square
        """
        self.__size = size
