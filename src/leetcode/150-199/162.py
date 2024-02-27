from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def f(i: int, j: int) -> int:
            if i == j:
                return i

            mid = i + (j - i) // 2
            return f(i, mid) if nums[mid] > nums[mid + 1] else f(mid + 1, j)

        return f(0, len(nums) - 1)