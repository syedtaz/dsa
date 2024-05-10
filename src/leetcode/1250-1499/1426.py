from typing import List
from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        counts = Counter(arr)
        acc = 0

        for k, v in counts.items():
            if k + 1 in counts:
                acc += v
        return acc