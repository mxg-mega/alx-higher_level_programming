#!/usr/bin/python3
"""Node Class for making singly
linked list
    Attributes:
        __data: the data of the node
        __next_node: the next node
"""


class Node():
    """function __init__ initializes the class attributes
    Args:
        data (int): data of the node
        next_node (Node): it is none or another node class instance
    Raises:
        TypeError: if next node is not a node
    """
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is None:
            pass
        elif not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter method for data"""
        return self.__data
    
    @data.setter
    def data(self, value):
        """Setter method for data
        Args:
            value (int): integer value for data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter Method for next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter Method for next_node"""
        if value is None:
            value = None
        elif not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""Class SinglyLinkedList
Attributes:
    __head: the head of the list
"""


class SinglyLinkedList():
    """__init__ instantiates the Class"""
    def __init__(self):
        self.__head = None

    """sorted_insert inserts a node in
    an ordered manner
    Args:
        value: takes in a value for the data
    """
    def sorted_insert(self, value):
        if not isinstance(value, int):
            raise TypeError("All data should be an integer")

        newNode = Node(value)
        if self.__head is None:
            self.__head = newNode
        else:
            tmp = self.__head
            if newNode.data < tmp.data:
                self.__head = newNode
                newNode.next_node = tmp
                return
            while tmp is not None && newNode.data < tmp.data:
                tmp = tmp.next_node
            if tmp.net_node is not None:
                newNode.next_node = tmp.next_node
            tmp.next_node = newNode


