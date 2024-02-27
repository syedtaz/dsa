from typing import List
from functools import cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        @cache
        def f(i: int, j: int) -> int:
            if j >= len(triangle):
                return 0

            l = f(i, j + 1)
            r = f(i + 1, j + 1)
            return min(l, r) + triangle[j][i]

        return f(0, 0)