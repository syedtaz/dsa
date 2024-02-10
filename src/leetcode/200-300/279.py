from functools import cache
from math import ceil, sqrt

class Solution:
    def numSquares(self, n: int) -> int:

        @cache
        def f(k: int, acc: int) -> int:
            if k <= 1:
                return acc + 1

            return min([f(k - j ** j, acc + 1) for j in range(1, int(ceil(sqrt(k))))])

        return f(n, 1)

s = Solution()
print(s.numSquares(13))