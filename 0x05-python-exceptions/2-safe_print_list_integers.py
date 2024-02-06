#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(0, x):
            try:
                print("{:d}".format(my_list[i]), end='')
            except ValueError:
                count += 1
                continue
            except IndexError:
                break
        print()
        return ((i + 1) - count)
    except TypeError:
        print()
        return ((i + 1) - count)
