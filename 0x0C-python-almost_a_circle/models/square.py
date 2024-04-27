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

    def to_dictionary(self):
        """ public method to_dictionary
            that returns the dictionary representation
            of a Rectangle
        """
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}

    def update(self, *args, **kwargs):
        """ Update method updates the value of
            the attribites

            Args:
            *args is the list of arguments - no-keyworded arguments
                 1st argument should be the id attribute
                 2nd argument should be the size attribute
                 3rd argument should be the x attribute
                 4th argument should be the y attribute
        """
        length = len(args)
        if length == 0:
            for name, value in kwargs.items():
                if name == "id":
                    self.id = value
                elif name == "size":
                    self.width = value
                    self.height = value
                elif name == "x":
                    self.x = value
                elif name == "y":
                    self.y = value
        else:
            for i in range(length):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
                    break

    def __str__(self):
        """ Over ridding the str method for Square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
