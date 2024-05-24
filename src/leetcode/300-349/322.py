from functools import cache
from typing import List
from math import inf


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def recurrence(i: int) -> int:
            if i < 0:
                return -1
            elif i == 0:
                return 0
            else:
                cost = inf
                for j in filter(lambda x: x <= i, coins):
                    f = recurrence(i - j)
                    if f != -1:
                        cost = min(cost + 1, f)
                if type(cost) == float:
                    return -1
                return int(cost)

        return recurrence(amount)
