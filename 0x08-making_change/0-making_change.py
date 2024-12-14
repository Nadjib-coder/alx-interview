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
    
    remainder = total
    coins_needed = 0
    
    coin_index = 0
    
    sorted_coins_list = sorted(coins, reverse=True)
    
    list_len = len(coins)
    
    while remainder > 0:
        
        if coin_index >= list_len:
            return -1
        
        if remainder- sorted_coins_list[coin_index] >= 0:
            remainder -= sorted_coins_list[coin_index]
            
            coins_needed += 1
        else:
            coin_index += 1
    return coins_needed