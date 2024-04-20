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

    """area return the area of a rectangle """
    def area(self):
        return self.__width * self.__height

    """ when str is called it should return a string
        in this format '[Rectangle] <width>/<height>'
    """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
