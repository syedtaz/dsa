from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        left, right = 0, len(nums) - 1
        acc = 0

        while left < right:
            if nums[left] + nums[right] < target:
                acc += right - left
                left += 1
            else:
                right -= 1

        return acc