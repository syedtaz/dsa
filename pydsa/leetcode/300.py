from typing import List
from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

      @cache
      def f(i: int, last: int) -> int:
         if i > len(nums) - 1:
            return 0

         if nums[i] <= last:
            return f(i + 1, last)

         yes = 1 + f(i + 1, nums[i])
         no = f(i + 1, last)
         return max(yes, no)

      if len(nums) == 0:
         return 0

      return max([f(i, nums[i]) for i in range(len(nums))])