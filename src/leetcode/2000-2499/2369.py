from typing import List
from functools import cache


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def f(i: int) -> bool:
            if i >= len(nums):
                return True

            return any(
                [
                    i + 1 < len(nums) and (nums[i] == nums[i + 1]) and f(i + 2),
                    i + 2 < len(nums)
                    and (nums[i] == nums[i + 1] == nums[i + 2])
                    and f(i + 3),
                    i + 2 < len(nums)
                    and (nums[i] == nums[i + 1] - 1 == nums[i + 2] - 2)
                    and f(i + 3),
                ]
            )

        return f(0)
