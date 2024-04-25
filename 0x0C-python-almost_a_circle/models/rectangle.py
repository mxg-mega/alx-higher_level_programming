#!/usr/bin/python3
""" Recatangle Class"""
Base = __import__('Base')


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
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        self.__y = value
