from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:

        if len(nums) == 0:
            return True

        prev = nums.pop()

        while len(nums) > 0:
            if nums[-1] <= prev:
                prev = nums.pop()
            else:
                break

        if len(nums) == 0:
            return True

        return all(a <= b for (a, b) in zip(nums, nums[1:]))