#!/usr/bin/python3
""" 0x08-making_change """


def makeChange(coins, total):
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return -1 if dp[total] == total + 1 else dp[total]
