from functools import lru_cache
from math import inf

def minNumberOfCoinsForChange(n, denoms):
    @lru_cache
    def recurrence(i):
        if i < 0:
            return -1
        if i == 0:
            return 0

        cost = inf
        for j in denoms:
            ans = recurrence(i - j)
            if ans != -1:
                cost = min(cost, ans + 1)

        return cost if type(cost) != float else -1

    return recurrence(n)
