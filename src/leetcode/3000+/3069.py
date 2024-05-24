from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        left: list[int] = [nums[0]]
        right: list[int] = [nums[1]]

        for num in nums[2:]:
            _ = left.append(num) if left[-1] > right[-1] else right.append(num)

        return left + right
