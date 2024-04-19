#!/usr/bin/python3
""" MyList class inherits from class list """


class MyList(list):
    """print_sorted prints the instance itself
        as a list in a sorted manner
        Args:
            self(list): the instance itself is a list
    """
    def print_sorted(self):
        if len(self) == 0:
            print([])
        else:
            dup = sorted(self)
            print(dup)
