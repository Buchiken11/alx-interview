#!/usr/bin/python3
"""
greegy algorithms: the coin Change problem
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    counted = total
    coins_counted = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while counted > 0:
        if coin_idx >= n:
            return -1
        if counted - sorted_coins[coin_idx] >= 0:
            counted -= sorted_coins[coin_idx]
            coins_counted += 1
        else:
            coin_idx += 1
    return coins_counted
