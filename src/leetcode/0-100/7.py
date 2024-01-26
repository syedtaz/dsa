from math import log


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        neg = -1 if x < 0 else 1
        n = abs(x)
        d = int(log(n, 10)) + 1

        def pick(exp: int, acc: int) -> int:
            if exp == d + 1:
                return acc
            nacc = acc + (n % (10**exp) // (10 ** (exp - 1))) * (10 ** (d - exp))
            return pick(exp + 1, nacc)

        ans = pick(1, 0) * neg
        if ans < (2**31) * -1 or ans > (2**31) - 1:
            ans = 0

        return ans