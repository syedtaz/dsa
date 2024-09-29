from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n, a, b = len(nums), 0, 0

        for i in nums:
            if nums[abs(i) - 1] < 0:
                a = abs(i)
            else:
                nums[abs(i) - 1] *= -1

        for i in range(1, n):
            if nums[i] > 0:
                b = i + 1

        return [a, b]
