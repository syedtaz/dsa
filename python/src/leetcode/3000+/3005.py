from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        _, v = c.most_common()[0]
        return sum([x for x in c.values() if x == v])
