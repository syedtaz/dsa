from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        repr = [int(x) for x in str(n)]
        return reduce(lambda acc, x: acc * x, repr, 1) - sum(repr)
