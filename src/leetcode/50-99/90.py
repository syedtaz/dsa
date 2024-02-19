from typing import List
from functools import cache

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        @cache
        def powerset(i: int) -> list[list[int]]:
            if i == len(nums):
                return [[]]

            return [[nums[i]] + x for x in powerset(i + 1)] + powerset(i + 1)

        acc : set = set()

        for els in powerset(0):
            els.sort()
            acc.add(tuple(els))

        return [list(x) for x in acc]