from functools import cache
from math import ceil


class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def f(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5

            if a <= 0:
                return 1.0

            if b <= 0:
                return 0.0

            results = [
                f(a - 4, b),
                f(a - 3, b - 1),
                f(a - 2, b - 2),
                f(a - 1, b - 3),
            ]

            return 0.25 * sum(results)

        return f(ceil(n / 25), ceil(n / 25)) if n < 5000 else 1.0
