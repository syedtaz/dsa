from typing import List
from functools import cache

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        @cache
        def f(i: int) -> list[list[int]]:
            return (
                [[]] if i == len(nums) else [[nums[i]] + x for x in f(i + 1)] + f(i + 1)
            )

        return f(0)

# s = Solution()
# print(s.subsets(nums=[0]))