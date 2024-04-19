#!/usr/bin/python3
""" MyList class inherits from class list """


class MyList(list):
    """print_sorted prints the instance itself
        as a list in a sorted manner
        Args:
            self(list): the instance itself is a list
        raises:
            
    """
    def print_sorted(self):
        print(sorted(self))
