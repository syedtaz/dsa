class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        # n = 3 ^ x for some x
        # => n - 3 ^ x = 0

        def f(x: int) -> bool:
            return abs(n - (3 ** x)) <= 0.0001

