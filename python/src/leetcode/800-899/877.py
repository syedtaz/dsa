from typing import List
from functools import cache


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def f(i: int, j: int) -> int:
            if i >= j:
                return 0

            choices = [
                piles[i] + f(i + 2, j),
                piles[i] + f(i + 1, j - 1),
                piles[j] + f(i + 1, j - 1),
                piles[j] + f(i, j - 2),
            ]

            return max(choices)

        i = 0
        j = len(piles) - 1

        return any([f(i, j) > f(i + 1, j), f(i, j) > f(i, j - 1)])
