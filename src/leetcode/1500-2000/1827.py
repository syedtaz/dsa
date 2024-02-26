from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        acc = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                continue

            diff = nums[i - 1] - nums[i] + 1
            nums[i] = nums[i] + diff
            acc += diff

        return acc