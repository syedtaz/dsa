from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower = [x for x in nums if x < pivot]
        eq = [x for x in nums if x == pivot]
        higher = [x for x in nums if x > pivot]
        return lower + eq + higher