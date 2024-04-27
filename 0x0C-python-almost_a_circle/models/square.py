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

    def __str__(self):
        """ Over ridding the str method for Square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
