from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        acc: list[int] = []

        for num in nums:
            if nums[abs(num) - 1] < 0:
                acc.append(abs(num))
                continue

            nums[abs(num) - 1] *= -1

        return acc
