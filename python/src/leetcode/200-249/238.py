from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc = 1
        prefixes = [(acc := acc * x) for x in nums]

        acc = 1
        suffixes = [(acc := acc * x) for x in reversed(nums)][::-1]

        for i in range(len(nums)):
            pre = 1 if i == 0 else prefixes[i - 1]
            suf = 1 if i == len(nums) - 1 else suffixes[i + 1]
            nums[i] = pre * suf

        return nums
