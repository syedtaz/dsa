from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([j - i for (i, j) in zip(prices, prices[1:]) if j - i > 0])
