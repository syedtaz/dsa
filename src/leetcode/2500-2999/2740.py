from typing import List

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()

        diff = abs(nums[0] - nums[1])
        for (i, j) in zip(nums, nums[1:]):
            diff = min(diff, abs(i - j))

        return diff