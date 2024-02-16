from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        return abs((len(nums) + 1) * (len(nums)) // 2 - s)
