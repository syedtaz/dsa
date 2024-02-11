from typing import List
from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def recurrence(i: int, k: int) -> int:
            if i >= n and k == 0:
                return