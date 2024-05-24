from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = [0] * 2001

        for k in arr:
            counts[k + 1000] -= 1

        counts.sort()
        for a, b in zip(counts, counts[1:]):
            if a != 0 and a == b:
                return False
        return True
