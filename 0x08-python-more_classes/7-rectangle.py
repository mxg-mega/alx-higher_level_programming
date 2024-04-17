#!/usr/bin/python3
""" Module that defines a class Rectangle """


class Rectangle:
    """ initialization function for class rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for variable heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height
            Args:
               value(int): value to set
            Exceptions:
               TypeError: value has to be an integer
               ValueError: height must be >= 0
       """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function calculates the area of the rectangle"""
        if self.__width == 0 or self.height == 0:
            return 0
        return self.__width * self.__height

    def perimeter(self):
        """ function calculates the perimeter of a rectangle """
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ prints rep of rectangle using print_symbol """
        prints = ''
        if self.__width == 0 or self.height == 0:
            return ''
        for i in range(self.__height):
            for j in range(self.__width):
                prints += str(self.print_symbol)
            prints += '\n'
        return prints[:-1]

    def __repr__(self):
        """ representation of class """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
