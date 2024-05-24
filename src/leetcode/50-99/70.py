class Solution:
    def climbStairs(self, n: int) -> int:
        table = [0] * n
        table[0] = 1
        for i in range(1, n):
            one = table[i - 1] if i >= 1 else 0
            two = table[i - 2] if i >= 2 else 0
            table[i] = one + two

        return table[n - 1]
