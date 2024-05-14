#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
  for row_mtx in matrix:
        for i, num in enumerate(row_mtx):
            if i != 0:
                print(" ", end='')
            print("{:d}".format(num), end='')
        print()
