#!/usr/bin/python3
""" Recatangle Class"""
from models.base import Base


class Rectangle(Base):
    """ a Subclass of Base defining Rectangles """

    """ __init__ helps instantiate the class
    Args:
        width(int): width value of rect
        height(int): height value of rectangle
        x(int): x
        y(int): y
        id(int): id of object
    """
    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if type(value) is not int:
            raise TypeError("Value of width must be an integer")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if type(value) is not int:
            raise TypeError("Value of height must be an integer")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        if type(value) is not int:
            raise TypeError("Value of x must be an integer")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        if type(value) is not int:
            raise TypeError("Value of y must be an integer")
        self.__y = value
