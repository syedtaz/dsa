from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        acc = 0

        for i in range(len(piles) // 3):
            acc += piles[-2 * i - 2]

        return acc