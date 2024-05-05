from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        acc = 0
        return [acc := acc + x for x in nums]