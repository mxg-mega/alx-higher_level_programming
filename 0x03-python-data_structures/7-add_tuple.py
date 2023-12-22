#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    a1 = 0
    b1 = 0
    a2 = 0
    b2 = 0

    a_len = len(tuple_a)
    b_len = len(tuple_b)
    if a_len == 0:
        a = 0
    elif a_len < 2:
        a2 = 0
        a1 = int(tuple_a[0])
    else:
        a1 = int(tuple_a[0])
        a2 = int(tuple_a[1])

    if b_len == 0:
        b = 0
    elif b_len < 2:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b2 = int(tuple_b[1])
        b1 = int(tuple_b[0])

    a = a1 + b1
    b = a2 + b2

    new_tuple = (a, b)
    return new_tuple
