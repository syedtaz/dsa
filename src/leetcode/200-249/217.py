from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return any([a == b for a, b in zip(nums, nums[1:])])
