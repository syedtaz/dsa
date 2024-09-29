from math import floor


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1

        def f(a: float) -> float:
            return a * a - x

        def fixedpoint(i: float, j: float, prev: float) -> int:
            mid = i + (j - i) / 2
            res = f(mid)

            if abs(res - prev) < 0.05:
                return int(floor(mid))

            return fixedpoint(mid, j, res) if res < 0 else fixedpoint(i, mid, res)

        return fixedpoint(0, x, 0)
