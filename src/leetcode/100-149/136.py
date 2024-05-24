from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        acc = 0
        for x in nums:
            acc ^= x
        return acc
