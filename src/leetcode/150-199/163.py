from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        def f(i: int, cur: int, acc: list[list[int]]) -> list[list[int]]:
            if cur >= upper:
                return acc

            if i >= len(nums):
                return acc + [[cur, upper]]

            if nums[i] == cur:
                return f(i + 1, cur + 1, acc)

            return f(i, nums[i], acc + [[cur, nums[i] - 1]])

        return f(0, lower, [])