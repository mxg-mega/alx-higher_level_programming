#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            str = '{:d}'
            if j == i[-1]:
                print(str.format(j), end='')
            else:
                print(str.format(j), end=' ')
        print()
