from typing import List
from functools import cache


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def f(i: int) -> int:
            if i >= len(nums):
                return 0

            results = [f(j) for j in range(i + 1, len(nums)) if nums[i] < nums[j]] + [0]
            return 1 + max(results)

        return max([f(i) for i in range(len(nums))])
