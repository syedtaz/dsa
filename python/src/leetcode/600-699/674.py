from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i, acc, cur = 1, 1, 1

        while True:
            if i >= len(nums):
                return max(acc, cur)

            if nums[i] > nums[i - 1]:
                i, cur = i + 1, cur + 1
                continue

            acc = max(acc, cur)
            i, cur = i + 1, 1
