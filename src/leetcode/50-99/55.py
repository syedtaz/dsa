from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def f(i: int, last: int) -> bool:
            if i == 0:
                return last == 0

            return f(i - 1, nums[i]) if i + nums[i] >= last else False

        return f(len(nums) - 1, len(nums) - 1)
