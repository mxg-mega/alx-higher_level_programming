#!/usr/bin/python3
""" Rectangle class """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ This class is a subclass of BaseGeometry """
    """ __init__ instanciates the class with width and height

        Args:
            width(int): width value of rectangle
            height(int): height value of rectangle
        raises:
            TypeError: this is from the superclass validator
                function.
            ValueError: this is from the validator function
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
