class Solution:
    def climbStairs(self, n: int) -> int:
        match n:
            case 1 | 2:
                return n
            case _:
                a, b = 1, 2

                for _ in range(2, n):
                    c = a + b
                    a, b = b, c

                return b