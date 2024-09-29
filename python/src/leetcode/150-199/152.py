from typing import List
from sys import maxsize


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = -maxsize
        pref = 1
        for x in nums:
            m = max(m, pref := pref * x)
            if pref == 0:
                pref = 1

        suff = 1
        for x in reversed(nums):
            m = max(m, suff := suff * x)
            if suff == 0:
                suff = 1

        return m
