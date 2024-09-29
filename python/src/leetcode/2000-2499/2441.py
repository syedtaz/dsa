from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        xs = set(nums)
        return max((xs := [x for x in xs if -x in xs])) if len(xs) > 0 else -1
