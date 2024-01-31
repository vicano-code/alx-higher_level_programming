#!/usr/bin/python3
"""
Module 101-nqueens

A program that solves the N queens problem.
-The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
NOTE: This program is limited to values of N = 4 or 6
"""


import sys


class Nqueens:
    """
    Class for solving the N queens problem
    """

    def nqueens_sol(self):
        """
        function for solving the N queens problem
        """
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)

        try:
            N = int(sys.argv[1])
        except ValueError:
            print("N must be a number")
            sys.exit(1)

        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        for i in range(N-2):
            my_list = []
            k = i + 1
            for j in range(N):
                sub_list = []
                sub_list.append(j)
                sub_list.append(k)
                if j >= 0 and k >= 0:
                    my_list.append(sub_list)
                k = k + i + 2
                if k > N - 1:
                    k = k - N - 1
            if len(my_list) == N:
                print("{}".format(my_list))


k = Nqueens()
k.nqueens_sol()
