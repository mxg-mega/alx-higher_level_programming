#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    unique_elements = set(my_list)
    uniq_add = 0
    for i in unique_elements:
        uniq_add += i
    return uniq_add
