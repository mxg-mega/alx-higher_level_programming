#!/usr/bin/python3
""" Module that defines a class Rectangle """


class Rectangle:
    """ initialization function for class rectangle """
    def __init__(self, width=0, heigth=0):
        self.__width = width
        self.__height = heigth

    @property
    def width(self):
        """ getter for variable width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width
            Args:
                value(int): value to set
            Exceptions:
                TypeError: value has to be an integer
                ValueError: width must be >= 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def heigth(self):
        """ getter for variable heigth"""
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        """ setter for heigth
            Args:
               value(int): value to set
            Exceptions:
               TypeError: value has to be an integer
               ValueError: height must be >= 0
       """
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__heigthh = value
