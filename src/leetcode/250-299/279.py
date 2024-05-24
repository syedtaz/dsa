from functools import cache
from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def f(i: int) -> int:
            if i <= 1:
                return i

            return min(
                [1 + f(i - k) for j in range(1, int(sqrt(i)) + 1) if (k := j**2) <= i]
            )

        return f(n)
