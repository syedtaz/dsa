from typing import List
from functools import cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def recurrence(i: int, k: int) -> int:
            if i >= n:
                return 1 if k == 0 else 0

            plus = recurrence(i + 1, k + nums[i])
            minus = recurrence(i + 1, k - nums[i])
            return plus + minus

        return recurrence(0, target)
