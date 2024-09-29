from math import log, floor


class Solution:
    divisor = 3 ** int(floor(log(2**31, 3)))

    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and self.divisor % n == 0
