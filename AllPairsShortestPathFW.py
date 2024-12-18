# This program solves All Pairs Shortest Path
# Using Floyd-Warshall Algorithm
import numpy as np


def floyd_warshall_algorithm(A0):
    n = len(A0)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Check if there exists shorter path in vertex k
                if A0[i][j] > A0[i][k] + A0[k][j]:
                    A0[i][j] = A0[i][k] + A0[k][j]
    return A0


def main():
    # Initialize the table A0
    infinity = float('inf')
    A0 = np.array([[0, 3, infinity, 7],
                   [8, 0, 2, infinity],
                   [5, infinity, 0, 1],
                   [2, infinity, infinity, 0]])
    solution = floyd_warshall_algorithm(A0)
    print(solution)


main()
