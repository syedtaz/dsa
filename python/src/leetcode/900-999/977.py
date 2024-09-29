from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        acc: list[int] = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            a, b = abs(nums[left]), abs(nums[right])

            if b > a:
                acc[i], right = b * b, right - 1
            else:
                acc[i], left = a * a, left + 1

        return acc
