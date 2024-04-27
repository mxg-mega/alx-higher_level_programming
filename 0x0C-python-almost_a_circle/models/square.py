#!/usr/bin/python3
""" Square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square inherits from class
        Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ __init__ instantiates the class
            All attribute operations are inherited
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Size getter method """
        return self.width

    @size.setter
    def size(self, value):
        """ Size setter method """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ Over ridding the str method for Square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
