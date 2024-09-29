from typing import List
from functools import cache
from math import inf

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        m, n = len(dungeon), len(dungeon[0])

        @cache
        def f(x: int, y: int) -> float:

            if x >= m or y >= n:
                return -inf

            v = dungeon[x][y]
            right = f(x + 1, y)
            down = f(x, y + 1)
            choice = min(right, down)

            if choice == -inf:
                return 1 if v >= 0 else 1 - v

            return max(1, choice - v + 1)

        return int(f(0, 0))