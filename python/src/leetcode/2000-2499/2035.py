from typing import List
from functools import cache

# You are given an integer array nums of 2 * n integers. You need to partition
# nums into two arrays of length n to minimize the absolute difference of the
# sums of the arrays. To partition nums, put each element of nums into one of
# the two arrays.

# Return the minimum possible absolute difference.


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        @cache
        def f(i: int, j: int) -> int:
            if i <= j:
                return 0

            return min(
                [
                    abs(nums[i] - a) + b
                    for (a, b) in [
                        (nums[k], f(i, k) + f(k + 1, j)) for k in range(i + 1, j)
                    ]
                ]
            )

        return f(0, len(nums))
