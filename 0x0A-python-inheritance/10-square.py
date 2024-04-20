#!/usr/bin/python3
""" Square class """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ This class is a subclass of Rectangle """
    """ __init__ instanciates the class with size

        Args:
            size(int): size value of the square

        raises:
            TypeError: this is from the superclass validator
                function.
            ValueError: this is from the validator function
    """
    def __init__(self, size=0):
        self.integer_validator("size", size)
        self.__size = size

    """area return the area of a rectangle """
    def area(self):
        return self.__size ** 2
