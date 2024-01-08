#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for val in row:
            if val is not row[len(row) - 1]:
                print("{:d}".format(val), end=" ")
            else:
                print("{:d}".format(val), end="")
        print()
