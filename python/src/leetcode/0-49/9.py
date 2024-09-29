from math import log10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        n = int(log10(x)) + 1 if x != 0 else 0

        for i in range(1, n):
            left = x // (10 ** (n - i)) % 10
            right = x // (10 ** (i - 1)) % 10
            if left != right:
                return False

        return True
