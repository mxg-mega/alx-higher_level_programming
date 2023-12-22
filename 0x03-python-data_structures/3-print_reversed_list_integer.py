#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    for i in range(len(my_list)):
        if len(my_list) == 0:
            break
        index = (i + 1) * -1
        str = '{:d}'
        print(str.format(my_list[index]))
