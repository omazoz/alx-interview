#!/usr/bin/python3
""" 0x08-making_change """


def makeChange(coins, total):
    """ Generate changes needed to reach total
    """
    memo = dict()

    def dp(n):
        # return memo if n is in memo
        if n in memo: return memo[n]
        # return -1 if no combination can sum to n
        if n < 0: return -1
        # return 0 if n is zero
        if n == 0: return 0
        # initialize minimum number of coins needed to infinity
        res = float('inf')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem != -1: res = min(res, 1 + subproblem)
        # store the result into memo
        memo[n] = res if res != float('inf') else -1
        return memo[n]

    return dp(total)
