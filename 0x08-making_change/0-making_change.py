#!/usr/bin/python3

""" Contains makeChange Function"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)
    num_change = 0
    sum_change = 0
    
    for i in coins:
        while sum_change < total:
            sum_change += i
            num_change += i
        if sum_change == total:
            return num_change
        sum_change -= i
        num_change -= i
    return -1