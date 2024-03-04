from typing import List
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @cache
        def f(i: int, j: int) -> int:
            if i >= len(prices):
                return 0

            sell = 0 if i == j else prices[i] - prices[j]
            buy = f(i + 1, i)
            return max(sell, buy)

        return f(0, 0)

s = Solution()
print(s.maxProfit(prices = [7,1,5,3,6,4]))