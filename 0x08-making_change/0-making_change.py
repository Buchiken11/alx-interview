#!/usr/bin/python3
"""
fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """ fewest number of coins needed to meet total """
    if total <= 0:
        return 0
    # sort the coins from top tp bottom
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        sum_total = total
        bal += sum_total
        total -= (sum_total * coin)
    if total != 0:
        return -1
    return change
