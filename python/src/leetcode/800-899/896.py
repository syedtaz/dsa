from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incr = decr = True

        for a, b in zip(nums, nums[1:]):
            if a > b:
                incr = False
            if a < b:
                decr = False

        return incr or decr
