from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        acc = 0
        csum = [(acc := acc + x) for x in nums]
        counts : dict[int, int] = defaultdict(int)
        count = 0

        for s in csum:
            counts[s] += 1
            count += 1 if s == k else 0
            count += counts[s-k] if (s - k in counts and k != 0) else 0

        return count