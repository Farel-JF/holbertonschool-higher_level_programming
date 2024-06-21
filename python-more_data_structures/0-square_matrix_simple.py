#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Compute the square of each element in a matrix.

    Args:
        matrix (list of lists): The input matrix.

    Returns:
        list of lists: A new matrix where each element is the square of
        the corresponding element in the input matrix.

    """
    new_matrix = []
    for row_matrix in matrix:
        new_row = []
        for num in row_matrix:
            new_row.append(num ** 2)
        new_matrix.append(new_row)
    return new_matrix
