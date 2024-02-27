from typing import List
from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def recurrence(i: int, f: bool) -> int:
            if i >= len(nums):
                return 0 if f else nums[0]