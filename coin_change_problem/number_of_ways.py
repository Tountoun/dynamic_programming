#!/usr/bin/python3
"""This module tries to solve coin change problem."""


def solve(coins=[], total=0):
    """
    Return the number of ways the total amount can be got base on
    different coins.
    Args:
        coins (list(int)): the list of different coins
        total (int): the amount to be got using those coins
    Return:
        the number of ways the total can be found
    """
    rows = len(coins)
    cols = total + 1
    solving_array = [[0] * cols for i in range(rows)]

    for i in range(rows):
        solving_array[i][0] = 1
    for i in range(rows):
        for j in range(cols):
            if coins[i] > j:
                solving_array[i][j] = solving_array[i-1][j]
            else:
                solving_array[i][j] = solving_array[i-1][j] + solving_array[i][j-coins[i]]

    return solving_array[rows - 1][total]


if __name__ == '__main__':
    print(solve([12, 4, 6], 12)) #output: 3
    print(solve([1, 2, 3], 5)) #output: 5
    print(solve([1, 2, 3], 6)) #output: 7
    print(solve([1, 5, 6, 8], 11)) #output 6 
