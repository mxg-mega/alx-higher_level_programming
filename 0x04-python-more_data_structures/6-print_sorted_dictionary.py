#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        print()
    sorted = [i for i in a_dictionary.keys()]
    sorted.sort()
    for i in sorted:
        print('{}: {}'.format(i, a_dictionary[i]))
