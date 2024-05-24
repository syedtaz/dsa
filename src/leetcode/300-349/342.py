class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        pow2 = n & (n - 1) == 0
        hex = n & 0x10101010101010101010101010101010 == 0
        return pow2 and hex
