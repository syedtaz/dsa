from collections import Counter
from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)

        for k, v in sorted(counts.items(), key=lambda x: x[0], reverse=True):
            if v == 1:
                return k

        return -1
