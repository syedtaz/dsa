from functools import cache


class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def g(i: int) -> int:
            if i <= 1:
                return 1

            return sum([g(j - 1) * g(i - j) for j in range(1, i + 1)])

        return g(n)
