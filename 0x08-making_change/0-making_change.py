#!/usr/bin/python3

""" Contains makeChange Function """


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    
    # Initialize a list to track the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If the total cannot be reached, return -1
    return dp[total] if dp[total] != float('inf') else -1


#!/usr/bin/python3

# """ Contains makeChange Function"""


# def makeChange(coins, total):
#     """
#     Returns: fewest number of coins needed to meet total
#         If total is 0 or less, return 0
#         If total cannot be met by any number of coins you have, return -1
#     """
#     if not coins or coins is None:
#         return -1
#     if total <= 0:
#         return 0
#     change = 0
#     coins = sorted(coins)[::-1]
#     for coin in coins:
#         while coin <= total:
#             total -= coin
#             change += 1
#         if (total == 0):
#             return change
#     return -1