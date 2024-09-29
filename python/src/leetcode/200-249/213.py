from typing import List
from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def f(i: int, first: bool) -> int:
            if i >= len(nums):
                return 0

            if i == len(nums) - 1:
                return 0 if first else nums[i]

            no = f(i + 1, first)
            yes = nums[i] + f(i + 2, first)
            return max(no, yes)

        return max(nums[0] + f(2, True), f(1, False))
