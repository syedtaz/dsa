from typing import List
from sys import maxsize

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        acc = -maxsize

        for i in range(len(nums) // 2):
            acc = max(acc, nums[i] + nums[-i - 1])

        return acc