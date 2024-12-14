from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def f(x: int) -> bool:
            return sum([(a + x - 1) // x for a in piles]) <= h

        i, j = 1, max(piles)

        while i <= j:
            if f(m := i + (j - i) // 2):
                j = m - 1
            else:
                i = m + 1

        return i