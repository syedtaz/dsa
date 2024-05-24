from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        cands = [arr[n // 4], arr[n // 2], arr[(3 * n) // 4]]
        target = n // 4

        for cand in cands:
            left = bisect_left(arr, cand)
            right = bisect_right(arr, cand) - 1
            if right - left + 1 > target:
                return cand

        assert False
