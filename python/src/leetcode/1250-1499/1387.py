from functools import cache


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def power(x: int) -> int:
            if x == 1:
                return 0

            return 1 + power(x // 2) if x % 2 == 0 else 1 + power((3 * x) + 1)

        results = sorted([x for x in range(lo, hi + 1)], key=lambda x: power(x))
        return results[k - 1]
