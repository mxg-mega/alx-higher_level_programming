#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end='')
                count += 1
            except ValueError:
                continue
            except IndexError:
                print("Traceback (most recent call last):")
        print()
        return (count)
    except TypeError:
        print()
        return (count)
