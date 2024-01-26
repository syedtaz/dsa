from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def f(x: int) -> int:
            if x == 0:
                return 1

            one = f(x - 1) if x >= 1 else 0
            two = f(x - 2) if x >= 2 else 0
            return one + two

        return f(n)