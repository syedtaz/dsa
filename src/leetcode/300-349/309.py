from typing import List
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @cache
        def f(i: int) -> int:
            if i >= len(prices) - 1:
                return 0

            acc = 0

            for j in range(i + 1, len(prices)):
                acc = max(acc, prices[j] - prices[i] + f(j + 2))

            return max(acc, f(i + 1))

        return f(0)