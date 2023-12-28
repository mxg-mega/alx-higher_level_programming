#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square(a_list=[]):
        return list(map((lambda x: x * x), a_list))
    return list(map(square, matrix))
