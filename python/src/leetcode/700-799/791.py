import math


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        map = {c: idx for idx, c in enumerate(order)}
        acc = [(idx, ch) for idx, ch in enumerate(s)]
        acc.sort(key=lambda x: map[x[1]] if x[1] in map else math.inf)
        return "".join([x for _, x in acc])
