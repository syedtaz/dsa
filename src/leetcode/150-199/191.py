from math import log2


class Solution:
    def hammingWeight(self, n: int) -> int:
        def check(i: int, idx: int) -> int:
            return 1 if (i >> idx) & 1 == 1 else 0

        bound = int(log2(n)) + 1 if n != 0 else 1
        acc = 0
        for i in range(bound):
            acc += check(n, i)
        return acc
