from math import sqrt


class Solution:
    def pivotInteger(self, n: int) -> int:
        y = int(sqrt(x := n * (n + 1) // 2))
        return y if y * y == x else -1
