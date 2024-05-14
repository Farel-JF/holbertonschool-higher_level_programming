#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
   for row_mtx in matrix:
    for i in row_mtx:
      print("{:d}".format(i), end=" ")
    print()
