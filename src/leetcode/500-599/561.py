from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([min(nums[2 * i], nums[2 * i + 1]) for i in range(len(nums) // 2)])