from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        nums.sort(key=lambda x: (counts[x], -x))
        return nums
