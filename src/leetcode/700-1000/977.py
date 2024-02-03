from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        acc : list[int] = [0] * len(nums)
        left, right = 0, len(nums) - 1

        for i in range(len(nums), -1, -1):
            a, b = abs(nums[left]), abs(nums[right])
            if a <= b:
                acc[i] = a * a
                left = left + 1
            else:
                acc[i] = b * b
                right = right - 1

        return acc
