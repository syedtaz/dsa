from typing import List
from bisect import bisect_left

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        acc = 0

        for i in range(n):
            for j in range(i + 1, n - 1):
                k = bisect_left(nums, nums[i] + nums[j], lo = j + 1)
                acc += k - j - 1

        return acc