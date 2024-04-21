#!/usr/bin/python3
""" Read_file function """


def read_file(filename=""):
    """ function reads a file

        Args:
            filname(str): the name of the file to open

    """
    with open(filename, "r", encoding='utf-8') as fileRead:
        content = fileRead.read()
        print(content, end='')
