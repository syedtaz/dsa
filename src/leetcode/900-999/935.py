class Solution:
    def knightDialer(self, n: int) -> int:
        def f(i: int) -> int:
            if i == 1:
                return 10

            a, b, c, d = 4, 2, 2, 1
            for _ in range(i - 1):
                a, b, c, d = 2 * (b + c) % 1000000007, a, (a + 2 * d) % 1000000007, c

            return (a + b + c + d) % 1000000007

        return f(n)
