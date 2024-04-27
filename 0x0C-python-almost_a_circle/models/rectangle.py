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
    def __init__(self, width=1, height=1, x=0, y=0, id=None):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            Area Function returns the area of a rectangle.

            Returns:
                Product of height and width of instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """ display function prints the rectangle base on
            it parameters
        """
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print(("#" * self.__width))

    def update(self, *args, **kwargs):
        """ Update the class Rectangle by adding the public method 'update'
            that assigns an argument to each attribute.

            Args:
                args: A variable number of arguments representing the
                      attributes in the order id, width, height, x, and y.
        """
        
        length = len(args)
        if length == 0:
            for name, value in kwargs.items():
                if name == "id":
                    self.id = value
                elif name == "width":
                    self.__width = value
                elif name == "height":
                    self.__height = value
                elif name == "x":
                    self.__x = value
                elif name == "y":
                    self.__y = value
        else:
            for i in range(length):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
                    break

    def __str__(self):
        """ modified str returns this format
           '[Rectangle] (<id>) <x>/<y> - <width>/<height>'
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)
