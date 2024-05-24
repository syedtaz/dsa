from typing import List
from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def set(x: int, i: int) -> int:
            return x | (1 << i)

        def check(x: int, i: int) -> int:
            return x & (1 << i)

        def eqsum(x: int) -> bool:
            l, r = 0, 0
            for i in range(len(nums)):
                if check(x, i):
                    l += nums[i]
                else:
                    r += nums[i]
            return l == r

        @cache
        def f(i: int, choices: int) -> bool:
            if i >= len(nums):
                return eqsum(choices)

            yes = f(i + 1, set(choices, i))
            no = f(i + 1, choices)
            return yes or no

        return f(0, 0)
