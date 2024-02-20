from math import log2

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return abs(log2(n) - int(log2(n))) < 0.0000001