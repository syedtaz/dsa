from functools import cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def f(n: int, i: int) -> int:
            if i == 0:
                return 0
            elif n == 0:
                return 1
            elif coins[i - 1] > n:
                return f(n, i - 1)
            else:
                return f(n, i - 1) + f(n - coins[i - 1], i)

        return f(n=amount,i=len(coins))