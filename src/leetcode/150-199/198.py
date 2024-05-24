from typing import List
from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def f(i: int) -> int:
            if i >= len(nums):
                return 0

            yes = nums[i] + f(i + 2)
            no = f(i + 1)
            return max(yes, no)

        return f(0)
