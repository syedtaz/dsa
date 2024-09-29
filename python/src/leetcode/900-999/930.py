from typing import List
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = 0
        prefixes = [0] + [pref := pref + x for x in nums]
        counts: dict[int, int] = defaultdict(int)
        acc = 0

        for x in prefixes:
            acc += counts.get(x - goal, 0)
            counts[x] += 1

        return acc
