from typing import List
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        acc = 0

        for [x1, y1] in points:
            counts: dict[int, int] = defaultdict(int)

            for [x2, y2] in points:
                dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
                counts[dist] += 1

            for v in counts.values():
                acc += v * (v - 1)
        return acc
