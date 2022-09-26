#!/usr/bin/python3
"""
A function that divides all elements of a matrix.
"""


def test_matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix

    Arguments:
        matrix:
    div: divider

    Returns: the divided new matrix
    """
    if isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by Zero")

    new_matrix = matrix.copy()

    for j in range(len(matrix)):
        if isinstance(matrix[j], list) is False:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        size = len(matrix[0])
        if len(matrix[j]) != size:
            raise TypeError("Each row of the matrix must have the same size")

        new_matrix[j] = matrix[j].copy()

        for k in range(len(matrix[j])):
            if isinstance(matrix[j][k], (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[j][k] = round((matrix[j][k] / div), 2)
    return new_matrix
