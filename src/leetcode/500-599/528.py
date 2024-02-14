from typing import List
from random import random

class Solution:
    w: list[float]

    def __init__(self, w: List[int]):
        t = [(x / sum(w)) for x in w]
        self.w = [0.0] + [sum(t[:idx+1]) for idx in range(len(t))]

    def binary_search(self, i: int, j: int, v: float) -> int:
        mid = int(i + (j - i) / 2)
        if self.w[mid] <= v <= self.w[mid + 1]:
            return mid
        if self.w[mid] <= v:
            return self.binary_search(mid, j, v)
        else:
            return self.binary_search(i, mid, v)

    def pickIndex(self) -> int:
        x = random()
        return self.binary_search(0, len(self.w) - 1, x)
