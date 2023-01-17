#!/usr/bin/python3
"""
This module is used to get the minimum of coins to be used
in order to get the total amount.
"""


def solve(coins=[], total=0):
    """
    Find the minimum of coins to use based on different coins given
    to get total amount
    Args:
        coins (list(int)): list of different coins
        total (int): the amount to be got
    Return:
        the minimum number of coins used to get total
    """
    rows = len(coins)
    cols = total + 1
    array = [[100] * cols for i in range(rows)]

    for i in range(rows):
        array[i][0] = 0
    for i in range(1, cols):
        array[0][i] = i
    for i in range(1, rows):
        for j in range(1, cols):
            if coins[i] > j:
                array[i][j] = array[i-1][j]
            else:
                array[i][j] = min(array[i-1][j], 1 + array[i][j-coins[i]])

    return array[rows-1][total]


if __name__ == '__main__':
    print(solve([1, 2, 3], 5)) #output 2
    print(solve([1, 5, 6, 8], 11)) #output 2
